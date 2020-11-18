import pandas as pd

sys_params = {
    'fee_numerator': [990, 990, 990, 990,
                        970, 970, 970, 970],
    'fee_denominator': [1000],
    'uniswap_events': [pd.read_pickle('uniswap_events.pickle')],
    'c_rule': [13,13,12,12,
                13,13,12,12],
    'conv_tolerance': [0.025, 0.005, 0.025, 0.005,
                        0.025, 0.005, 0.025, 0.005],
    'fix_cost': [1],
}