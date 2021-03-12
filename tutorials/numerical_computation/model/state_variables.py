# Dependences
import datetime as dt
from .sys_params import initial_values


## Initial state object
genesis_states = {
    # 'price': int(initial_values['TOK']), 
    # 'target': int(initial_values['TOK']), 
    'price': 4, 
    'target': 3.5, 
    'error': -.5, 
    'integral': -.5,  
    'Dt': 0, #seconds
    'timestamp': dt.datetime.now(), #date
    'price_adjustment_rate': -5e-7
}

