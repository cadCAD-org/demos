# Policies

def p_actionDecoder(params, substep, state_history, prev_state):
    
    prev_timestep = prev_state['timestep']
    if substep > 1:
        prev_timestep -= 1
        
    #skip the first two events, as they are already accounted for in the initial conditions of the system
    data_counter = prev_timestep + 2 
    
    action = {
        'eth_sold': 0,
        'tokens_sold': 0,
        'eth_deposit': 0,
        'UNI_burn': 0,        
    }
    
    event = uniswap_events['event'][data_counter]
    
    action['action_id'] = event
    
    if event == 'TokenPurchase':
        action['eth_sold'] = uniswap_events['eth_delta'][data_counter]
    elif event == 'EthPurchase':
        action['tokens_sold'] = uniswap_events['token_delta'][data_counter]
    elif event == 'AddLiquidity':
        action['eth_deposit'] = uniswap_events['eth_delta'][data_counter]
    elif event == 'Transfer':
        UNI_delta = uniswap_events['uni_delta'][data_counter]
        if UNI_delta < 0:
            action['UNI_burn'] = -UNI_delta

    return action

# SUFs

def s_addLiquidity_UNI(params, substep, state_history, prev_state, policy_input):
    total_liquidity = int(prev_state['UNI_supply'])
    eth_reserve = int(prev_state['ETH_balance'])
    liquidity_minted = int(policy_input['eth_deposit'] * total_liquidity // eth_reserve)
    return ('UNI_supply', total_liquidity + liquidity_minted)

def s_addLiquidity_ETH(params, substep, state_history, prev_state, policy_input):
    eth_reserve = int(prev_state['ETH_balance'])
    return ('ETH_balance', eth_reserve + policy_input['eth_deposit'])

def s_addLiquidity_DAI(params, substep, state_history, prev_state, policy_input):
    eth_reserve = int(prev_state['ETH_balance'])
    token_reserve = int(prev_state['DAI_balance'])
    if policy_input['eth_deposit'] == 0:
        token_amount = 0
    else:
        token_amount = int(policy_input['eth_deposit'] * token_reserve // eth_reserve + 1)
    return ('DAI_balance', token_reserve + token_amount)

def s_removeLiquidity_UNI(params, substep, state_history, prev_state, policy_input):
    total_liquidity = int(prev_state['UNI_supply'])
    amount = int(policy_input['UNI_burn'])
    return ('UNI_supply', int(total_liquidity - amount))

def s_removeLiquidity_ETH(params, substep, state_history, prev_state, policy_input):
    total_liquidity = int(prev_state['UNI_supply'])
    eth_reserve = int(prev_state['ETH_balance'])
    amount = int(policy_input['UNI_burn'])
    eth_amount = int(amount * eth_reserve // total_liquidity)
    return ('ETH_balance', int(eth_reserve - eth_amount))

def s_removeLiquidity_DAI(params, substep, state_history, prev_state, policy_input):
    total_liquidity = int(prev_state['UNI_supply'])
    token_reserve = int(prev_state['DAI_balance'])
    amount = int(policy_input['UNI_burn'])
    token_amount = int(amount * token_reserve // total_liquidity)
    return ('DAI_balance', int(token_reserve - token_amount))

def s_ethToToken_ETH(params, substep, history, prev_state, policy_input):
    eth_sold = int(policy_input['eth_sold']) #amount of ETH being sold by the user
    eth_reserve = int(prev_state['ETH_balance'])
    return ('ETH_balance', eth_reserve + eth_sold)

def s_ethToToken_DAI(params, substep, state_history, prev_state, policy_input):
    eth_sold = int(policy_input['eth_sold']) #amount of ETH being sold by the user
    eth_reserve = int(prev_state['ETH_balance'])
    token_reserve = int(prev_state['DAI_balance'])
    if eth_sold == 0:
        return ('DAI_balance', token_reserve)
    else:
        tokens_bought = int(getInputPrice(eth_sold, eth_reserve, token_reserve, params))
        return ('DAI_balance', token_reserve - tokens_bought)

def s_tokenToEth_ETH(params, substep, state_history, prev_state, policy_input):
    tokens_sold = int(policy_input['tokens_sold']) #amount of tokens being sold by the user
    eth_reserve = int(prev_state['ETH_balance'])
    if tokens_sold == 0:
        return ('ETH_balance', eth_reserve)
    else:
        token_reserve = int(prev_state['DAI_balance'])
        eth_bought = int(getInputPrice(tokens_sold, token_reserve, eth_reserve, params))
        return ('ETH_balance', eth_reserve - eth_bought)
    
def s_tokenToEth_DAI(params, substep, state_history, prev_state, policy_input):
    tokens_sold = int(policy_input['tokens_sold']) #amount of tokens being sold by the user
    token_reserve = int(prev_state['DAI_balance'])
    return ('DAI_balance', token_reserve + tokens_sold)

def s_mechanismHub_DAI(params, substep, state_history, prev_state, policy_input):
    action = input_['action_id']
    if action == 'TokenPurchase':
        return s_ethToToken_DAI(params, substep, state_history, prev_state, input_)
    elif action == 'EthPurchase':
        return tokenToEth_DAI(params, substep, state_history, prev_state, input_)
    elif action == 'AddLiquidity':
        return s_addLiquidity_DAI(params, substep, state_history, prev_state, input_)
    elif action == 'Transfer':
        return s_removeLiquidity_DAI(params, substep, state_history, prev_state, input_)
    return('DAI_balance', prev_state['DAI_balance'])
    
def s_mechanismHub_ETH(params, substep, state_history, prev_state, input_):
    action = input_['action_id']
    if action == 'TokenPurchase':
        return s_ethToToken_ETH(params, substep, state_history, prev_state, input_)
    elif action == 'EthPurchase':
        return tokenToEth_ETH(params, substep, state_history, prev_state, input_)
    elif action == 'AddLiquidity':
        return s_addLiquidity_ETH(params, substep, state_history, prev_state, input_)
    elif action == 'Transfer':
        return s_removeLiquidity_ETH(params, substep, state_history, prev_state, input_)
    return('ETH_balance', prev_state['ETH_balance'])

def s_mechanismHub_UNI(params, substep, state_history, prev_state, input_):
    action = input_['action_id']
    if action == 'AddLiquidity':
        return s_addLiquidity_UNI(params, substep, state_history, prev_state, input_)
    elif action == 'Transfer':
        return s_removeLiquidity_UNI(params, substep, state_history, prev_state, input_)
    return('UNI_supply', prev_state['UNI_supply'])


# AUX

def getInputPrice(input_amount, input_reserve, output_reserve, params):
    fee_numerator = params['fee_numerator']
    fee_denominator = params['fee_denominator']
    input_amount_with_fee = input_amount * fee_numerator
    numerator = input_amount_with_fee * output_reserve
    denominator = (input_reserve * fee_denominator) + input_amount_with_fee
    return int(numerator // denominator)