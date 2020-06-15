import numpy as np 
import pandas as pd
from .reproductive_number import ReproductionNumber
## Help functions

def get_current_timestep(cur_substep, s):
    if cur_substep == 1:
        return s['timestep']+1
    return s['timestep']

def predict_reproductive_number(incidence, si_pars, window_width):
    predictor = ReproductionNumber(incidence=incidence, si_pars=si_pars, window_width=window_width)
    predictor.compute_overall_infectivity()
    predictor.compute_posterior_parameters()
    predictor.compute_posterior_summaries(predictor.sample_from_posterior(), t_max=1)
    return predictor.posterior_summary.iloc[-1]['Rt_mean']

## Policies

def p_exposed_growth(params, substep, state_history, prev_state):
    infection_rate = prev_state['reproductive_number']
    exposed_population = infection_rate*prev_state['infected']*(prev_state['susceptible']/(prev_state['susceptible']+ prev_state['exposed'] + prev_state['infected'] + prev_state['recovered']))
    if(exposed_population > prev_state['susceptible']):
        exposed_population = prev_state['susceptible']
    return {'exposed_growth': np.ceil(exposed_population)}

def p_infected_growth(params, substep, state_history, prev_state):
    infected_population = params['exposure_rate']*prev_state['exposed']
    if(infected_population > prev_state['exposed']):
        infected_population = prev_state['exposed']
    return {'infected_growth': np.ceil(infected_population)}

def p_recovered_growth(params, substep, state_history, prev_state):
    recovered_population = params['recovering_rate']*prev_state['infected']
    if(recovered_population > prev_state['infected']):
        recovered_population = prev_state['infected']
    return {'recovered_growth': np.ceil(recovered_population)}

def p_incidence_growth(params, substep, state_history, prev_state):
    incidence_cases = params['exposure_rate']*prev_state['exposed']
    return {'incidence_growth': np.ceil(incidence_cases)}

def p_total_infected_growth(params, substep, state_history, prev_state):
    total_infected = prev_state['recovered']+prev_state['infected']+prev_state['exposed']
    return {'total_infected_growth': np.ceil(total_infected)}

def p_reproductive_number_mutation(params, substep, state_history, prev_state):
    if (len(state_history) >= 2*params['window_width']):
        incidence = []
        for state in state_history:
            filter_dict = {k: v for k,v in state[0].items() if k in ['incidence', 'timestep']}
            incidence.append(filter_dict)
        incidence = pd.DataFrame(incidence)
        incidence.rename(columns={'timestep': 'dates'}, inplace=True)
        reproductive_number = predict_reproductive_number(incidence, params['si_pars'], params['window_width'])

    else:
        reproductive_number = prev_state['reproductive_number']
    return {'reproductive_number_mutation': reproductive_number}


## SUFs

def s_susceptible_population(params, substep, state_history, prev_state, policy_input):
    updated_susceptible_population = prev_state['susceptible'] - policy_input['exposed_growth']
    return ('susceptible', max(updated_susceptible_population, 0))

def s_exposed_population(params, substep, state_history, prev_state, policy_input):
    updated_exposed_population = prev_state['exposed'] + policy_input['exposed_growth'] - policy_input['infected_growth']
    return ('exposed', max(updated_exposed_population, 0))

def s_infected_population(params, substep, state_history, prev_state, policy_input):
    updated_infected_population = prev_state['infected'] + policy_input['infected_growth'] - policy_input['recovered_growth']
    return ('infected', max(updated_infected_population, 0))

def s_recovered_population(params, substep, state_history, prev_state, policy_input):
    updated_recovered_population = prev_state['recovered'] + policy_input['recovered_growth']
    return ('recovered', max(updated_recovered_population, 0))

def s_incidence_population(params, substep, state_history, prev_state, policy_input):
    return ('incidence', max(policy_input['incidence_growth'], 0))

def s_total_infected(params, substep, state_history, prev_state, policy_input):
    return ('total_infected', max(policy_input['total_infected_growth'], 0))

def s_reproductive_number(params, substep, state_history, prev_state, policy_input):
    return ('reproductive_number', policy_input['reproductive_number_mutation'])