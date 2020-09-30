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
    'rule' : ["martin", "step","ramp", "sin"],
    'dP' : ['N/A', P0/4, P0/1000, P0/2],
    'sigma': [.005,'N/A','N/A', 'N/A'],
    'period': ['N/A', 2000,2000,2000],
    'phi': [0], #phi for exiting funds
    'beta': [0.9], #beta is param for armijo rule
}
