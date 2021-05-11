import itertools

"""
Model parameters.

We set:
- trade types
- liquidity action
- multiple asset action
- composite asset action type
- asymetric vs symetric liquidity action type

In addition to that, we define:
- asset initial values
- fees
- as well as the above parameters
"""
############### TRADES ################################################################
# exo_trade = [True] #['noisy', 'r_skewed', 'q_skewed', 'high_magnitude', 'high_frequency']
# exo_trade = ['noisy', 'r_skewed', 'q_skewed', 'high_magnitude', 'high_frequency']
# exo_trade = ['test_q_for_r'] # agent 0
# exo_trade = ['test_r_for_q'] # agent 1
# exo_trade = ['pass'] # No trades 
exo_trade = ['test_r_for_r'] # agent 1

# Test branch push #

################## TRADE SIZE ########################################
# exo_trade_size = ['fix_size']  # agent 5?
exo_trade_size = ['vary_size'] # agent 5?
mu = [500]
sigma = [100]

############### RANDOM SEQUENCE - add -swap -remove #####################
#exo_random_sequence = ['off'] 
exo_random_sequence = ['on'] 

################## LIQUIDITY ######################################################
# exo_liq = ['test_add']  # agent 2
# exo_liq = ['test_remove'] # agent 3
exo_liq = ['pass'] # No liquidity actions 

############## MULTIPLE ASSET ACTION TYPE #########################
#exo_asset = ['alternating']
exo_asset = ['i_only']
# exo_asset = ['j_only']


############## COMPOSITE ACTION TYPE #########################
exo_composite = ['alternating'] # add liq then trade
# exo_composite = ['trade_bias'] # add liq then trade

###################### ASYMMETRIC / SYMMETRIC LIQUIDITY #################################
# Uniswap permits symmetric adds , this will allow a naive implementation of assymetric add and removes, 
# but must account for the correct comparison to another system 
ENABLE_SYMMETRIC_LIQ = [True] 
# ENABLE_SYMMETRIC_LIQ = [False] # False

ACTION_LIST = [['test_add', 'test_r_for_q', 'test_q_for_r','test_r_for_r', 'test_remove']]
# ACTION_LIST = [['test_add', 'test_r_for_q', 'test_q_for_r', 'test_remove']]

# ACTION_LIST = [['test_add', 'test_r_for_r', 'test_remove']]
asset_initial_values = {
    'i' : 
        {'R': 1000000,
        'Q': 2000000,
        # 'S': 100000000 * 200000000},
        'S': 10000},

    'j' : 
        {'R': 1000000,
        'Q': 2000000,
        # 'S': 100000000 * 200000000},
        'S': 10000},
}

######################### Initialize Shares in Omnipool Differently #############
Q = asset_initial_values['i']['Q'] + asset_initial_values['j']['Q']
Sq = Q
BTR = Sq / Q

C = asset_initial_values['i']['S'] * asset_initial_values['j']['S']**2 # squared for same as asset k 

##########  reserve invariance function #1
#a = [1]
ENABLE_BALANCER_PRICING = [True] 

initial_values = {
    'UNI_Qi': asset_initial_values['i']['Q'],
    'UNI_Ri': asset_initial_values['i']['R'],
    'UNI_Si': asset_initial_values['i']['S'],
    'UNI_Qj': asset_initial_values['j']['Q'],
    'UNI_Rj': asset_initial_values['j']['R'],
    'UNI_Sj': asset_initial_values['j']['S'],
    'UNI_ij': asset_initial_values['i']['R'],
    'UNI_ji': asset_initial_values['j']['R'],
    'UNI_Sij': asset_initial_values['j']['R']*asset_initial_values['i']['R'],
    'Ri': asset_initial_values['i']['R'],
    # 'Si': 5*asset_initial_values['i']['R'],
    'Si': asset_initial_values['i']['S'],
    'Rj': asset_initial_values['j']['R'],
    # 'Sj': 5*asset_initial_values['j']['R'],
    'Sj': asset_initial_values['j']['S'],
    'Sq': asset_initial_values['i']['S'] + asset_initial_values['j']['S'],
    # 'Sq': 5*Q,
    'Q':  asset_initial_values['i']['Q'] + asset_initial_values['j']['Q'],
    'H':  asset_initial_values['i']['Q'] + asset_initial_values['j']['Q'],
}
# print(initial_values['Q'])
#################################################################################################################
fee_numerator = [990, 997, 1000]
fee_denominator = [1000]

### Parameters
factors = [fee_numerator, fee_denominator, exo_trade, exo_liq, ENABLE_SYMMETRIC_LIQ, exo_asset, exo_composite, ACTION_LIST, ENABLE_BALANCER_PRICING]
product = list(itertools.product(*factors))
fee_numerator, fee_denominator, exo_trade, exo_liq, ENABLE_SYMMETRIC_LIQ, exo_asset, exo_composite, ACTION_LIST, ENABLE_BALANCER_PRICING = zip(*product)
fee_numerator = list(fee_numerator)
fee_denominator = list(fee_denominator)
exo_trade =  list(exo_trade)
exo_liq =  list(exo_liq)
ENABLE_SYMMETRIC_LIQ = list(ENABLE_SYMMETRIC_LIQ)
exo_asset =  list(exo_asset)
exo_composite = list(exo_composite)
ACTION_LIST =  list(ACTION_LIST)
ENABLE_BALANCER_PRICING = list(ENABLE_BALANCER_PRICING)
# These are the parameters of Uniswap that represent the fee collected on each swap. Notice that these are hardcoded in the Uniswap smart contracts, but we model them as parameters in order to be able to do A/B testing and parameter sweeping on them in the future.

params = {
    'fee_numerator': fee_numerator,
    'fee_denominator': fee_denominator,
    'exo_trade': exo_trade, 
    'exo_liq' : exo_liq,
    'ENABLE_SYMMETRIC_LIQ' : ENABLE_SYMMETRIC_LIQ,
    'exo_asset' : exo_asset,
    'exo_composite' : exo_composite,
    'ACTION_LIST': ACTION_LIST,
    'ENABLE_BALANCER_PRICING': ENABLE_BALANCER_PRICING,
    'exo_trade_size': exo_trade_size,
    'mu': mu,
    'sigma': sigma,
    'exo_random_sequence': exo_random_sequence,
}
