import pandas as pd

sys_params = {
    'fee_numerator': [997, 997, 997, 997,
                        995, 995, 995, 995],
    'fee_denominator': [1000],
    'uniswap_events': [pd.read_pickle('uniswap_events.pickle')],
    'c_rule': [13,13,15,15,
                13,13,15,15],
    'conv_tolerance': [0.0005, 0.001, 0.0005, 0.001,
                        0.0005, 0.001, 0.0005, 0.001]
}