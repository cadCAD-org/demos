import numpy as np


## Policies

def p_infected_growth(params, substep, state_history, prev_state):
    infected_population = params['infection_rate']*prev_state['infected']*prev_state['susceptible']/(prev_state['susceptible'] + prev_state['infected'] + prev_state['recovered'])
    return {'infected_growth': infected_population}


def p_recovered_growth(params, substep, state_history, prev_state):
    recovered_population = params['recovering_rate']*prev_state['infected']
    return {'recovered_growth': recovered_population}


## SUFs

def s_susceptible_population(params, substep, state_history, prev_state, policy_input):
    updated_susceptible_population = prev_state['susceptible'] - policy_input['infected_growth']
    return ('susceptible', max(updated_susceptible_population, 0))


def s_infected_population(params, substep, state_history, prev_state, policy_input):
    updated_infective_population = prev_state['infected'] + policy_input['infected_growth'] - policy_input['recovered_growth']
    return ('infected', max(updated_infective_population, 0))
        

def s_recovered_population(params, substep, state_history, prev_state, policy_input):
    updated_recovered_population = prev_state['recovered'] + policy_input['recovered_growth']
    return ('recovered', max(updated_recovered_population, 0))