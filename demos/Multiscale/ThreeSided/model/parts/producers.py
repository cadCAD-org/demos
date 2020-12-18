
import numpy as np
#governance decision ~ system policy for compensating producers
#consider transaction volume, labor committed and token reserve and supply to determine payout

#this function is a parameter of this policy which determines diminishing value of more labor
base_value = 1000.0

def marginal_utility_function(x):
    #this is how much the platform value a total amount of production (in fiat)
    return base_value+np.sqrt(x)


# Behaviors
def producer_choice(params, step, history, current_state):
    #ROI heuristic
    # add or remove resources based on deviation from threshold
    if current_state['producer_roi_estimate'] < 0:
        delta_labor = current_state['volume_of_production']*(params['attrition_rate']-1.0)
    else:
        ratio = current_state['producer_roi_estimate']/params['roi_threshold']
        delta_labor = params['roi_gain']*current_state['volume_of_production']*(ratio-1.0)
    
    return {'delta_labor': delta_labor}

def producer_compensation_policy(params, step, history, current_state):
    tokens_paid = current_state['conversion_rate']*marginal_utility_function(current_state['volume_of_production'])
    return {'tokens_paid': tokens_paid}

# Mechanisms 
def commit_delta_production(params, step, sL, s, _input):
    y = 'volume_of_production'
    x = s['volume_of_production']+_input['delta_labor']
    return (y, x)


def compensate_production(params, step, sL, s, _input):
    y = 'token_reserve'
    x = s['token_reserve']-_input['tokens_paid']
    return (y, x)

def update_producer_roi_estimate(params, step, sL, s, _input):
    revenue = _input['tokens_paid']/s['conversion_rate']
    cost = s['cost_of_production']*s['volume_of_production']
    spot_ROI_estimate =   (revenue-cost)/cost
    y = 'producer_roi_estimate'
    x = params['rho']*spot_ROI_estimate + s['producer_roi_estimate']*(1.0-params['rho'])
    return (y, x)