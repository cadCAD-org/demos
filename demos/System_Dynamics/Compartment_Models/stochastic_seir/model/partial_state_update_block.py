from .parts.seir_model import *


partial_state_update_block = [
    {
        'policies': {
            'exposed_growth': p_exposed_growth,
            'infected_growth': p_infected_growth,
            'recovered_growth': p_recovered_growth
        },
        'variables': {
            'susceptible': s_susceptible_population,
            'exposed': s_exposed_population,
            'infected': s_infected_population,
            'recovered': s_recovered_population   
        }
    }

]