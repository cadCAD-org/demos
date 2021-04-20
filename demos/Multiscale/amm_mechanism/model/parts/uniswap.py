import numpy as np
import pandas as pd
from .utils import *
from .agent_utils import *

# Mechanisms
def mechanismHub_Ri(params, substep, state_history, prev_state, policy_input):
    """
This function returns the approprate pool function to a given policy input:
- Ri_Purchase --> q_to_r_Ri
- Q_Purchase --> r_to_q_Ri
- AddLiquidity --> addLiquidity_Ri
- RemoveLiquidity --> removeLiquidity_Ri
    """
    action = policy_input['action_id']
    asset_id = policy_input['asset_id'] # defines asset subscript
    if action == 'Ri_Purchase':
        return q_to_r_Ri(params, substep, state_history, prev_state, policy_input)
    elif action == 'Q_Purchase':
        return r_to_q_Ri(params, substep, state_history, prev_state, policy_input)
    elif action == 'AddLiquidity':
        return addLiquidity_Ri(params, substep, state_history, prev_state, policy_input)
    elif action == 'RemoveLiquidity':
        return removeLiquidity_Ri(params, substep, state_history, prev_state, policy_input)
    return('UNI_R' + asset_id, prev_state['UNI_R' + asset_id])
    
def mechanismHub_Q(params, substep, state_history, prev_state, policy_input):
    """
This function returns the approprate pool function to a given policy input:
- Ri_Purchase --> q_to_r_Q
- Q_Purchase --> r_to_q_Q
- AddLiquidity --> addLiquidity_Q
- RemoveLiquidity --> removeLiquidity_Q

    """
    action = policy_input['action_id']
    asset_id = policy_input['asset_id'] # defines asset subscript
    
    if action == 'Ri_Purchase':
        return q_to_r_Q(params, substep, state_history, prev_state, policy_input)
    elif action == 'Q_Purchase':
        return r_to_q_Q(params, substep, state_history, prev_state, policy_input)
    elif action == 'AddLiquidity':
        return addLiquidity_Q(params, substep, state_history, prev_state, policy_input)
    elif action == 'RemoveLiquidity':
        return removeLiquidity_Q(params, substep, state_history, prev_state, policy_input)
    return('UNI_Q'+ asset_id, prev_state['UNI_Q'+ asset_id])

def mechanismHub_Si(params, substep, state_history, prev_state, policy_input):
    """
This function returns the approprate pool function to a given policy input:
- AddLiquidity --> addLiquidity_Si
- RemoveLiquidity --> removeLiquidity_Si

    """
    action = policy_input['action_id']
    asset_id = policy_input['asset_id'] # defines asset subscript

    if action == 'AddLiquidity':
        return addLiquidity_Si(params, substep, state_history, prev_state, policy_input)
    elif action == 'RemoveLiquidity':
        return removeLiquidity_Si(params, substep, state_history, prev_state, policy_input)
    return('UNI_S'+ asset_id, prev_state['UNI_S'+ asset_id])

def agenthub(params, substep, state_history, prev_state, policy_input):
    """
This function returns the approprate agent function to a given policy input:
- Ri_Purchase --> agent_q_to_r_trade
- Q_Purchase --> agent_r_to_q_trade
- AddLiquidity --> agent_add_liq
- RemoveLiquidity --> agent_remove_liq
- R_Swap --> agent_r_to_r_swap
    """
    action = policy_input['action_id']
    if action == 'Ri_Purchase':
        return agent_q_to_r_trade(params, substep, state_history, prev_state, policy_input)
    elif action == 'Q_Purchase':
        return agent_r_to_q_trade(params, substep, state_history, prev_state, policy_input)
    elif action == 'AddLiquidity':
        return agent_add_liq(params, substep, state_history, prev_state, policy_input)
    elif action == 'RemoveLiquidity':
        return agent_remove_liq(params, substep, state_history, prev_state, policy_input)
    elif action == 'R_Swap':
        return agent_r_to_r_swap(params, substep, state_history, prev_state, policy_input)
    return('uni_agents', prev_state['uni_agents'])

def mechanismHub_ij(params, substep, state_history, prev_state, policy_input):
    """
This function returns the approprate pool function to a given policy input depending on the 'direction':
- R_Swap --> agent_r_to_r_in
- R_Swap --> agent_r_to_r_out
    """
    action = policy_input['action_id']
    if action == 'R_Swap':
        
        asset_id = policy_input['asset_id']
        purchased_asset_id = policy_input['purchased_asset_id']
        # direction = policy_input['direction']
        direction = asset_id + purchased_asset_id
        in_direction = 'ij'
        out_direction = in_direction[::-1]
        if direction == in_direction:

            return r_to_r_in(params, substep, state_history, prev_state, policy_input)
        elif direction == out_direction:

            return r_to_r_out(params, substep, state_history, prev_state, policy_input)
    # return('UNI_' + asset_id + purchased_asset_id, prev_state['UNI_' + asset_id + purchased_asset_id])
    return('UNI_ij', prev_state['UNI_ij'])

def mechanismHub_ji(params, substep, state_history, prev_state, policy_input):
    """
This function returns the approprate pool function to a given policy input depending on the 'direction':
- R_Swap --> agent_r_to_r_in
- R_Swap --> agent_r_to_r_out
    """
    action = policy_input['action_id']
    if action == 'R_Swap':
        
        asset_id = policy_input['asset_id']
        purchased_asset_id = policy_input['purchased_asset_id']
        # direction = policy_input['direction']
        direction = asset_id + purchased_asset_id
        in_direction = 'ji'
        out_direction = in_direction[::-1]
        if direction == in_direction:

            return r_to_r_in(params, substep, state_history, prev_state, policy_input)
        elif direction == out_direction:

            return r_to_r_out(params, substep, state_history, prev_state, policy_input)
    # return('UNI_' + asset_id + purchased_asset_id, prev_state['UNI_' + asset_id + purchased_asset_id])
    return('UNI_ji', prev_state['UNI_ji'])