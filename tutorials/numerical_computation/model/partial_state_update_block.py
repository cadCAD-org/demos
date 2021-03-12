from .parts.system import *

partial_state_update_block = [
    {
        # system.py
        'policies': 
            {
            'update_event': event
            },
        'variables': 
            {
            'timestamp':time_move,
            'Dt': store_Dt
            }
    },
    {
        # system.py
        'policies': 
            {
            'target_price': resolve_target_price,
            'market_price': martingale
            },
        'variables': 
            {
            'price':store_market_price,
            'target': store_target_price,
            'error': store_error,
            'integral': update_leaky_integral,
            }
    },
    {
        'policies':
            {
            },
        'variables':
            {
            'price_adjustment_rate': store_control_action
            }   
    }
]