# The following imports NEED to be in the exact order
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor

# Simulation configs, input any new simulations here
from prey_predator_sd import config
from prey_predator_abm import config
#from {new_simulation} import config

from cadCAD import configs
import pandas as pd


def run(drop_midsteps: bool=True) -> pd.DataFrame:
    """
    Run all experiments and return their output on the dataset column.
    Each line represents an iteration of the parameter-sweep combinations.
    """
    
    exec_mode = ExecutionMode()
    exec_context = ExecutionContext(exec_mode.local_mode)
    run = Executor(exec_context=exec_context, configs=configs)
    results = pd.DataFrame()

    (system_events, tensor_field, sessions) = run.execute()

    df = pd.DataFrame(system_events)
    results = []
    for i, (_, subset_df) in enumerate(df.groupby(["simulation", "subset"])):
        params = configs[i].sim_config['M']
        result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
        # keep only last substep of each timestep
        if drop_midsteps:
            max_substep = max(subset_df.substep)
            is_droppable = (subset_df.substep != max_substep)
            is_droppable &= (subset_df.substep != 0)
            subset_df = subset_df.loc[~is_droppable]
        result_record['dataset'] = [subset_df]
        results.append(result_record)

    return pd.concat(results).reset_index()