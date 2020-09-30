"""
Model parameters
"""

import numpy as np

initial_values = {
    'WAD': 10**18,
    'TOK':10**27,
    'RAD': 10**45,
    'SPY':31536000, # seconds per year
    'MAX':2**255,
    'SPH':60*60,
}


halflife=initial_values['SPY']/52 # weeklong halflife
alpha = int(np.power(.5,float(1/halflife))*initial_values['TOK'])



sys_params = {
    'expected_lag': [10],
    'minimum_period': [initial_values['SPH']],
    'correction_wt': [0.5],
    'noise_wt': [0.001],
    'alpha': [alpha],
    'TOK':[initial_values['TOK']],
}
