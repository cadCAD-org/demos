# Dependences
import datetime as dt
from .sys_params import initial_values


## Initial state object
genesis_states = {
    'price': int(initial_values['TOK']), 
    'target': int(initial_values['TOK']), 
    'error': {'new':0, 'old':0}, 
    'leaky_integral': 0,
    'integral': 0,  
    'Dt': 0, #seconds
    'timestamp': dt.datetime.now() #date
}

