from .parts.get_r0_model import *


partial_state_update_block = [
    {
        'policies': {
            'recovering_rate_estimation': p_recovering_rate_estimation,
            'infection_rate_estimation': p_infection_rate_estimation
        },
        'variables': {
            'r0': s_r0_estimation   
        }
    }

]