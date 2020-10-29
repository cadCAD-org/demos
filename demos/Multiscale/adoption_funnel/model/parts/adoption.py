import numpy as np

# Behaviors
def p_reputation(params, substep, state_history, prev_state, **kwargs):
    """
    Policy for steady marketing spend signal generation.
    """
    constant = params['THRESHOLD']
    random = np.random.normal(params['THRESHOLD'], scale = 1.0)
    return {'reputation': constant}


def p_experience(params, substep, state_history, prev_state, **kwargs):
    """
    Policy for steady marketing spend signal generation.
    """
    constant = params['EXO_EXPERIENCE']
    random = np.random.normal(params['EXO_EXPERIENCE'], scale = 1.0)
    return {'experience': constant}


# Mechanisms
def s_adoption(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'adoption'
 
    prev_state['adoption'].apply_signal(prev_state['signal'])
    prev_state['adoption'].set_threshold(params['THRESHOLD'])
    prev_state['adoption'].determine_state(prev_state['signal'])
    value = prev_state['adoption']
    return (key, value)

def s_pool(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'pool'
    
    prev_state['pool'].apply_signal(prev_state['signal'])
    prev_state['pool'].set_threshold(ext_threshold=params['THRESHOLD'])
    prev_state['pool'].calculate_drip(params['LEAK_COEFFICIENT'])
    prev_state['pool'].update_pools(params['LEAK_COEFFICIENT'])
    value = prev_state['pool']
    return (key, value)