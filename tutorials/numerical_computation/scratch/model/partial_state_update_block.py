from .parts.system import *

partial_state_update_block = [
    {
        # system.py
        'policies': {
            'update_event': event
        },
        'variables': {
            'error': store_error,
            'timestamp':time_move,
            'Dt': store_Dt
        }
    },
    {
        'policies': {
        },
        'variables': {
            'leaky_integral': update_leaky_integral,
            'integral': update_integral,
        }
    },
    {
        'policies': {
            'martingale': martingale        
        },
        'variables': {
            'price': price_move,
        }
    },
]