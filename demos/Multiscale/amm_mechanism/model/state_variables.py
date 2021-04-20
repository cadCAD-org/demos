"""
State variables are defined here.

We set:
- dependencies
- agent parameters (agent dataframe)
- asset parameters (asset daraframe)
- potential new asset parameters (new_asset dataframe)


In addition to that, we initialize:
- all Uniswap pools
- the initial state object
"""

# Dependences
from .parts.utils import *
from .sys_params import C, initial_values

import pandas as pd
########## AGENT INITIALIZATION ##########
number_of_agents = 8

# Configure agents for agent-based model
agents_df = pd.DataFrame({
    'r_i_out': 0, # reserve asset not in pool
    'r_i_in': 0, # reserve asset put into pool- virtual
    'h': 0, # base asset not in pool
    'q_i': 0, # base asset in pool- virtual (if added Q)
    's_i': 0, # i_reserve asset share of pool
    's_q': 0, # q_base asset share of pool
    'r_j_out': 0, # reserve asset not in pool
    'r_j_in': 0, # reserve asset put into pool- virtual
    'q_j': 0, # base asset in pool- virtual (if added Q)
    's_j': 0, # i_reserve asset share of pool
    }, index=[0])
agents_df = pd.concat([agents_df]*number_of_agents, ignore_index=True)
# Adding IDs to agents
agents_df.insert(0, 'm', range(0, len(agents_df)))

agents_df['r_i_out'] = 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['h'] =  100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['s_i'] =   100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['q_i'] =  100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['r_i_in'] =  100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['r_j_out'] = 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['s_j'] =  100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['r_j_in'] =  100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000
agents_df['q_j'] =  100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000

#############################################################################################
UNI_P_RQi = initial_values['UNI_Qi'] / initial_values['UNI_Ri']
UNI_P_RQj = initial_values['UNI_Qj'] / initial_values['UNI_Rj']
UNI_P_ij = initial_values['UNI_ij'] / initial_values['UNI_ji']


## Initial state object
initial_state = {
    # UNISWAP Global Vars
    'UNI_Qi': initial_values['UNI_Qi'],
    'UNI_Ri': initial_values['UNI_Ri'],
    'UNI_Si': initial_values['UNI_Si'],
    'UNI_Qj': initial_values['UNI_Qj'],
    'UNI_Rj': initial_values['UNI_Rj'],
    'UNI_Sj': initial_values['UNI_Sj'],
    'UNI_ij': initial_values['UNI_ij'],
    'UNI_ji': initial_values['UNI_ji'],
    'UNI_Sij': initial_values['UNI_Sij'],
    # Uniswap Local Vars
    'uni_agents': agents_df,
    # Metrics
    'UNI_P_RQi' : UNI_P_RQi,
    'UNI_P_RQj' : UNI_P_RQj,
    'UNI_P_ij' : UNI_P_ij,
}


