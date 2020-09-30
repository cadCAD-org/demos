from .policy_aux import get_trade_decision
from .suf_aux import *

# Policy

def p_actionDecoder(_params, substep, sH, s):
    uniswap_events = _params['uniswap_events']
    
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

    if event == 'TokenPurchase':
        I_t = s['ETH_balance']
        O_t = s['DAI_balance']
        I_t1 = uniswap_events['eth_balance'][t]
        O_t1 = uniswap_events['token_balance'][t]
        delta_I = uniswap_events['eth_delta'][t]
        delta_O = uniswap_events['token_delta'][t]
        action['eth_sold'] = get_trade_decision(delta_I, delta_O, I_t, O_t, I_t1, O_t1, _params)
    elif event == 'EthPurchase':
        I_t = s['DAI_balance']
        O_t = s['ETH_balance']
        I_t1 = uniswap_events['token_balance'][t]
        O_t1 = uniswap_events['eth_balance'][t]
        delta_I = uniswap_events['token_delta'][t]
        delta_O = uniswap_events['eth_delta'][t]
        action['tokens_sold'] = get_trade_decision(delta_I, delta_O, I_t, O_t, I_t1, O_t1, _params)
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
        return ethToToken_DAI(_params, substep, sH, s, _input)
    elif action == 'EthPurchase':
        return tokenToEth_DAI(_params, substep, sH, s, _input)
    elif action == 'AddLiquidity':
        return addLiquidity_DAI(_params, substep, sH, s, _input)
    elif action == 'Transfer':
        return removeLiquidity_DAI(_params, substep, sH, s, _input)
    return('DAI_balance', s['DAI_balance'])
    
def s_mechanismHub_ETH(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'TokenPurchase':
        return ethToToken_ETH(_params, substep, sH, s, _input)
    elif action == 'EthPurchase':
        return tokenToEth_ETH(_params, substep, sH, s, _input)
    elif action == 'AddLiquidity':
        return addLiquidity_ETH(_params, substep, sH, s, _input)
    elif action == 'Transfer':
        return removeLiquidity_ETH(_params, substep, sH, s, _input)
    return('ETH_balance', s['ETH_balance'])

def s_mechanismHub_UNI(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'AddLiquidity':
        return addLiquidity_UNI(_params, substep, sH, s, _input)
    elif action == 'Transfer':
        return removeLiquidity_UNI(_params, substep, sH, s, _input)
    return('UNI_supply', s['UNI_supply'])