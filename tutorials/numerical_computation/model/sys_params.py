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



sys_params = {
    'expected_lag': [10],
    'minimum_period': [initial_values['SPH']],
    'correction_wt': [0.5],
    'noise_wt': [0.001],
    'TOK':[initial_values['TOK']],
}
