from .parts.seird_variable_r0_model import *


partial_state_update_block = [
    {
        'policies': {
            'exposed_growth': p_exposed_growth,
            'infected_growth': p_infected_growth,
            'recovered_growth': p_recovered_growth,
            'dead_growth': p_dead_growth,
            'daily_infection_rate_growth': p_daily_infection_rate_growth
        },
        'variables': {
            'susceptible': s_susceptible_population,
            'exposed': s_exposed_population,
            'infected': s_infected_population,
            'recovered': s_recovered_population,
            'dead': s_dead_population,
            'daily_infection_rate': s_daily_infection_rate 
        }
    }

]