from math import sqrt

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

def get_trade_decision(delta_I, delta_O, I_t, O_t, I_t1, O_t1, _params):
    if classifier(delta_I, delta_O, _params['c_rule']) == 'Conv':
        calculated_delta_O = int(get_input_price(delta_I, I_t, O_t, _params))
        historic_delta_O = int(get_input_price(delta_I, I_t1, O_t1, _params))
        if calculated_delta_O >= historic_delta_O * (1 - _params['conv_tolerance']):
            return delta_I
        else:
            return 0
    else:
        P = (I_t + delta_I) / (O_t + delta_O)
        delta_I = get_delta_I(P, I_t, O_t, _params)

        return delta_I

def get_delta_I(P, I_t, O_t, _params):
    a = _params['fee_numerator']
    b = _params['fee_denominator']
    delta_I = (
        (-(I_t*b + I_t*a)) + sqrt(
            ((I_t*b - I_t*a)**2) + (4*P*O_t*I_t*a*b)
        )
    )  / (2*a)

    return int(delta_I)