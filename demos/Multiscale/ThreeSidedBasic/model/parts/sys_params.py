

# params
params = {
    'eta': [.33], # for tx_volume_generator
    'tampw': [100000], # transactions limit
    'alpha': [.5], # for data acquisition cost generator
    'beta': [.2], # for data acquisition cost generator
    'costDecrease': [.015], # decrease in cost
    'price': [1], # sales price
    'vcRoundFunding': [100000.0],
    'overHeadCosts': [5000.0]
}



# Initial States
initial_values = { 
            'tx_volume': float(100), #unit: fiat
            'product_cost': float(.3), #unit: fiat cost
            'revenue': float(0), # revenue per month
            'fiat_reserve': float(0),#unit: fiat
            'overhead_cost': float(100), #unit: fiat per month
            'seed_money': float(0),
            'R&D': float(0), #per month
            'COGS': float(0), #per month
}
