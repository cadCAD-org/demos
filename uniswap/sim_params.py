import pandas as pd

SIMULATION_TIME_STEPS = len(pd.read_pickle('~/Documents/uniswap/uniswap_events.pickle'))-2
MONTE_CARLO_RUNS = 1