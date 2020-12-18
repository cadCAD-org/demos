# Behaviors
def kpis(params, step, history, current_state):
    return {'Stat': 1}



# Mechanisms
def COGS(params, step, sL, s, _input):
    y = 'COGS'
    if _input['Stat'] == 1:
        x = (s['product_cost'] * s['tx_volume']) 
    else:
        x = s['COGS']
    return (y, x)

