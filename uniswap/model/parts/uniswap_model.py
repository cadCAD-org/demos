from math import sqrt

# Policies

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

def s_addLiquidity_UNI(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    eth_reserve = int(s['ETH_balance'])
    liquidity_minted = int(_input['eth_deposit'] * total_liquidity // eth_reserve)
    return ('UNI_supply', total_liquidity + liquidity_minted)

def s_addLiquidity_ETH(_params, substep, sH, s, _input):
    eth_reserve = int(s['ETH_balance'])
    return ('ETH_balance', eth_reserve + _input['eth_deposit'])

def s_addLiquidity_DAI(_params, substep, sH, s, _input):
    eth_reserve = int(s['ETH_balance'])
    token_reserve = int(s['DAI_balance'])
    if _input['eth_deposit'] == 0:
        token_amount = 0
    else:
        token_amount = int(_input['eth_deposit'] * token_reserve // eth_reserve + 1)
    return ('DAI_balance', token_reserve + token_amount)

def s_removeLiquidity_UNI(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    amount = int(_input['UNI_burn'])
    return ('UNI_supply', int(total_liquidity - amount))

def s_removeLiquidity_ETH(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    eth_reserve = int(s['ETH_balance'])
    amount = int(_input['UNI_burn'])
    eth_amount = int(amount * eth_reserve // total_liquidity)
    return ('ETH_balance', int(eth_reserve - eth_amount))

def s_removeLiquidity_DAI(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    token_reserve = int(s['DAI_balance'])
    amount = int(_input['UNI_burn'])
    token_amount = int(amount * token_reserve // total_liquidity)
    return ('DAI_balance', int(token_reserve - token_amount))

def s_ethToToken_ETH(_params, substep, history, s, _input):
    delta_I = int(_input['eth_sold']) #amount of ETH being sold by the user
    I_t = int(s['ETH_balance'])
    return ('ETH_balance', I_t + delta_I)

def s_ethToToken_DAI(_params, substep, sH, s, _input):
    delta_I = int(_input['eth_sold']) #amount of ETH being sold by the user
    I_t = int(s['ETH_balance'])
    O_t = int(s['DAI_balance'])
    if delta_I == 0:
        return ('DAI_balance', O_t)
    else:
        delta_O = int(get_input_price(delta_I, I_t, O_t, _params))
        return ('DAI_balance', O_t - delta_O)

def s_tokenToEth_ETH(_params, substep, sH, s, _input):
    delta_I = int(_input['tokens_sold']) #amount of tokens being sold by the user
    O_t = int(s['ETH_balance'])
    I_t = int(s['DAI_balance'])
    if delta_I == 0:
        return ('ETH_balance', O_t)
    else:
        delta_O = int(get_input_price(delta_I, I_t, O_t, _params))
        return ('ETH_balance', O_t - delta_O)
    
def s_tokenToEth_DAI(_params, substep, sH, s, _input):
    delta_I = int(_input['tokens_sold']) #amount of tokens being sold by the user
    I_t = int(s['DAI_balance'])
    return ('DAI_balance', I_t + delta_I)

def s_mechanismHub_DAI(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'TokenPurchase':
        return s_ethToToken_DAI(_params, substep, sH, s, _input)
    elif action == 'EthPurchase':
        return s_tokenToEth_DAI(_params, substep, sH, s, _input)
    elif action == 'AddLiquidity':
        return s_addLiquidity_DAI(_params, substep, sH, s, _input)
    elif action == 'Transfer':
        return s_removeLiquidity_DAI(_params, substep, sH, s, _input)
    return('DAI_balance', s['DAI_balance'])
    
def s_mechanismHub_ETH(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'TokenPurchase':
        return s_ethToToken_ETH(_params, substep, sH, s, _input)
    elif action == 'EthPurchase':
        return s_tokenToEth_ETH(_params, substep, sH, s, _input)
    elif action == 'AddLiquidity':
        return s_addLiquidity_ETH(_params, substep, sH, s, _input)
    elif action == 'Transfer':
        return s_removeLiquidity_ETH(_params, substep, sH, s, _input)
    return('ETH_balance', s['ETH_balance'])

def s_mechanismHub_UNI(_params, substep, sH, s, _input):
    action = _input['action_id']
    if action == 'AddLiquidity':
        return s_addLiquidity_UNI(_params, substep, sH, s, _input)
    elif action == 'Transfer':
        return s_removeLiquidity_UNI(_params, substep, sH, s, _input)
    return('UNI_supply', s['UNI_supply'])

# AUX

def get_input_price(delta_I, I_t, O_t, _params):
    fee_numerator = _params['fee_numerator']
    fee_denominator = _params['fee_denominator']
    delta_I_with_fee = delta_I * fee_numerator
    numerator = delta_I_with_fee * O_t
    denominator = (I_t * fee_denominator) + delta_I_with_fee
    return int(numerator // denominator)

def classifier(delta_I, delta_O, c_rule):
    if (delta_I / (10 ** (18-c_rule))).is_integer() or (delta_O / (10 ** (18-c_rule))).is_integer() :
      return "Conv"
    else:
      return "Arb"

def get_trade_decision(delta_I, delta_O, I_t, O_t, I_t1, O_t1, _params):
    if classifier(delta_I, delta_O, _params['c_rule']) == 'Conv':
        calculated_delta_O = int(get_input_price(delta_I, I_t, O_t, _params))
        historic_delta_O = int(get_input_price(delta_I, I_t1, O_t1, _params))
        if calculated_delta_O >= historic_delta_O * (1 - _params['conv_tolerance']):
            return delta_I
        else:
            return 0
    else:
        P = (I_t + delta_I) / (O_t + delta_O)
        delta_I = get_delta_I(P, I_t, O_t, _params)

        return delta_I

def get_delta_I(P, I_t, O_t, _params):
    a = _params['fee_numerator']
    b = _params['fee_denominator']
    delta_I = (
        (-(I_t*b + I_t*a)) + sqrt(
            ((I_t*b - I_t*a)**2) + (4*P*O_t*I_t*a*b)
        )
    )  / (2*a)

    return int(delta_I)
