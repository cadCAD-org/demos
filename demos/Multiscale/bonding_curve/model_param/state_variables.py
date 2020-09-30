from datetime import datetime
import numpy as np
from .sys_params import initial_conditions

# Genesis States 
genesis_states = {
    'supply': initial_conditions['S0'],
    'price': initial_conditions['P0'],
    'reserve': initial_conditions['R0'],
    'spot_price': initial_conditions['P0'],
    'output_price': initial_conditions['P0'],

}
