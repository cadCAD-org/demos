from .parts.marketing_signal import *
from .parts.adoption import *

partial_state_update_block = [
    {
        # marketing_signal.py
        'policies': {
            'marketing_rate': p_marketing_rate,
            'p_marketing_shock' : p_marketing_shock,
        },
        'variables': {
            'signal': s_signal,
        }
    },
    {
        # adoption.py
        'policies': {
            'reputation' : p_reputation,
            'experience' : p_experience,
        },
        'variables': {
            'pool': s_pool,  

        }
    },

]