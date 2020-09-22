from .parts.seir_model import *


partial_state_update_block = [
    {
        'policies': {
            'exposed_growth': p_exposed_growth,
            'infected_growth': p_infected_growth,
            'recovered_growth': p_recovered_growth,
            'incidence_growth': p_incidence_growth,
            'total_infected_growth': p_total_infected_growth,
            'reproductive_number_mutation': p_reproductive_number_mutation
        },
        'variables': {
            'susceptible': s_susceptible_population,
            'exposed': s_exposed_population,
            'infected': s_infected_population,
            'recovered': s_recovered_population,
            'incidence': s_incidence_population,
            'total_infected': s_total_infected,
            'reproductive_number': s_reproductive_number 
        }
    }
]