from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
from .state_variables import genesis_states
from .partial_state_update_block import PSUBs
from .sys_params import sys_params as sys_params
from .sim_params import *

sim_config = config_sim(
    {
        'N': MONTE_CARLO_RUNS,
        'T': range(SIMULATION_TIME_STEPS), 
        'M': sys_params,
    }
)

exp = Experiment()
exp.append_configs(
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=PSUBs
)