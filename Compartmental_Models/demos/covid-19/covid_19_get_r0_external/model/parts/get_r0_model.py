import numpy as np 
import pandas as pd


def get_current_timestep(cur_substep, s):
    if cur_substep == 1:
        return s['timestep']+1
    return s['timestep']


def get_dataframe(path):
    data = pd.read_csv(path)
    return data


## Policies


def p_recovering_rate_estimation(params, substep, state_history, prev_state):
    data = get_dataframe('data/sp_r0.csv')
    data_diff = data.copy()
    data_diff = data_diff.diff(axis=0)
    daily_recovered = data_diff.iloc[get_current_timestep(substep, prev_state),3]
    daily_infected = data_diff.iloc[get_current_timestep(substep, prev_state),2]
    susceptible_population = data.iloc[get_current_timestep(substep, prev_state),1]
    infected_population = data.iloc[get_current_timestep(substep, prev_state),2]
    recovering_rate_estimation = daily_recovered /  infected_population
    infection_rate_estimation = (daily_infected + daily_recovered)/(infected_population*susceptible_population/12252023)
    r0_estimation =  infection_rate_estimation/recovering_rate_estimation
    return {'recovering_rate_estimation': r0_estimation}


def p_infection_rate_estimation(params, substep, state_history, prev_state):
    data = get_dataframe('data/sp_r0.csv')
    data_diff = data.copy()
    data_diff = data_diff.diff(axis=0)
    daily_infected = data_diff.iloc[get_current_timestep(substep, prev_state),1]
    daily_recovered = data_diff.iloc[get_current_timestep(substep, prev_state),2]
    return {'infection_rate_estimation': daily_infected}


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


def s_dead_population(params, substep, state_history, prev_state, policy_input):
    updated_dead_population = prev_state['dead'] + policy_input['dead_growth']
    return ('dead', max(updated_dead_population, 0))


def s_r0_estimation(params,     substep, state_history, prev_state, policy_input):
    r0_estimation = policy_input['recovering_rate_estimation']
    return('r0_estimation', r0_estimation) 