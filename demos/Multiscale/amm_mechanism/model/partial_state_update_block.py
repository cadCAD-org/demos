"""
Partial state update block. 

Here the partial state update blocks are configurated by setting
- policies
- variables

for each state update block individually
"""

from .parts.uniswap import *
from .parts.metrics import *
from .parts.action_list import *

partial_state_update_block = [
    {
        # uniswap.py asset i AND j
        'policies': {
            'user_action': actionDecoder
        },
        'variables': {
            # UNISWAP WORLD
            'uni_agents': agenthub,
            'UNI_Ri': mechanismHub_Ri,
            'UNI_Qi': mechanismHub_Q,
            'UNI_Si': mechanismHub_Si,
            'UNI_Rj': mechanismHub_Ri,
            'UNI_Qj': mechanismHub_Q,
            'UNI_Sj': mechanismHub_Si,
            'UNI_ij': mechanismHub_ij,
            'UNI_ji': mechanismHub_ji,
        }
    },
    {
        # Metrics
        'policies': {
            # 'user_action': actionDecoder
        },
        'variables': {
            # UNISWAP WORLD
            'UNI_P_RQi': s_swap_price_i,
            'UNI_P_RQj': s_swap_price_j,
            'UNI_P_ij': s_swap_price_ij,
        }
    },
]