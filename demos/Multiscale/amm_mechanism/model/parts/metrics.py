from .utils import *

def s_swap_price_i(params, substep, state_history, prev_state, policy_input):
    """
    Calculates and returns the swap price for a trade Qi for Ri
    """
    Q_reserve = int(prev_state['UNI_Qi'])
    R_reserve = int(prev_state['UNI_Ri'])

    # input 1000 q token get r
    delta_q = 1000
    delta_r = getInputPrice(delta_q, Q_reserve, R_reserve, params)
   
    return ('UNI_P_RQi', delta_q/delta_r)

def s_swap_price_j(params, substep, state_history, prev_state, policy_input):
    """
    Calculates and returns the swap price for a trade Qj for Rj
    """
    Q_reserve = int(prev_state['UNI_Qj'])
    R_reserve = int(prev_state['UNI_Rj'])

    # input 1000 q token get r
    delta_q = 1000
    delta_r = getInputPrice(delta_q, Q_reserve, R_reserve, params)
   
    return ('UNI_P_RQj', delta_q/delta_r)

def s_swap_price_ij(params, substep, state_history, prev_state, policy_input):
    """
    Calculates and returns the swap price for a trade Ri for Rj
    """
    Q_reserve = int(prev_state['UNI_ij'])
    R_reserve = int(prev_state['UNI_ji'])

    # input 1000 q token get r
    delta_q = 1000
    delta_r = getInputPrice(delta_q, Q_reserve, R_reserve, params)
   
    return ('UNI_P_ij', delta_q/delta_r)