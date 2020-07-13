from scipy.stats import lognorm, norm
import numpy as np

def init_param_dist(param_init, rand_seed):
    '''Initialize distribution from tuple, scipy or array-like object.
    Args:
        param_init (tuple, scipy.stats dist., or array-like)
    Examples:
        >>> np.random.seed(0)
        >>> dist = SEIRBayes.init_param_dist((1, 2, .9, 'lognorm'))
        >>> dist.interval(0.9)
        (1.0, 2.0)
        >>> dist = SEIRBayes.init_param_dist([0.1, 0.2, 0.3])
        >>> dist.rvs(2)
        array([0.1, 0.2])
        >>> from scipy.stats import lognorm
        >>> dist = SEIRBayes.init_param_dist(lognorm(s=.1, scale=1))
        >>> dist.mean()
        1.005012520859401
    '''
    if isinstance(param_init, tuple):
        lb, ub, density, family = param_init
        if family != 'lognorm':
            raise NotImplementedError('Only family lognorm '
                                      'is implemented')

        dist = make_lognormal_from_interval(lb, ub, density, rand_seed)
    return dist

def make_lognormal_from_interval(lb, ub, alpha, rand_seed):
    ''' Creates a lognormal distribution SciPy object from intervals.
    This function is a helper to create SciPy distributions by specifying the
    amount of wanted density between a lower and upper bound. For example,
    calling with (lb, ub, alpha) = (2, 3, 0.95) will create a LogNormal
    distribution with 95% density between 2 a 3.
    Args:
        lb (float): Lower bound
        ub (float): Upper bound
        alpha (float): Total density between lb and ub
    Returns:
        scipy.stats.lognorm
    
    Examples:
        >>> dist = make_lognormal_from_interval(2, 3, 0.95)
        >>> dist.mean()
        2.46262863041182
        >>> dist.std()
        0.25540947842844575
        >>> dist.interval(0.95)
        (1.9999999999999998, 2.9999999999999996)
    '''
    z = norm()
    z.random_state = rand_seed
    z = z.interval(alpha)[1]
    mean_norm = np.sqrt(ub * lb)
    std_norm = np.log(ub / lb) / (2 * z)
    log_dist = lognorm(s=std_norm, scale=mean_norm)
    log_dist.random_state = rand_seed
    return log_dist


    #random value mesma ordem mesmo valor em dois sweep diferentes