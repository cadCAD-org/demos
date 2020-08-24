
from cadCAD.configuration import Experiment #.append_configs
from cadCAD.configuration.utils import config_sim
# if test notebook is in parent above /src
from src.sim.model.state_variables import genesis_states
from src.sim.model.partial_state_update_block import partial_state_update_block #, partial_state_update_block_B
from src.sim.model.sys_params import sys_params #as sys_params_A
from src.sim.model.utils import *

from copy import deepcopy
from cadCAD import configs
import scipy.stats as stats
# import networkx as nx
import numpy as np

from typing import Dict, List

# from .utils import *

# if test notebook is in /src
# from model.state_variables import genesis_states
# from model.partial_state_update_block import partial_state_update_block
# from model.sys_params import sys_params as sys_params_A

from src.sim.sim_setup import SIMULATION_TIME_STEPS, MONTE_CARLO_RUNS

# sys_params: Dict[str, List[int]] = sys_params

sim_config = config_sim(
    {
        'N': MONTE_CARLO_RUNS, 
        'T': range(SIMULATION_TIME_STEPS), # number of timesteps
        'M': sys_params,
    }
)

exp = Experiment()

# Experiment.append_configs()
exp.append_configs(
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_block
)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # GENESIS SWEEP LOGIC # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

for c in configs: # for each configuration object
    c.initial_state = deepcopy(c.initial_state) # make a deepcopy of the initial state dict (it's shared across configs by default)
    # for k in c.initial_state: # for each state variable
    #     if k in c.sim_config['M']: # if there is a param with the same name in the params dict
    #         c.initial_state[k] = c.sim_config['M'][k] # assign the param value to the initial value of the state variable

    c.initial_state['pool'] = Adoption_Pool(c.sim_config['M']['SOURCE_POOL'])
    # c.initial_state['network']  = init_network(c.initial_state['network'], c.sim_config['M'])