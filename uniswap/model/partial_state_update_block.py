from .parts.uniswap_model import *

PSUBs = [
    {
        'policies': {
            'user_action': p_actionDecoder
        },
        'variables': {
            'DAI_balance': s_mechanismHub_DAI,
            'ETH_balance': s_mechanismHub_ETH,
            'UNI_supply': s_mechanismHub_UNI,
            'fee': s_fee,
            'conv_tol': s_conv_tol
        }
    }

]