import numpy as np
import pandas as pd
import copy

def agent_add_liq(params, substep, state_history, prev_state, policy_input):
    """
    This function updates agent local states when liquidity is added in one asset.
    If symmetric liquidity add is enabled additional calculations are made.

    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    agent_id = policy_input['agent_id']
    U_agents =  copy.deepcopy(prev_state['uni_agents'])
    chosen_agent = U_agents[U_agents['m']==agent_id]

    total_liquidity = int(prev_state['UNI_S' + asset_id])
    Q_reserve = int(prev_state['UNI_Q' + asset_id])
    Ri_reserve = int(prev_state['UNI_R' + asset_id])

    ri_deposit = int(policy_input['ri_deposit'])
    liquidity_minted = int(policy_input['ri_deposit'] * total_liquidity // Ri_reserve)

    U_agents.at[agent_id,'r_' + asset_id + '_out'] = chosen_agent['r_' + asset_id + '_out'].values - ri_deposit
    U_agents.at[agent_id,'r_' + asset_id + '_in'] = chosen_agent['r_' + asset_id + '_in'].values + ri_deposit
    U_agents.at[agent_id,'s_' + asset_id] = chosen_agent['s_' + asset_id].values + liquidity_minted

###############################################################
  ################## SYMMETRIC #################
    if params['ENABLE_SYMMETRIC_LIQ']:
        alpha = ri_deposit / prev_state['UNI_R' + asset_id]
        Q_prime = (1 + alpha) * Q_reserve
        q_amount = Q_prime - Q_reserve
        U_agents.at[agent_id,'h'] = chosen_agent['h'].values - q_amount
        U_agents.at[agent_id,'q_' + asset_id] = chosen_agent['q_' + asset_id].values + q_amount
##################### something like this ##############################

    return ('uni_agents', U_agents)  


def agent_remove_liq(params, substep, state_history, prev_state, policy_input):
    """
    This function updates agent states when liquidity is removed in one asset.
    If symmetric liquidity add is enabled additional calculations are made.

    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    agent_id = policy_input['agent_id']
    U_agents =  copy.deepcopy(prev_state['uni_agents'])
    chosen_agent = U_agents[U_agents['m']==agent_id]

    total_liquidity = int(prev_state['UNI_S' + asset_id])
    si_burn = int(policy_input['UNI_burn'])
    Q_reserve = int(prev_state['UNI_Q' + asset_id])
    Ri_reserve = int(prev_state['UNI_R' + asset_id])

    ##### WATCH INTEGERS ###################
    ri_amount = (si_burn * Ri_reserve // total_liquidity)
    q_amount = (si_burn * Q_reserve // total_liquidity)
    # print(ri_amount)

    U_agents.at[agent_id,'r_' + asset_id + '_out'] = chosen_agent['r_' + asset_id + '_out'].values + ri_amount
    U_agents.at[agent_id,'r_' + asset_id + '_in'] = chosen_agent['r_' + asset_id + '_in'].values - ri_amount

    ################## SYMMETRIC #################
    if params['ENABLE_SYMMETRIC_LIQ']:
        U_agents.at[agent_id,'h'] = chosen_agent['h'].values + q_amount
        U_agents.at[agent_id,'q_' + asset_id] = chosen_agent['q_' + asset_id].values - q_amount
    #####################################################

    U_agents.at[agent_id,'s_' + asset_id] = chosen_agent['s_' + asset_id].values - si_burn

    return ('uni_agents', U_agents)  

def getInputPrice(input_amount, input_reserve, output_reserve, params):
    """
    Calculates the input price, considering fees
    """
    fee_numerator = params['fee_numerator']
    fee_denominator = params['fee_denominator']
    input_amount_with_fee = input_amount * fee_numerator
    numerator = input_amount_with_fee * output_reserve
    denominator = (input_reserve * fee_denominator) + input_amount_with_fee
    return int(numerator // denominator)

def agent_q_to_r_trade(params, substep, state_history, prev_state, policy_input):
    """
    This function updates agent states when a 'q to r' trade is performed:
    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    agent_id = policy_input['agent_id']
    U_agents =  copy.deepcopy(prev_state['uni_agents'])
    chosen_agent = U_agents[U_agents['m']==agent_id]
    q_sold = policy_input['q_sold'] #amount of Q being sold by the user
    Q_reserve = prev_state['UNI_Q' + asset_id]
    Ri = prev_state['UNI_R' + asset_id]
    # if q_sold == 0:
    #     return ('UNI_R' + asset_id, Ri)
    # else:
    r_bought = getInputPrice(q_sold, Q_reserve, Ri, params)
    
    U_agents.at[agent_id,'h'] = chosen_agent['h'].values - q_sold
    U_agents.at[agent_id,'r_' + asset_id + '_out'] = chosen_agent['r_' + asset_id + '_out'].values + r_bought

    return ('uni_agents', U_agents)
    
def agent_r_to_q_trade(params, substep, state_history, prev_state, policy_input):
    """
    This function updates agent states when a 'r to q' trade is performed:
    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    agent_id = policy_input['agent_id']
    U_agents =  copy.deepcopy(prev_state['uni_agents'])
    chosen_agent = U_agents[U_agents['m']==agent_id]
    ri = int(policy_input['ri_sold']) #amount of Ri being sold by the user
    Q = int(prev_state['UNI_Q' + asset_id])
    # if r == 0:
    #     # return ('UNI_Q' + asset_id, Q)
    # else:
    Ri = int(prev_state['UNI_R' + asset_id])
    q_bought = int(getInputPrice(ri, Ri, Q, params))
        # return ('UNI_Q' + asset_id, Q - q_bought)

    # print(q_bought)
    U_agents.at[agent_id,'h'] = chosen_agent['h'].values + q_bought

    U_agents.at[agent_id,'r_' + asset_id + '_out'] = chosen_agent['r_' + asset_id + '_out'].values - ri

    return ('uni_agents', U_agents)        

def agent_r_to_r_swap(params, substep, state_history, prev_state, policy_input):
    """
    This function updates agent states when a swap is performed between two assets
    """
    asset_id = policy_input['asset_id'] # defines asset subscript
    purchased_asset_id = policy_input['purchased_asset_id'] # defines asset subscript

    agent_id = policy_input['agent_id']
    U_agents =  prev_state['uni_agents']
    chosen_agent = U_agents[U_agents['m']==agent_id]

    delta_Ri = int(policy_input['ri_sold']) #amount of Ri being sold by the user
    
    if delta_Ri == 0:
        return ('uni_agents', U_agents) 
    
    Q = prev_state['UNI_' + purchased_asset_id + asset_id]
    # if r == 0:
    #     # return ('UNI_Q' + asset_id, Q)
    # else:
    Ri = prev_state['UNI_' + asset_id + purchased_asset_id]
    delta_Rk = getInputPrice(delta_Ri, Ri, Q, params)
  
    U_agents.at[agent_id,'r_' + asset_id + '_out'] = chosen_agent['r_' + asset_id + '_out'] - delta_Ri
    U_agents.at[agent_id,'r_' + purchased_asset_id + '_out'] = chosen_agent['r_' + purchased_asset_id + '_out'] + delta_Rk


    return ('uni_agents', U_agents) 