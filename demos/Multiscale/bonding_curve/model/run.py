import pandas as pd
from model import config 
from cadCAD.engine import ExecutionMode, ExecutionContext,Executor
from cadCAD import configs



def run():
    '''
    Definition:
    Run simulation
    '''
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    simulation = Executor(exec_context=local_mode_ctx, configs=configs)
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
    df['price_pc']=df.price.pct_change()
    df['spot_price_pc']=df.spot_price.pct_change()
    
    return df


