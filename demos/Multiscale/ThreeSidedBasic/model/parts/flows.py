
# Behaviors
def inflow(params, step, history, current_state):
    # Receive money from relevant parties
    return {'Receive': 1}

def outflow(params, step, history, current_state):
    # Pay relevant parties
    return {'Pay': 1}


# Mechanisms 
def receive_fiat_from_consumers(params, step, sL, s, _input):
    y = 'fiat_reserve'
    if _input['Receive'] == 1:
        x = s['fiat_reserve'] + s['tx_volume'] * params['price']
    else:
        x = s['fiat_reserve']
    return (y, x)

def receive_revenue_from_consumers(params, step, sL, s, _input):
    y = 'revenue'
    if _input['Receive'] == 1:
        x = s['tx_volume'] * params['price']
    else:
        x = s['revenue']
    return (y, x)

def pay_fiat_to_producers(params, step, sL, s, _input):
    y = 'fiat_reserve'
    if _input['Pay'] == 1:
        x = s['fiat_reserve'] -  (s['product_cost'] * s['tx_volume']) 
        x = s['fiat_reserve']
    return (y, x)

def pay_investment_expenses(params, step, sL, s, _input):
    y = 'fiat_reserve'
    if _input['Pay'] == 1:
        x = s['fiat_reserve'] - s['R&D']
    else:
        x = s['fiat_reserve']
    return (y, x)

def pay_overhead_costs(params, step, sL, s, _input):
    y = 'fiat_reserve'
    if _input['Pay'] == 1:
        x = s['fiat_reserve'] - s['overhead_cost'] 
    else:
        x = s['fiat_reserve']
    return (y, x)


