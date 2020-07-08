sys_params = {
        '''
                The above tuples are create following a pattern, being this:
                (lower_bond, upper_bond, density, distribution_family).
        '''
        # reproduction number
        'r0_dist': [(2.5, 6, 0.95, 'lognorm')],
        # infectious period
        'alpha_dist': [(7, 14, 0.95, 'lognorm')],
        # incubation period
        'gamma_dist': [(4.1, 7, 0.95, 'lognorm')],
        # random seed to control the behavior of random parameters
        'rand_seed': [233423, 1, 51, 200]
}