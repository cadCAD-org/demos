import numpy as np
import scipy.stats as sps
import datetime as dt
import pandas as pd



# Behaviors
def event(params, step, sL, s):

    error =s['price']-s['target']
    delta_time = sps.expon.rvs(loc = params['minimum_period'], scale = params['expected_lag'])

    return({'error':error, 'delta_time': delta_time})

def martingale(params, step, sL, s):

    theta = params['correction_wt']
    noise = np.random.randn()*params['noise_wt']
    raw_price = float(s['price'])/params['TOK']
    raw_target = float(s['target'])/params['TOK']

    raw_price = theta*raw_target+(1-theta)*raw_price + noise
    
    return({'raw_price':raw_price})

# Mechansims
def store_error(params, step, sL, s, _input):

    key = 'error'

    new_error = _input['error']
    old_error = s['error']['new']

    value = {'new':new_error, 'old':old_error}

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
        I = alpha^Dt *I + A  
    """

    new_error = s['error']['new']
    old_error = s['error']['old']

    e_bar = int((new_error+old_error)/2)

    Dt = s['Dt']

    area = e_bar*Dt

    alpha = params['alpha']
    remaing_frac = float(alpha/params['TOK'])**Dt

    remaining = int(remaing_frac*s['leaky_integral'])

    value = remaining+area
    key = 'leaky_integral'

    return(key, value)

def update_integral(params, step, sL, s, _input):
    """
    Given integral previous value I, and the last two errors [new_error, old_error] and time pased Dt
        A = Dt*(new_error+old_error)/2
        I = I + A  
    """

    new_error = s['error']['new']
    old_error = s['error']['old']

    e_bar = int((new_error+old_error)/2)

    Dt = s['Dt']

    area = e_bar*Dt

    value = s['integral']+area
    key = 'integral'

    return(key, value)



def price_move(params, step, sL, s, _input):

    raw_price = _input['raw_price']
    price = int(raw_price*params['TOK'])

    key = 'price'
    value = price

    return(key, value)

