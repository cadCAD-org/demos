# The following imports NEED to be in the exact order
from cadCAD import configs
######### ADD FOR PRINTING CONFIG
from cadCAD.configuration.utils import *
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor

from src.sim import config


exec_mode = ExecutionMode()
exec_ctx = ExecutionContext(context=exec_mode.multi_proc)
simulation = Executor(exec_context=exec_ctx, configs=configs)
raw_system_events, tensor_field, session = simulation.execute()
df = pd.DataFrame(raw_system_events)

def get_M(k, v):
    if k == 'sim_config':
        k, v = 'M', v['M']
    return k, v

config_ids = [
    dict(
        get_M(k, v) for k, v in config.__dict__.items() if k in ['simulation_id', 'run_id', 'sim_config', 'subset_id']
    ) for config in configs
]

# 4.18 Method MC
def run(drop_midsteps=True, df = df):
    # results = df
    print('config_ids = ', config_ids)
    # sub_dfs = pd.DataFrame(columns= range(max(df.subset)+1))
    
    results = pd.DataFrame()
    for i, config_id in enumerate(config_ids):
        params = config_id['M']
        result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
        sub_df = df[df.subset == config_id['subset_id']]
        # sub_df = df[df.subset == config_id['subset_id']][df.run == config_id['run_id'] + 1]

        print(sub_df.head())
        if drop_midsteps:
            max_substep = max(sub_df.substep)
            is_droppable = (sub_df.substep != max_substep) & (sub_df.substep != 0)
            sub_df.drop(sub_df[is_droppable].index, inplace=True)


        # subset_id = max(sub_df.subset)
        # print(max(df.subset))
        # # sub_dfs = pd.DataFrame()
        # # if max(sub_df.subset) ==  
        # sub_dfs[subset_id].append(sub_df, ignore_index=True)
        # sub_dfs[subset_id].append(sub_df[subset_id])
        # sub_dfs[subset_id] = pd.concat(sub_dfs[subset_id])
        

        result_record['dataset'] = [sub_df]
        results = results.append(result_record)

    return results.reset_index()



# 4.18 Method One-Run
# def run(drop_midsteps=True, df = df):
#     # results = df
#     print('config_ids = ', config_ids)
#     sub_dfs = pd.DataFrame(columns= range(max(df.subset)+1))
    
#     results = pd.DataFrame()
#     for i, config_id in enumerate(config_ids):
#         params = config_id['M']
#         # result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
#         # sub_df = df[df.subset == config_id['subset_id']]
#         sub_df = df[df.subset == config_id['subset_id']][df.run == config_id['run_id'] + 1]

#         print(sub_df.head())
#         if drop_midsteps:
#             max_substep = max(sub_df.substep)
#             is_droppable = (sub_df.substep != max_substep) & (sub_df.substep != 0)
#             sub_df.drop(sub_df[is_droppable].index, inplace=True)


#         # subset_id = max(sub_df.subset)
#         # print(max(df.subset))
#         # # sub_dfs = pd.DataFrame()
#         # # if max(sub_df.subset) ==  
#         # sub_dfs[subset_id].append(sub_df, ignore_index=True)
#         # sub_dfs[subset_id].append(sub_df[subset_id])
#         # sub_dfs[subset_id] = pd.concat(sub_dfs[subset_id])
        
#         result_record['dataset'] = [sub_df]
#         results = results.append(result_record)

#     return results.reset_index()

# 4.17 method

# def run(drop_midsteps=True):
#     print('config_ids = ', config_ids)
#     result_records_list, sim_id_records = [], []
#     results = pd.DataFrame()
#     sim_ids = list(set([_id['simulation_id'] for _id in config_ids]))
#     sim_dfs = {_id: [] for _id in sim_ids}
#     for i, config_id in enumerate(config_ids):
#         sim_id, run_id = config_id['simulation_id'], config_id['run_id']
#         params = config_id['M']
#         result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))

#         mod_record = {'sim_id': sim_id, 'meta': result_record}
#         if sim_id not in sim_id_records:
#             sim_id_records.append(sim_id)
#             result_records_list.append(mod_record)

#         sim_id = config_id['simulation_id']
#         print('sim id first loop = ',sim_id)

#         sub_df = df[df.simulation == config_id['simulation_id']][df.run == config_id['run_id'] + 1]
#         sim_dfs[sim_id].append(sub_df)
#         # print(sub_df[['simulation', 'run', 'substep', 'timestep']].tail(5))
#         # print(sub_df.tail(5))

#     for sim_id in sim_ids:
#         result_record = [d for d in result_records_list if d['sim_id'] == sim_id][0]['meta']
#         sim_dfs[sim_id] = pd.concat(sim_dfs[sim_id])
#         sub_df = sim_dfs[sim_id]

#         print('sim id second loop = ',sim_id)
#         # keep only last substep of each timestep
#         if drop_midsteps:
#             max_substep = max(sub_df.substep)
#             is_droppable = (sub_df.substep != max_substep) & (sub_df.substep != 0)
#             sub_df.drop(sub_df[is_droppable].index, inplace=True)

#         # print(sub_df.head(3))
#         # print(sub_df.tail(3))
#         result_record['dataset'] = [sub_df]
#         results = results.append(result_record)
#         # print(sub_df[['simulation', 'run', 'substep', 'timestep']].tail(5))

#     return results.reset_index()

# RUN on 0.3.15
def run_3(drop_midsteps=True):
    exec_mode = ExecutionMode()
    multi_proc_ctx = ExecutionContext(context=exec_mode.multi_proc)
    run = Executor(exec_context=multi_proc_ctx, configs=configs)
    results = pd.DataFrame()
    i = 0
    for raw_result, _ in run.execute():
        params = configs[i].sim_config['M']
        result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))

        df = pd.DataFrame(raw_result)
        # keep only last substep of each timestep
        if drop_midsteps:
            max_substep = max(df.substep)
            is_droppable = (df.substep != max_substep) & (df.substep != 0)
            df.drop(df[is_droppable].index, inplace=True)

        result_record['dataset'] = [df]
        results = results.append(result_record)
        i += 1
    return results.reset_index()

print(run().head(1))
