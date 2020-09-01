# import networkx as nx
import numpy as np

# from ..utils import *

def p_marketing_rate(params, substep, state_history, prev_state, **kwargs):
    # params = params[0]
    """
    Policy for steady marketing spend signal generation.
    """
    constant = params['MARKETING_STEADY']
    random = np.random.normal(params['MARKETING_STEADY'], scale = 1.0)
    return {'steady_signal': constant}

def p_marketing_shock(params, substep, state_history, prev_state, **kwargs):
    """
    Policy for shock marketing (spend and other sources).
    """
    # Expected number of shocks
    # coded through parameter
    # params = params[0]
    freq = params['MARKETING_SHOCK_FREQ'] * 0.5

    # expected but randomized through poisson
    if np.random.poisson(freq) > params['MARKETING_SHOCK_FREQ']:
        shock = params['MARKETING_SHOCK_MAG']
    else:
        shock = 0
    return {'shock_signal': shock}

def s_signal(params, substep, state_history, prev_state, policy_input, **kwargs):
    """
    State for generating signal from marketing.
    """
    key = 'signal'

    value = policy_input['steady_signal'] + policy_input['shock_signal']
    return (key, value)

    