from .policy_aux import get_input_price

def addLiquidity_DAI(_params, substep, sH, s, _input):
    eth_reserve = int(s['ETH_balance'])
    token_reserve = int(s['DAI_balance'])
    if _input['eth_deposit'] == 0:
        token_amount = 0
    else:
        token_amount = int(_input['eth_deposit'] * token_reserve // eth_reserve + 1)
    return ('DAI_balance', token_reserve + token_amount)



def removeLiquidity_DAI(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    token_reserve = int(s['DAI_balance'])
    amount = int(_input['UNI_burn'])
    token_amount = int(amount * token_reserve // total_liquidity)
    return ('DAI_balance', int(token_reserve - token_amount))



def ethToToken_DAI(_params, substep, sH, s, _input):
    delta_I = int(_input['eth_sold']) #amount of ETH being sold by the user
    I_t = int(s['ETH_balance'])
    O_t = int(s['DAI_balance'])
    if delta_I == 0:
        return ('DAI_balance', O_t)
    else:
        delta_O = int(get_input_price(delta_I, I_t, O_t, _params))
        return ('DAI_balance', O_t - delta_O)


def tokenToEth_DAI(_params, substep, sH, s, _input):
    delta_I = int(_input['tokens_sold']) #amount of tokens being sold by the user
    I_t = int(s['DAI_balance'])
    return ('DAI_balance', I_t + delta_I)