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