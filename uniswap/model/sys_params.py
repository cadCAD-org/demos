import pandas as pd

sys_params = {
    'fee_numerator': [997, 997, 997, 997,
                        995, 995, 995, 995],
    'fee_denominator': [1000],
    'uniswap_events': [pd.read_pickle('uniswap_events.pickle')],
    'c_rule': [3,3,15,15,
                3,3,15,15],
    'conv_tolerance': [0.0005, 0.025, 0.0005, 0.025,
                        0.0005, 0.025, 0.0005, 0.025]
}