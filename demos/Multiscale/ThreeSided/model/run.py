import pandas as pd
from .parts.utils import * 
from cadCAD.engine import ExecutionMode, ExecutionContext,Executor
from .config import exp

def run():
    '''
    Definition:
    Run simulation
    '''
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    simulation = Executor(exec_context=local_mode_ctx, configs=exp.configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    # Result System Events DataFrame
    df = pd.DataFrame(raw_system_events)
    return df



def postprocessing(df, sim_ind=-1):
    '''
    Function for postprocessing the simulation results 
    '''
    # subset to last substep of each simulation
    df= df[df.substep==df.substep.max()]

    mean_df,median_df,std_df,min_df = aggregate_runs(df,'timestep')

    return mean_df,median_df,std_df,min_df