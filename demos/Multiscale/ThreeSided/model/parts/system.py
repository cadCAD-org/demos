
# Mechanisms
def update_smooth_avg_fiat_reserve(params, step, sL, s, _input):
    y = 'smooth_avg_fiat_reserve'
    x = s['fiat_reserve']*params['rho']+s['smooth_avg_fiat_reserve']*(1-params['rho'])
    return (y, x)

def update_smooth_avg_token_reserve(params, step, sL, s, _input):
    y = 'smooth_avg_token_reserve'
    x = s['token_reserve']*params['rho']+s['smooth_avg_token_reserve']*(1-params['rho'])
    return (y, x)

