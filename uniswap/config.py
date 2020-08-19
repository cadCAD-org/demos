from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
# from .model.state_variables import genesis_states
from .model.partial_state_update_block import PSUBs
# from .model.sys_params import sys_params as sys_params
# from .sim_params import *

sys_params = {
    'fee_numerator': [997],
    'fee_denominator': [1000]
}

genesis_states = {
    'DAI_balance': 5900000000000000000000,
    'ETH_balance': 30000000000000000000,
    'UNI_supply': 30000000000000000000
}

SIMULATION_TIME_STEPS = 100
MONTE_CARLO_RUNS = 1

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