import pandas as pd

sys_params = {
    'fee_numerator': [997, 997, 997, 995, 995, 995, 993, 993, 993],
    'fee_denominator': [1000],
    'uniswap_events': [pd.read_pickle('uniswap_events.pickle')],
    'c_rule': [13],
    'conv_tolerance': [0.15, 0.10, 0.05, 0.15, 0.10, 0.05, 0.15, 0.10, 0.05],
    'fix_cost': [1],
}