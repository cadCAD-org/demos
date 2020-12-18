

# params
params = {
    'eta': [.065], # for tx_volume_generator
    'tampw': [100000], # transactions limit
    'alpha': [.9], # for cost_of_production_generator
    'beta': [1.0], # for cost_of_production_generator
    'flat': [500], #log quadratic overhead model; parameters
    'a': [1000.0],
    'b': [100.0],
    'c': [1.0],
    'd': [1.0],
    'theta': [0.6], #theta percent of service providers ALWAYS use fiat,
    'gamma': [0.1], #parameter gamma is a tuning gain
    'roi_threshold': [.2],
    'attrition_rate': [.5],
    'roi_gain': [0.025],
    'conversion_fee': [.03],
    'platform_fee': [0.075],
    'rho': [.1],
    'buffer_runway': [3.0],
    'reserve_threshold': [.25],
    'min_budget_release': [0],
    'final_supply': [1000000.0], #1M #unit: tokens
    'release_rate':[.01], #percent of remaining,
    'conversion_rate_gain': [1]
}



# Initial States
initial_values = {
    'fiat_reserve': float(25000),#unit: fiat
    'overhead_cost': float(500), #unit: fiat
    'operational_budget': float(25000), #unit: fiat
    'token_reserve': float(25000),#unit: tok
    'token_supply': float(25000),#unit: tok
    'tx_volume': float(1000), #unit: fiat
    'conversion_rate': float(1), #unit: tok/fiat
    'cost_of_production': float(10), #unit: fiat/labor
    'volume_of_production': float(20), #unit: labor
    'producer_roi_estimate': float(1.1), #unitless //signal for informing policies
    'smooth_avg_fiat_reserve': float(25000), #unit: fiat //signal for informing policies
    'smooth_avg_token_reserve': float(25000), #unit: token //signal for informing policies
}