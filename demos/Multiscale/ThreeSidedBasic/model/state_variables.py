from .parts.sys_params import *

# Initial States
state_variables = { 
            'tx_volume': initial_values['tx_volume'], #unit: fiat
            'product_cost': initial_values['product_cost'], #unit: fiat cost
            'revenue': initial_values['revenue'], # revenue per month
            'fiat_reserve': initial_values['fiat_reserve'],#unit: fiat
            'overhead_cost': initial_values['overhead_cost'], #unit: fiat per month
            'seed_money': initial_values['seed_money'],
            'R&D': initial_values['R&D'], #per month
            'COGS': initial_values['COGS'] #per month
}

