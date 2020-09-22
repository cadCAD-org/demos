sys_params = {
        # 𝛽:  expected amount of people an infected person infects per day
        'infection_rate': [1],        
        # 𝛾: the proportion of infected recovering per day ( 𝛾  = 1/D)
        'recovering_rate': [1/4],
        # 𝛿: expected rate that exposed people turn into infected
        'exposure_rate': [1/3],
        # serial interval parameters
        'si_pars': [{'mean': 4.7, 'sd': 2.9}],
        'window_width': [2],
}
