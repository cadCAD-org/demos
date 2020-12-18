

# Behaviors
def investors(params, step, history, current_state):
    # Pay relevant parties
    if current_state['timestep'] == 1:
        return {'Invest': 1}
    elif current_state['timestep'] == 10:
        return {'Invest': 1}
    else:
        return {'Invest': 0}


# Mechanisms 
def receive_fiat_from_investors(params, step, sL, s, _input):
    y = 'fiat_reserve'
    if _input['Invest'] == 1:
        x = s['fiat_reserve'] + s['seed_money']
    else:
        x = s['fiat_reserve']
    return (y, x)

