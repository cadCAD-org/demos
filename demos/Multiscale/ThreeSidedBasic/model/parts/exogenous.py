import numpy as np


# Exogenous Mechanisms 
def tx_volume_generator(params, step, sL, s, _input):
    y = 'tx_volume'
    x = s['tx_volume']*(1+2*params['eta']*np.random.rand()*(1-s['tx_volume']/params['tampw']))
    return (y, x)

def product_cost_generator(params, step, sL, s, _input):
    y = 'product_cost'
    x = params['alpha']*s['product_cost']+params['beta']*np.random.rand() - params['costDecrease']
    return (y, x)

def investors_generator(params, step, sL, s, _input):
    y = 'seed_money'
    if s['timestep'] == 1:
        x = s['seed_money'] + params['vcRoundFunding']
    elif s['timestep'] == 10:
        x = s['seed_money'] + params['vcRoundFunding']
    else:
        x = s['seed_money'] + 0
    return (y, x)

def update_overhead_costs(params, step, sL, s, _input):
    # Create step function for updating overhead costs
    y = 'overhead_cost'
    if s['timestep']%15 == 0:
        x = s['overhead_cost'] + params['overHeadCosts']
    else:
        x = s['overhead_cost'] + 0
    return (y, x)

def R_and_D(params, step, sL, s, _input):
    y = 'R&D'
    if s['timestep']%17 == 0:
        x = s['R&D'] + 1000
    else:
        x = s['R&D'] + 0
    return (y, x) 

