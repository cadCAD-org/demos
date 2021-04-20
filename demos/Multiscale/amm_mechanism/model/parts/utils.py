import numpy as np

def addLiquidity_Si(params, substep, state_history, prev_state, policy_input):
    """
    For adding liquidity this function returns the amount of shares UNI_S for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    total_liquidity = int(prev_state['UNI_S' + asset_id])
    Ri_reserve = int(prev_state['UNI_R' + asset_id])
    liquidity_minted = int(policy_input['ri_deposit'] * total_liquidity // Ri_reserve)
    return ('UNI_S' + asset_id, total_liquidity + liquidity_minted)

def addLiquidity_Q(params, substep, state_history, prev_state, policy_input):
    """
    For adding liquidity this function returns the amount of token UNI_Q for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    Q_reserve = int(prev_state['UNI_Q' + asset_id])
    Ri_reserve = int(prev_state['UNI_R' + asset_id])
    if policy_input['ri_deposit'] == 0:
        token_amount = 0
    else:
        token_amount = int(policy_input['ri_deposit'] * Q_reserve // Ri_reserve + 1)
    # ASSUME SYMMETRIC LIQUIDITY
    if params['ENABLE_SYMMETRIC_LIQ']: 
        return ('UNI_Q' + asset_id, Q_reserve + token_amount)
    # ASSUME ASSYMMETRIC LIQUIDITY
    else:
        return ('UNI_Q' + asset_id, Q_reserve)

def addLiquidity_Ri(params, substep, state_history, prev_state, policy_input):
    """
    For adding liquidity this function returns the amount of token UNI_R for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    Ri_reserve = int(prev_state['UNI_R' + asset_id])
    if policy_input['ri_deposit'] == 0:
        token_amount = 0
    else:
        token_amount = int(policy_input['ri_deposit'])
  
    return ('UNI_R' + asset_id, Ri_reserve + token_amount)

def removeLiquidity_Si(params, substep, state_history, prev_state, policy_input):
    """
    For removing liquidity this function returns the amount of shares UNI_S for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    total_liquidity = int(prev_state['UNI_S' + asset_id])
    amount = int(policy_input['UNI_burn'])
    return ('UNI_S' + asset_id, int(total_liquidity - amount))

def removeLiquidity_Q(params, substep, state_history, prev_state, policy_input):
    """
    For removing liquidity this function returns the amount of token UNI_Q for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    total_liquidity = int(prev_state['UNI_S' + asset_id])
    Q_reserve = int(prev_state['UNI_Q' + asset_id])
    amount = int(policy_input['UNI_burn'])
    q_amount = int(amount * Q_reserve // total_liquidity)
    # ASSUME SYMMETRIC LIQUIDITY
    # return ('UNI_Q' + asset_id, int(Q_reserve - q_amount))
     # ASSUME ASSYMMETRIC LIQUIDITY  
    if params['ENABLE_SYMMETRIC_LIQ']: 
        return ('UNI_Q' + asset_id, int(Q_reserve - q_amount))
    else:
        return ('UNI_Q' + asset_id, Q_reserve)

def removeLiquidity_Ri(params, substep, state_history, prev_state, policy_input):
    """
    For removing liquidity this function returns the amount of token UNI_R for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    total_liquidity = int(prev_state['UNI_S' + asset_id])
    Q_reserve = int(prev_state['UNI_R' + asset_id])
    amount = int(policy_input['UNI_burn'])
    q_amount = int(amount * Q_reserve // total_liquidity)
    return ('UNI_R' + asset_id, int(Q_reserve - q_amount))


def getInputPrice(input_amount, input_reserve, output_reserve, params):
    fee_numerator = params['fee_numerator']
    fee_denominator = params['fee_denominator']
    input_amount_with_fee = input_amount * fee_numerator
    numerator = input_amount_with_fee * output_reserve
    denominator = (input_reserve * fee_denominator) + input_amount_with_fee
    return (numerator // denominator)

def q_to_r_Q(params, substep, state_history, prev_state, policy_input):
    """
    For a 'q to r' trade this function returns the amount of token UNI_Q for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    q_sold = int(policy_input['q_sold']) #amount of Q being sold by the user
    Q_reserve = int(prev_state['UNI_Q' + asset_id])
    return ('UNI_Q' + asset_id, Q_reserve + q_sold)

def q_to_r_Ri(params, substep, state_history, prev_state, policy_input):
    """
    For a 'q to r' trade this function returns the amount of token UNI_R for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    q_sold = int(policy_input['q_sold']) #amount of Q being sold by the user
    Q_reserve = int(prev_state['UNI_Q' + asset_id])
    Ri = int(prev_state['UNI_R' + asset_id])
    if q_sold == 0:
        return ('UNI_R' + asset_id, Ri)
    else:
        r_bought = int(getInputPrice(q_sold, Q_reserve, Ri, params))
        return ('UNI_R' + asset_id, Ri - r_bought)
    
def r_to_q_Q(params, substep, state_history, prev_state, policy_input):
    """
    For a 'r to q' trade this function returns the amount of token UNI_Q for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript

    r = int(policy_input['ri_sold']) #amount of Ri being sold by the user
    Q = int(prev_state['UNI_Q' + asset_id])
    if r == 0:
        return ('UNI_Q' + asset_id, Q)
    else:
        Ri = int(prev_state['UNI_R' + asset_id])
        q_bought = int(getInputPrice(r, Ri, Q, params))
        return ('UNI_Q' + asset_id, Q - q_bought)
    
def r_to_q_Ri(params, substep, state_history, prev_state, policy_input):
    """
    For a 'r to q' trade this function returns the amount of token UNI_R for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    r = int(policy_input['ri_sold']) #amount of Ri being sold by the user
    Ri = int(prev_state['UNI_R' + asset_id])
    return ('UNI_R' + asset_id, r + Ri)

def r_to_r_in(params, substep, state_history, prev_state, policy_input):
    """
    For a 'r to r' trade between two assets this function returns the amount of token UNI_Rx for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    purchased_asset_id = policy_input['purchased_asset_id'] # defines asset subscript

    delta_Ri = int(policy_input['ri_sold']) #amount of Ri being sold by the user
    
    if delta_Ri == 0:
        return ('UNI_' + asset_id + purchased_asset_id, prev_state['UNI_' + asset_id + purchased_asset_id])
    
    Rk = prev_state['UNI_' + purchased_asset_id + asset_id]
    # if r == 0:
    #     # return ('UNI_Q' + asset_id, Q)
    # else:
    Ri = prev_state['UNI_' + asset_id + purchased_asset_id]
    delta_Rk = getInputPrice(delta_Ri, Ri, Rk, params)

    return ('UNI_' + asset_id + purchased_asset_id, Ri + delta_Ri)
    
def r_to_r_out(params, substep, state_history, prev_state, policy_input):
    """
    For a 'r to r' trade between two assets this function returns the amount of token UNI_Rx for the respective asset depending on the policy_input
    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    purchased_asset_id = policy_input['purchased_asset_id'] # defines asset subscript

    delta_Ri = int(policy_input['ri_sold']) #amount of Ri being sold by the user
    
    if delta_Ri == 0:
        # return ('UNI_' + asset_id + purchased_asset_id, prev_state['UNI_' + asset_id + purchased_asset_id])
        return ('UNI_' + asset_id + purchased_asset_id, prev_state['UNI_' + asset_id + purchased_asset_id])
    
    Rk = prev_state['UNI_' + purchased_asset_id + asset_id]
    # if r == 0:
    #     # return ('UNI_Q' + asset_id, Q)
    # else:
    Ri = prev_state['UNI_' + asset_id + purchased_asset_id]
    delta_Rk = getInputPrice(delta_Ri, Ri, Rk, params)
    Rk = prev_state['UNI_' + purchased_asset_id + asset_id]
    return ('UNI_' + purchased_asset_id + asset_id, Rk - delta_Rk)