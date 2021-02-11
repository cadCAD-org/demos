from .policy_aux import get_output_amount


# DAI functions

def addLiquidity_DAI(_params, substep, sH, s, _input):
    eth_reserve = int(s['ETH_balance'])
    token_reserve = int(s['DAI_balance'])
    if _input['eth_deposit'] == 0:
        token_amount = 0
    else:
        token_amount = int(_input['eth_deposit'] * token_reserve // eth_reserve + 1)
    return ('DAI_balance', token_reserve + token_amount)


def removeLiquidity_DAI(_params, substep, sH, s, _input):
    token_reserve = int(s['DAI_balance'])
    pct_amount = _input['UNI_pct']
    amount = token_reserve * pct_amount
    return ('DAI_balance', int(token_reserve - amount))


def ethToToken_DAI(_params, substep, sH, s, _input):
    delta_I = int(_input['eth_sold']) #amount of ETH being sold by the user
    I_t = int(s['ETH_balance'])
    O_t = int(s['DAI_balance'])
    if delta_I == 0:
        return ('DAI_balance', O_t)
    else:
        delta_O = int(get_output_amount(delta_I, I_t, O_t, _params))
        return ('DAI_balance', O_t - delta_O)


def tokenToEth_DAI(_params, substep, sH, s, _input):
    delta_I = int(_input['tokens_sold']) #amount of tokens being sold by the user
    I_t = int(s['DAI_balance'])
    return ('DAI_balance', I_t + delta_I)


# ETH functions

def addLiquidity_ETH(_params, substep, sH, s, _input):
    eth_reserve = int(s['ETH_balance'])
    return ('ETH_balance', eth_reserve + _input['eth_deposit'])


def removeLiquidity_ETH(_params, substep, sH, s, _input):
    eth_reserve = int(s['ETH_balance'])
    pct_amount = _input['UNI_pct']
    amount = pct_amount * eth_reserve
    return ('ETH_balance', int(eth_reserve - amount))


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
        delta_O = int(get_output_amount(delta_I, I_t, O_t, _params))
        return ('ETH_balance', O_t - delta_O)
    

# UNI functions

def addLiquidity_UNI(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    eth_reserve = int(s['ETH_balance'])
    liquidity_minted = int(_input['eth_deposit'] * total_liquidity // eth_reserve)
    return ('UNI_supply', total_liquidity + liquidity_minted)


def removeLiquidity_UNI(_params, substep, sH, s, _input):
    total_liquidity = int(s['UNI_supply'])
    pct_amount = _input['UNI_pct']
    amount = total_liquidity * pct_amount
    return ('UNI_supply', int(total_liquidity - amount))