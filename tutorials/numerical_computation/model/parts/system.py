import numpy as np
import scipy.stats as sps
import datetime as dt
import pandas as pd
from cadCAD.configuration.utils import access_block


# Behaviors
def event(params, step, sL, s):

    #error =s['price']-s['target']
    delta_time = sps.expon.rvs(loc = params['minimum_period'], scale = params['expected_lag'])

    #return({'error':error, 'delta_time': delta_time})
    return({'delta_time':delta_time})

def resolve_target_price(params, step, sL, s):

    Dt = s['Dt']

    target_price = s['target']*(1+s['price_adjustment_rate'])**Dt

    #return({'error':error, 'delta_time': delta_time})
    return({'target_price':target_price})


def martingale(params, step, sL, s):

    theta = params['correction_wt']
    noise = np.random.randn()*params['noise_wt']
    raw_price = float(s['price'])#/params['TOK']
    raw_target = float(s['target'])#/params['TOK']

    raw_price = theta*raw_target+(1-theta)*raw_price + noise
    
    return({'raw_price':raw_price})


def constant(params, step, sL, s):

    raw_price = params['fixed_price']
    
    return({'raw_price':raw_price})

# Mechansims
def store_market_price(params, step, sL, s, _input):

    key = 'price'

    value = _input['raw_price']

    return(key, value)

def store_target_price(params, step, sL, s, _input):

    key = 'target'

    value = _input['target_price']

    return(key, value)

def store_error(params, step, sL, s, _input):

    key = 'error'

    value = _input['target_price'] - _input['raw_price']

    return(key, value)

def time_move(params, step, sL, s, _input):

    seconds = _input['delta_time']
    td = dt.timedelta(days=0, seconds=seconds)
    key = 'timestamp'
    value = s['timestamp']+td

    return(key, value)

def store_Dt(params, step, sL, s, _input):

    key = 'Dt'
    value = np.floor(_input['delta_time'])

    return(key, value)


def update_leaky_integral(params, step, sL, s, _input):
    """
    Given integral previous value I, and the last two errors [new_error, old_error] and time pased Dt
        A = Dt*(new_error+old_error)/2
        I = I + A  
    """

    new_error = _input['target_price'] - _input['raw_price']

    old_error = s['error']
    #print(old_error)

    e_bar = (new_error+old_error)/2

    Dt = s['Dt']

    area = e_bar*Dt

    value = area+s['integral']*(1-params['leakage'])**Dt
    key = 'integral'

    return(key, value)

def price_move(params, step, sL, s, _input):

    raw_price = _input['raw_price']
    price = int(raw_price*params['TOK'])

    key = 'price'
    value = price

    return(key, value)

def store_control_action(params, step, sL, s, _input):

    continuous_rate = params['Kp']*s['error']+params['Ki']*s['integral']

    key = 'price_adjustment_rate'
    value = continuous_rate

    return(key, value)
