
# Behaviors
#these are uncontrollerd choices of users in the provider consumer
def consumer_choice(params, step, history, current_state):
    #fiat paid by consumers
    #note: balance of consumption vol covered in tokens (computed later)
    
    #simple heuristic ~ the fraction of token payment is proportion to free supply share
    free_supply = current_state['token_supply']-current_state['token_reserve']
    share_of_free_supply = free_supply/ current_state['token_supply']
    
    txi_fiat= (1.0-share_of_free_supply)*current_state['tx_volume']
    return {'txi_fiat': txi_fiat}


# Mechanisms 
def capture_consumer_payments1(params, step, sL, s, _input):
    #fiat inbound
    y = 'fiat_reserve'
    x = s['fiat_reserve']+_input['txi_fiat']
    return (y, x)

def capture_consumer_payments2(params, step, sL, s, _input):
    #tokens inbound
    y = 'token_reserve'
    fiat_eq = s['tx_volume']-_input['txi_fiat']
    x = s['token_reserve']+s['conversion_rate']*fiat_eq*(1.0+params['conversion_fee'])
    return (y, x)
