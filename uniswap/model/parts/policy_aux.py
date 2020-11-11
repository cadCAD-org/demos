from math import sqrt

def get_parameters(uniswap_events, event, s, t):
    if(event == "TokenPurchase"):
        I_t = s['ETH_balance']
        O_t = s['DAI_balance']
        I_t1 = uniswap_events['eth_balance'][t]
        O_t1 = uniswap_events['token_balance'][t]
        delta_I = uniswap_events['eth_delta'][t]
        delta_O = uniswap_events['token_delta'][t]
        action_key = 'eth_sold'
    else:
        I_t = s['DAI_balance']
        O_t = s['ETH_balance']
        I_t1 = uniswap_events['token_balance'][t]
        O_t1 = uniswap_events['eth_balance'][t]
        delta_I = uniswap_events['token_delta'][t]
        delta_O = uniswap_events['eth_delta'][t]
        action_key = 'tokens_sold'
    
    return I_t, O_t, I_t1, O_t1, delta_I, delta_O, action_key

def reverse_event(event):
    if(event == "TokenPurchase"):
        new_event = 'EthPurchase'
    else:
        new_event = 'TokenPurchase'
    return new_event

def get_input_price(delta_I, I_t, O_t, _params):
    fee_numerator = _params['fee_numerator']
    fee_denominator = _params['fee_denominator']
    delta_I_with_fee = delta_I * fee_numerator
    numerator = delta_I_with_fee * O_t
    denominator = (I_t * fee_denominator) + delta_I_with_fee
    return int(numerator // denominator)

def classifier(delta_I, delta_O, c_rule):
    if (delta_I / (10 ** (18-c_rule))).is_integer() or (delta_O / (10 ** (18-c_rule))).is_integer() :
      return "Conv"
    else:
      return "Arb"

def get_delta_I(P, I_t, O_t, _params):
    a = _params['fee_numerator']
    b = _params['fee_denominator']
    delta_I = (
        (-(I_t*b + I_t*a)) + sqrt(
            ((I_t*b - I_t*a)**2) + (4*P*O_t*I_t*a*b)
        )
    )  / (2*a)

    return int(delta_I)

def unprofitable_transaction(t, type_of, P, actual_P, delta_I, delta_O, action_key, convert_rate, _params):
    fix_cost = int((_params['fix_cost']/convert_rate)*(10**18))
    if(delta_O < 0):
        print(delta_O)
    if(action_key == 'eth_sold'):
        profit = delta_O*P - (delta_I)
        # if(t<50):
            # print(action_key)
            # print("is inverted:     ", type_of)
            # print("actual_P: ", actual_P)
            # print("P       : ", P)
            # print("delta_I    (ETH): ", delta_I)
            # print("delta_O*P  (ETH): ", int(delta_O*P))
            # print("abs_profit (ETH): ", profit)
            # print("fix_cost   (ETH): ", fix_cost)
            # print("abs_profit (USD): ", (profit/(10**18))*convert_rate)
    else:
        profit = delta_O - int(delta_I/P)
        # if(t<50):
            # print(action_key)
            # print("is inverted:     ", type_of)
            # print("actual_P: ", actual_P)
            # print("P       : ", P)
            # print("delta_I/P  (ETH): ", int(delta_I/P))
            # print("delta_O    (ETH): ", delta_O)
            # print("abs_profit (ETH): ", profit)
            # print("fix_cost   (ETH): ", fix_cost)
            # print("abs_profit (USD): ", (profit/(10**18))*convert_rate)
    return (profit < fix_cost)
