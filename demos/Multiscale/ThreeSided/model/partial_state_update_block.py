from .parts.exogenous import *
from .parts.producers import *
from .parts.providers import *
from .parts.consumers import *
from .parts.investors import *
from .parts.governance import *
from .parts.system import *


# The Partial State Update Blocks
partial_state_update_blocks = [
    # exogenous.py:
    {
        'policies':
        {
        },
        'variables':
        {
            'cost_of_production': cost_of_production_generator,
            'tx_volume': tx_volume_generator,
            'overhead_cost': overhead_cost_generator
        }

    },

    # producers.py:
    {
        'policies':
        {
            'action': producer_choice
        },
        'variables':
        {
            'volume_of_production': commit_delta_production        
        }
    },

    # consumers.py:
    {
        'policies':
        {
            'action': consumer_choice
        },
        'variables':
        {
            'fiat_reserve': capture_consumer_payments1,
            'token_reserve': capture_consumer_payments2
        }
    },
    # providers.py:
    {
        'policies':
        {
            'action': provider_choice
        },
        'variables':
        {
            'fiat_reserve': compensate_providers1,
            'token_reserve': compensate_providers2
        }
    },
    # producers.py:
    {
        'policies':
        {
            'action': producer_compensation_policy
        },
        'variables':
        {
            'token_reserve': compensate_production,
            'producer_roi_estimate': update_producer_roi_estimate
        }
    },

    # governance.py:
    {
        'policies':
        {
            'action': budgeting_policy
        },
        'variables':
        {
            'fiat_reserve': release_funds,
            'operational_budget': update_budget
        }
    },

    # governance.py:
    {
        'policies':
        {
            'action': minting_policy
        },
        'variables':
        {
            'token_reserve': mint1,
            'token_supply': mint2
        }
    },

    # system.py:
    {
        'policies':
        {
        },
        'variables':
        {
            'smooth_avg_fiat_reserve': update_smooth_avg_fiat_reserve,
            'smooth_avg_token_reserve':update_smooth_avg_token_reserve
        }
    },

    # governance.py:
    {
        'policies':
        {
            'action': conversion_policy
        },
        'variables':
        {
            'conversion_rate': update_conversion_rate
        }
    }
]

            
 

        