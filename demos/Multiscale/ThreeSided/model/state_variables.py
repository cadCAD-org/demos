from .parts.sys_params import *

# Initial States
state_variables = { 
            'fiat_reserve': initial_values['fiat_reserve'],#unit: fiat
            'overhead_cost': initial_values['overhead_cost'], #unit: fiat
            'operational_budget': initial_values['operational_budget'], #unit: fiat
            'token_reserve': initial_values['token_reserve'],#unit: tok
            'token_supply': initial_values['token_supply'],#unit: tok
            'tx_volume': initial_values['tx_volume'], #unit: fiat
            'conversion_rate': initial_values['conversion_rate'], #unit: tok/fiat
            'cost_of_production': initial_values['cost_of_production'], #unit: fiat/labor
            'volume_of_production': initial_values['volume_of_production'], #unit: labor
            'producer_roi_estimate': initial_values['producer_roi_estimate'], #unitless //signal for informing policies
            'smooth_avg_fiat_reserve': initial_values['smooth_avg_fiat_reserve'], #unit: fiat //signal for informing policies
            'smooth_avg_token_reserve': initial_values['smooth_avg_token_reserve'], #unit: token //signal for informing policies
}

