import numpy as np


# Exogenous Mechanisms 
def tx_volume_generator(params, step, sL, s, _input):
    y = 'tx_volume'
    x = s['tx_volume']*(1+2*params['eta']*np.random.rand()*(1-s['tx_volume']/params['tampw']))
    return (y, x)

def cost_of_production_generator(params, step, sL, s, _input):
    y = 'cost_of_production'
    x = params['alpha']*s['cost_of_production']+params['beta']*np.random.rand()
    return (y, x)

def overhead_cost_generator(params, step, sL, s, _input):
    #unit fiat
    y = 'overhead_cost'
    q = params['a']+params['b']*s['tx_volume']+params['c']*s['volume_of_production']+params['d']*s['tx_volume']*s['volume_of_production']
    x = params['flat']+np.log(q)
    return (y, x)