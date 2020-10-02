from .policy_aux import get_input_price

def addLiquidity_ETH(_params, substep, sH, s, _input):
    eth_reserve = int(s['ETH_balance'])
    return ('ETH_balance', eth_reserve + _input['eth_deposit'])


def removeLiquidity_ETH(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    eth_reserve = int(s['ETH_balance'])
    amount = int(_input['UNI_burn'])
    eth_amount = int(amount * eth_reserve // total_liquidity)
    return ('ETH_balance', int(eth_reserve - eth_amount))


def ethToToken_ETH(_params, substep, history, s, _input):
    delta_I = int(_input['eth_sold']) #amount of ETH being sold by the user
    I_t = int(s['ETH_balance'])
    return ('ETH_balance', I_t + delta_I)


def tokenToEth_ETH(_params, substep, sH, s, _input):
    delta_I = int(_input['tokens_sold']) #amount of tokens being sold by the user
    O_t = int(s['ETH_balance'])
    I_t = int(s['DAI_balance'])
    if delta_I == 0:
        return ('ETH_balance', O_t)
    else:
        delta_O = int(get_input_price(delta_I, I_t, O_t, _params))
        return ('ETH_balance', O_t - delta_O)
    