import pandas as pd
from .sys_params import initial_values
from model import config 
from cadCAD.engine import ExecutionMode, ExecutionContext,Executor
from cadCAD import configs

def run():
    '''
    Definition:
    Run simulation
    '''
    # Single
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    simulation = Executor(exec_context=local_mode_ctx, configs=configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    # Result System Events DataFrame
    df = pd.DataFrame(raw_system_events)
    
    return df


def postprocessing(df):
    '''
    Definition:
    Refine and extract metrics from the simulation
    
    Parameters:
    df: simulation dataframe
    '''

    rdf = df[df.substep<=1]
    rdf = rdf.drop_duplicates(subset=['simulation','run', 'substep', 'timestep'])
    
    rdf['normed_integral'] = rdf.integral.apply(lambda x: x/(initial_values['TOK']*initial_values['SPH']))
    rdf['normed_price'] = rdf.price.apply(lambda x: x/initial_values['TOK'])
    rdf['normed_target'] = rdf.target.apply(lambda x: x/initial_values['TOK'])
    rdf['normed_error']  = rdf.normed_price-rdf.normed_target
    
    rdf['new_error'] = rdf.error.apply(lambda x: x['new'])
    rdf['old_error'] = rdf.error.apply(lambda x: ['old'])

    rdf['normed_new_error'] = rdf.error.apply(lambda x: float(x['new']/initial_values['TOK']))
    rdf['normed_old_error'] = rdf.error.apply(lambda x: float(x['old']/initial_values['TOK']))

    rdf['mean_error'] = rdf.error.apply(lambda x: int((x['new']+x['old'])/2))
    rdf['cast_mean_error'] = rdf.mean_error.apply(float)
    rdf['normed_mean_error'] = rdf.cast_mean_error.apply(lambda x: float(x/initial_values['TOK']))

    
    return rdf