import pandas as pd

c_rule = 3

df = pd.read_pickle('uniswap_events.pickle')

def classifier(event, eth_delta, token_delta, c_rule):
    if event == 'TokenPurchase':
        if (eth_delta / (1 ** (18-c_rule))).is_integer():
            return 'Convenience'
        else:
            return 'Arbitrage'
    elif event == 'EthPurchase':
        if (eth_delta / (1 ** (18-c_rule))).is_integer():
            return 'Convenience'
        else:
            return 'Arbitrage'
    else:
        return 'None'

df['TradeClass'] = df.apply(lambda x: classifier(x['event'], x['eth_delta'], x['token_delta'], c_rule), axis=1)