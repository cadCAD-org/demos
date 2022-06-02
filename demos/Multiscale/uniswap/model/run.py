import pandas as pd
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from .config import exp
def run(drop_midsteps: bool=True) -> pd.DataFrame:
    """
    Run all experiments and return their output on the dataset column.
    Each line represents an iteration of the parameter-sweep combinations.
    """

    exec_mode = ExecutionMode()
    local_proc_ctx = ExecutionContext(context=exec_mode.multi_mode)
    simulation = Executor(exec_context=local_proc_ctx, configs=exp.configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    simulation_result = pd.DataFrame(raw_system_events)
    return simulation_result
