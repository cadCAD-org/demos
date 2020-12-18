
# Behaviors
def provider_choice(params, step, history, current_state):
    #fiat claimed by providers
    #note: balance of provided vol covered in tokens (computed later)
    txo_fiat = params['theta']*current_state['tx_volume']+ (1-params['theta'])*params['gamma']*current_state['volume_of_production']*current_state['cost_of_production']
    return {'txo_fiat': txo_fiat}


# Mechanisms 
def compensate_providers1(params, step, sL, s, _input):
    #fiat outbound
    y = 'fiat_reserve'
    x = s['fiat_reserve']-_input['txo_fiat']*(1.0-params['platform_fee'])
    return (y, x)

def compensate_providers2(params, step, sL, s, _input):
    #tokens outbound
    y = 'token_reserve'
    fiat_eq = s['tx_volume']-_input['txo_fiat']
    x = s['token_reserve']-s['conversion_rate']*fiat_eq*(1.0-params['platform_fee']-params['conversion_fee'])
    return (y, x)
