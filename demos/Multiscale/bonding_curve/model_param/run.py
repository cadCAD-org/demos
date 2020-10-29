import pandas as pd
from model_param import config 
from cadCAD.engine import ExecutionMode, ExecutionContext,Executor
from cadCAD import configs



def run():
    '''
    Definition:
    Run simulation
    '''
    exec_mode = ExecutionMode()
    multi_mode_ctx = ExecutionContext(context=exec_mode.multi_proc)


    simulation = Executor(exec_context=multi_mode_ctx, configs=configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    # Result System Events DataFrame
    df = pd.DataFrame(raw_system_events)
    
  
    
    return df
    

def postprocessing(df):
    '''
    '''
    # Clean substeps
    first_ind = (df.substep == 0) & (df.timestep == 0)
    last_ind = df.substep == max(df.substep)
    inds_to_drop = (first_ind | last_ind)
    df = df.loc[inds_to_drop].drop(columns=['substep'])

    # Attribute parameters to each row
    df = df.assign(**configs[0].sim_config['M'])
    for i, (_, n_df) in enumerate(df.groupby(['simulation', 'subset', 'run'])):
        df.loc[n_df.index] = n_df.assign(**configs[i].sim_config['M'])

    df['err'] = df.price-df.spot_price
    df['abs_err']= df.err.apply(abs)
    df['rel_err'] = df.abs_err/df.spot_price

        
    return df



