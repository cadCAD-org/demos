# Model parameters
from .parts.utils import *

hatch_raise = 100000 # fiat units
hatch_price = .1 #fiat per tokens
theta = .5 #share of funds going to funding pool at launch

R0 = hatch_raise*(1-theta) # initial reserve
S0 = hatch_raise/hatch_price # initial supply

kappa = 2 # bonding curvature parameter 
V0 = invariant(R0,S0,kappa) 
P0 = spot_price(R0, V0, kappa)

initial_conditions = {
    'R0':R0,
    'S0':S0,
    'V0':V0,
    'P0':P0
    
}

sys_params = {
    'kappa': [kappa],
    'invariant': [V0],
    'dust' : [10**-8],
    'rule' : ['martin' for r in range(10)],
    'dP' : ['N/A' for r in range(10)],
    'sigma': [.1*(.5**(r+1)) for r in range(10)],
    'period': ['N/A' for r in range(10)],
    'phi': [0], #phi for exiting funds
    'beta': [0.9], #beta is param for armijo rule
}
