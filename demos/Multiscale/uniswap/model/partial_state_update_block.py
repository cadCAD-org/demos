from .parts.system import *

partial_state_update_block = [
    {
        # system.py
        'policies': {
            'user_action': actionDecoder
        },
        'variables': {
            'DAI_balance': mechanismHub_DAI,
            'ETH_balance': mechanismHub_ETH,
            'UNI_supply': mechanismHub_UNI
        }
    }
]