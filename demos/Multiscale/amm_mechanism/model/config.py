from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
from .state_variables import initial_state
from .partial_state_update_block import partial_state_update_block
from .sys_params import params 

sim_config = config_sim (
    {
        'N': 1, # number of monte carlo runs
        'T': range(1000), # number of timesteps - 147439 is the length of uniswap_events
        'M': params, # simulation parameters
    }
)

exp = Experiment()

exp.append_configs(
    sim_configs=sim_config,
    initial_state=initial_state,
    partial_state_update_blocks=partial_state_update_block
)
