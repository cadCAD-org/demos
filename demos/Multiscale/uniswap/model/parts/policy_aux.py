from math import sqrt


def get_parameters(uniswap_events, event, s, t):
    if(event == "TokenPurchase"):
        I_t = s['ETH_balance']
        O_t = s['DAI_balance']
        I_t1 = uniswap_events['eth_balance'][t]
        O_t1 = uniswap_events['token_balance'][t]
        delta_I = uniswap_events['eth_delta'][t]
        delta_O = abs(uniswap_events['token_delta'][t])
        action_key = 'eth_sold'
    else:
        I_t = s['DAI_balance']
        O_t = s['ETH_balance']
        I_t1 = uniswap_events['token_balance'][t]
        O_t1 = uniswap_events['eth_balance'][t]
        delta_I = uniswap_events['token_delta'][t]
        delta_O = abs(uniswap_events['eth_delta'][t])
        action_key = 'tokens_sold'
    
    return I_t, O_t, I_t1, O_t1, delta_I, delta_O, action_key

def reverse_event(event):
    if(event == "TokenPurchase"):
        new_event = 'EthPurchase'
    else:
        new_event = 'TokenPurchase'
    return new_event

def get_output_amount(delta_I, I_t, O_t, _params):
    fee_numerator = _params['fee_numerator']
    fee_denominator = _params['fee_denominator']
    delta_I_with_fee = delta_I * fee_numerator
    numerator = delta_I_with_fee * O_t                        
    denominator = (I_t * fee_denominator) + delta_I_with_fee 
    return int(numerator // denominator)                      

def get_input_amount(delta_O, I_t, O_t, _params):
    fee_numerator = _params['fee_numerator']
    fee_denominator = _params['fee_denominator']
    numerator = I_t * delta_O * fee_denominator
    denominator = (O_t - delta_O) * fee_numerator
    return int(numerator // denominator) + 1

def classifier(delta_I, delta_O, retail_precision):
    if (delta_I / (10 ** (18-retail_precision))).is_integer() or (delta_O / (10 ** (18-retail_precision))).is_integer() :
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

def unprofitable_transaction(I_t, O_t, delta_I, delta_O, action_key, _params):
    fix_cost = _params['fix_cost']
    if(fix_cost != -1):
      if(action_key == 'eth_sold'): # TokenPurchase
          after_P = 1 / get_output_amount(1, I_t, O_t, _params)
          profit = int(abs(delta_O*after_P) - (delta_I))
      else: # EthPurchase
          after_P = get_input_amount(1, I_t, O_t, _params) / 1
          profit = int(abs(delta_O) - int(delta_I/after_P))
      return (profit < fix_cost)
    else:
      return False
