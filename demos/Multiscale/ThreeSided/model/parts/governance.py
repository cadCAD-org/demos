
# Behaviors
def budgeting_policy(params, step, history, current_state):
    #governance decision ~ system policy for budgeting to cover overhead costs
    #note that this is a naive Heuristic control policy based on 
    # Strategies described by human operators
    # there exist formal alternatives using stochastic optimal control

    #define an estimate of future overhead
    proj_overhead = current_state['overhead_cost'] #simple naive 
    
    #simple threshold based conditional logic
    if current_state['operational_budget']< params['buffer_runway']*proj_overhead:
        target_release = params['buffer_runway']*proj_overhead-current_state['operational_budget']
        if  current_state['fiat_reserve']-target_release > params['reserve_threshold']*current_state['fiat_reserve']:
            budget_released =  target_release
        else:
            budget_released = (1.0-params['reserve_threshold'])*current_state['fiat_reserve']
    else:
        budget_released = params['min_budget_release']*current_state['fiat_reserve']
    
    return {'budget_released': budget_released}

def minting_policy(params, step, history, current_state):
    '''
    governance decision ~ determines the conditions or schedule of new tokens minted
    '''
    mint =  (params['final_supply']-current_state['token_supply'])*params['release_rate']
    return {'mint': mint}


def conversion_policy(params, step, history, current_state):
    '''
    governance decision ~ system policy for token/fiat unit of value conversion
    '''
    ncr = params['conversion_rate_gain']*current_state['smooth_avg_token_reserve']/current_state['smooth_avg_fiat_reserve']
    return {'new_conversion_rate': ncr}

# Mechanisms 
def release_funds(params, step, sL, s, _input):
    #tokens outbound
    y = 'fiat_reserve'
    x = s['fiat_reserve'] - _input['budget_released']
    return (y, x)

def update_budget(params, step, sL, s, _input):
    #tokens outbound
    y = 'operational_budget'
    x = s['operational_budget'] + _input['budget_released']
    return (y, x)

def mint1(params, step, sL, s, _input):
    '''
    minting process mints into the reserve
    '''
    y = 'token_supply'
    x = s['token_supply'] + _input['mint']
    return (y, x)

def mint2(params, step, sL, s, _input):
    y = 'token_reserve'
    x = s['token_reserve'] + _input['mint']
    return (y, x)

def update_conversion_rate(params, step, sL, s, _input):
    y = 'conversion_rate'
    x = _input['new_conversion_rate']
    return (y, x)