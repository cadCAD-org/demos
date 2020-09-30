"""
Model parameters.
"""

# These are the initial conditions of the DAI-ETH Uniswap instance - https://etherscan.io/address/0x09cabEC1eAd1c0Ba254B09efb3EE13841712bE14
initial_values = {
    'DAI_balance': 5900000000000000000000,
    'ETH_balance': 30000000000000000000,
    'UNI_supply': 30000000000000000000
}


### Parameters

# These are the parameters of Uniswap that represent the fee collected on each swap. Notice that these are hardcoded in the Uniswap smart contracts, but we model them as parameters in order to be able to do A/B testing and parameter sweeping on them in the future.

sys_params = {
    'fee_numerator': [997],
    'fee_denominator': [1000]
}
