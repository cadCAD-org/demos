# Dependences
from .parts.utils import *
from .sys_params import initial_values


## Initial state object
genesis_states = {
    'DAI_balance': initial_values['DAI_balance'],
    'ETH_balance': initial_values['ETH_balance'],
    'UNI_supply': initial_values['UNI_supply']
}


