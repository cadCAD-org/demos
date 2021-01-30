# %%
import numpy as np
from .utils import *


# Behaviors
def grow_food(params, substep, state_history, prev_state):
    """
    Increases the food supply in all sites, subject to an maximum.
    """
    t = prev_state['timestep']

    regenerated_sites = calculate_increment(prev_state['sites'],
                                            params['food_growth_rate'],
                                            params['maximum_food_per_site'],
                                            t)

    if np.random.rand() < 0.02:
        disaster_factor = (0.6 + 0.1 * np.random.random()) # (between 60% and 90%)
        disaster_effect = (disaster_factor * regenerated_sites).astype(int)
        regenerated_sites -= disaster_effect
    return {'update_food': regenerated_sites}


# Mechanisms
def update_food(params, substep, state_history, prev_state, policy_input):
    key = 'sites'
    value = policy_input['update_food']
    return (key, value)

# %%

# %%
