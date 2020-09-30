import pandas as pd
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
    
     # subset to last substep
    df = df[df['substep'] == df.substep.max()]
    
    return df
