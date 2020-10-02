from .policy_aux import *
from .suf_aux import *

# Policy

def p_actionDecoder(_params, substep, sH, s):
    uniswap_events = _params[0]['uniswap_events']
    
    prev_timestep = s['timestep']
    if substep > 1:
        prev_timestep -= 1
        
    #skip the first two events, as they are already accounted for in the initial conditions of the system
    t = prev_timestep + 2 
    
    action = {
        'eth_sold': 0,
        'tokens_sold': 0,
        'eth_deposit': 0,
        'UNI_burn': 0,        
    }

    #Event variables
    event = uniswap_events['event'][t]
    action['action_id'] = event

    if event in ['TokenPurchase', 'EthPurchase']:
        I_t, O_t, I_t1, O_t1, delta_I, delta_O, action_key = get_parameters(uniswap_events, event, s, t)
        if classifier(delta_I, delta_O, _params[0]['c_rule']) == "Conv":
            #do conv stuff
            
            calculated_delta_O = int(get_input_price(delta_I, I_t, O_t, _params[0]))
            historic_delta_O = int(get_input_price(delta_I, I_t1, O_t1, _params[0]))
            if calculated_delta_O >= historic_delta_O * (1 - _params[0]['conv_tolerance']):
                action[action_key] = delta_I
        else:
            #do arbt stuff
            
            P = (I_t + delta_I) / (O_t + delta_O)
            actual_P = I_t / O_t
            if(actual_P > P):
                I_t, O_t, I_t1, O_t1, delta_I, delta_O, action_key = get_parameters(uniswap_events, reverse_event(event), s, t)
                delta_I = get_delta_I(P, I_t, O_t, _params[0])
                action[action_key] = delta_I
            else:
                delta_I = get_delta_I(P, I_t, O_t, _params[0])
                action[action_key] = delta_I
    elif event == 'AddLiquidity':
        delta_I = uniswap_events['eth_delta'][t]
        action['eth_deposit'] = delta_I
    elif event == 'Transfer':
        UNI_delta = uniswap_events['uni_delta'][t]
        if UNI_delta < 0:
            action['UNI_burn'] = -UNI_delta

    del uniswap_events
    return action

# SUFs

def s_mechanismHub_DAI(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'TokenPurchase':
        return ethToToken_DAI(_params[0], substep, sH, s, _input)
    elif action == 'EthPurchase':
        return tokenToEth_DAI(_params[0], substep, sH, s, _input)
    elif action == 'AddLiquidity':
        return addLiquidity_DAI(_params[0], substep, sH, s, _input)
    elif action == 'Transfer':
        return removeLiquidity_DAI(_params[0], substep, sH, s, _input)
    return('DAI_balance', s['DAI_balance'])
    
def s_mechanismHub_ETH(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'TokenPurchase':
        return ethToToken_ETH(_params[0], substep, sH, s, _input)
    elif action == 'EthPurchase':
        return tokenToEth_ETH(_params[0], substep, sH, s, _input)
    elif action == 'AddLiquidity':
        return addLiquidity_ETH(_params[0], substep, sH, s, _input)
    elif action == 'Transfer':
        return removeLiquidity_ETH(_params[0], substep, sH, s, _input)
    return('ETH_balance', s['ETH_balance'])

def s_mechanismHub_UNI(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'AddLiquidity':
        return addLiquidity_UNI(_params[0], substep, sH, s, _input)
    elif action == 'Transfer':
        return removeLiquidity_UNI(_params[0], substep, sH, s, _input)
    return('UNI_supply', s['UNI_supply'])