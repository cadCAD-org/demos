from cadCAD.configuration import Configuration

initial_conditions = {
    'susceptible': 90000,
    'insusceptible': 0,
    'exposed': 8000 ,
    'infective': 2000,
    'quarantined': 0,
    'recovered': 0,
    'death': 0,
    'cure_rate': 0.1,
    'mortality_rate': 0.01
}

simulation_parameters = {   
    'T': range(120), #number of discrete iterations in each experiement
    'N': 1, #number of times the simulation will be run (Monte Carlo runs)
    'M': {
        'protection_rate': 0,
        'infection_rate': 2,
        'average_latent_time': 5,
        'average_quarantine_time': 14
    }   
}

# Policies

def p_exposure_growth(params, substep, state_history, prev_state):
    exposed_population = params['infection_rate'] * prev_state['susceptible']
    exposed_population = exposed_population * (prev_state['infective'] / 100000)
    return {'exposure_growth': exposed_population}


def p_protection_growth(params, substep, state_history, prev_state):
    protected_population = params['protection_rate']*prev_state['susceptible']
    return {'protection_growth': protected_population}


def p_infection_growth(params, substep, state_history, prev_state):
    infected_population = (1/params['average_latent_time'])*prev_state['exposed']
    return {'infection_growth': infected_population}


def p_quarantined_growth(params, substep, state_history, prev_state):
    quarantined_population = (1/params['average_quarantine_time'])*prev_state['infective']
    return {'quarantined_growth': quarantined_population}


def p_recovered_growth(params, substep, state_history, prev_state):
    recovered_population = prev_state['cure_rate']*prev_state['quarantined']
    return {'recovered_growth': recovered_population}


def p_death_growth(params, substep, state_history, prev_state):
    death_population = prev_state['mortality_rate']*prev_state['quarantined']
    return {'death_growth': death_population}


def p_insusceptible_growth(params, substep, state_history, prev_state):
    insusceptible_population = params['protection_rate']*prev_state['susceptible']
    return {'insusceptible_growth': insusceptible_population}



# State Update Functions

def s_susceptible_population(params, substep, state_history, prev_state, policy_input):
    updated_susceptible_population = prev_state['susceptible'] - policy_input['exposure_growth'] - policy_input['protection_growth']
    return ('susceptible', max(round(updated_susceptible_population), 0))


def s_infective_population(params, substep, state_history, prev_state, policy_input):
    updated_infective_population = prev_state['infective'] + policy_input['infection_growth'] - policy_input['quarantined_growth']
    return ('infective', max(round(updated_infective_population), 0))
        
    
def s_exposed_population(params, substep, state_history, prev_state, policy_input):
    updated_exposed_population = prev_state['exposed'] + policy_input['exposure_growth'] - policy_input['infection_growth']
    return ('exposed', max(round(updated_exposed_population), 0))


def s_insusceptible_population(params, substep, state_history, prev_state, policy_input):
    updated_insusceptible_population = prev_state['insusceptible'] + policy_input['insusceptible_growth']
    return ('insusceptible', max(round(updated_insusceptible_population), 0))
    

def s_quarantined_population(params, substep, state_history, prev_state, policy_input):
    updated_quarantined_population = prev_state['quarantined'] + policy_input['quarantined_growth'] - policy_input['recovered_growth'] - policy_input['death_growth']
    return ('quarantined', max(round(updated_quarantined_population), 0))


def s_recovered_population(params, substep, state_history, prev_state, policy_input):
    updated_recovered_population = prev_state['recovered'] + policy_input['recovered_growth']
    return ('recovered', max(round(updated_recovered_population), 0))


def s_death_population(params, substep, state_history, prev_state, policy_input):
    updated_death_population = prev_state['death'] + policy_input['death_growth']
    return ('death', max(round(updated_death_population), 0))


partial_state_update_blocks = [
    {
        'policies': {
            'exposure_growth': p_exposure_growth,
            'protection_growth': p_protection_growth,
            'infection_growth': p_infection_growth,
            'quarantined_growth': p_quarantined_growth,
            'recovered_growth': p_recovered_growth,
            'death_growth': p_death_growth,
            'insusceptible_growth': p_insusceptible_growth
        },
        'variables':{
            'susceptible': s_susceptible_population,
            'insusceptible': s_insusceptible_population,
            'exposed': s_exposed_population,
            'infective': s_infective_population,
            'quarantined': s_quarantined_population,
            'recovered': s_recovered_population,
            'death': s_death_population 
        }
    }
]

config = Configuration(initial_state=initial_conditions, #dict containing variable names and initial values
                       partial_state_update_blocks=partial_state_update_blocks, #dict containing state update functions
                       sim_config=simulation_parameters #dict containing simulation parameters
                      )


