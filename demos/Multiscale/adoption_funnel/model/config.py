
from cadCAD.configuration import Experiment 
from cadCAD.configuration.utils import config_sim
from .state_variables import genesis_states
from .partial_state_update_block import partial_state_update_block 
from .sys_params import sys_params 
from .parts.utils import *

from copy import deepcopy
from cadCAD import configs
import scipy.stats as stats
import numpy as np

from typing import Dict, List


sim_config = config_sim(
    {
        'N': 1, # number of monte carlo runs
        'T': range(1000), # number of timesteps
        'M': sys_params, # system parameters
    }
)

exp = Experiment()

exp.append_configs(
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_block
)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # GENESIS SWEEP LOGIC # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

for c in exp.configs: # for each configuration object
    c.initial_state = deepcopy(c.initial_state) # make a deepcopy of the initial state dict (it's shared across configs by default)
 
    c.initial_state['pool'] = Adoption_Pool(c.sim_config['M']['SOURCE_POOL'])