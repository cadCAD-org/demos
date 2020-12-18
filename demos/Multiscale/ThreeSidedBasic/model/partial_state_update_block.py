from .parts.exogenous import *
from .parts.flows import *
from .parts.investors import *
from .parts.kpis import *


# The Partial State Update Blocks
partial_state_update_blocks = [
    # exogenous.py:
    {
        'policies':
        {
        },
        'variables':
        {
            'tx_volume': tx_volume_generator,
            'product_cost': product_cost_generator,
            'seed_money': investors_generator,
            'overhead_cost': update_overhead_costs,
            'R&D': R_and_D
        }

    },
    # flows.py:
    {
        'policies':
        {
            'action': inflow
        },
        'variables':
        {
            'fiat_reserve': receive_fiat_from_consumers,
            'revenue': receive_revenue_from_consumers
        }
    },

    #investors.py:
    {
        'policies':
        {
            'action': investors
        },
        'variables':
        {
            'seed_money': receive_fiat_from_investors
        }
    },
    #flows.py:
    {
        'policies':
        {
            'action': outflow
        },
        'variables':
        {
            'fiat_reserve': pay_fiat_to_producers,
            'fiat_reserve': pay_investment_expenses,
            'fiat_reserve': pay_overhead_costs
        }
    },
    #kpis.py:
    {
        'policies':
        {
            'action': kpis
        },
        'variables':
        {
            'COGS': COGS
        }
    },

]

            
 