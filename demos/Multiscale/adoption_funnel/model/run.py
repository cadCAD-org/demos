import pandas as pd
from cadCAD.engine import ExecutionMode, ExecutionContext,Executor
from .config import exp


def get_M(k, v):
    if k == 'sim_config':
        k, v = 'M', v['M']
    return k, v

config_ids = [
    dict(
        get_M(k, v) for k, v in config.__dict__.items() if k in ['simulation_id', 'run_id', 'sim_config', 'subset_id']
    ) for config in exp.configs
]


def run(drop_midsteps=True):
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
    
    config_ids = [
    dict(
        get_M(k, v) for k, v in config.__dict__.items() if k in ['simulation_id', 'run_id', 'sim_config', 'subset_id']
    ) for config in exp.configs
]
    
    results_list = []
    for i, config_id in enumerate(config_ids):
        params = config_id['M']
        result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
        sub_df = df[df.subset == config_id['subset_id']]

        max_substep = max(sub_df.substep)
        is_droppable = (sub_df.substep != max_substep) & (sub_df.substep != 0)
        sub_df.drop(sub_df[is_droppable].index, inplace=True)


        result_record['dataset'] = [sub_df]
        results_list.append(result_record)

    results = pd.concat(results_list)   
    return results.reset_index()
    



