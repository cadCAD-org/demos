# import networkx as nx
from pprint import pprint

import numpy as np
import itertools

### MARKETING PARAMETERS #################################
# uniform distribution of marketing signalling
MARKETING_STEADY = [500]

# Noisy shock marketing signalling magnitude and expected frequency
MARKETING_SHOCK_MAG = [1234]
MARKETING_SHOCK_FREQ = [2]

### EXTERNAL EXPERIENCE PARAMETERS #################################
# If UX/UI are not part of the model. Can use as an external signal to
#  generate stochastic process for experience.
EXO_EXPERIENCE = [140]

### POPULATION POOL PARAMETERS #################################
SOURCE_POOL = [100000] #, 12]

### INITIAL THRESHOLD VALUE PARAMETERS #################################
THRESHOLD = [0.1, 1, 2, 3]
LEAK_COEFFICIENT = [0.01]


#### USE ONLY FOR A/B WITH PARAMETER SWEEPS OR MULTIPLE PARAMETER SWEEPS #####

factors = [MARKETING_STEADY,SOURCE_POOL, THRESHOLD, LEAK_COEFFICIENT]
product = list(itertools.product(*factors))
MARKETING_STEADY,SOURCE_POOL, THRESHOLD, LEAK_COEFFICIENT = zip(*product)
MARKETING_STEADY = list(MARKETING_STEADY)
SOURCE_POOL = list(SOURCE_POOL)
THRESHOLD = list(THRESHOLD)
LEAK_COEFFICIENT = list(LEAK_COEFFICIENT)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
sys_params = {
   'MARKETING_STEADY': MARKETING_STEADY,
   'MARKETING_SHOCK_MAG': MARKETING_SHOCK_MAG, 
   'MARKETING_SHOCK_FREQ': MARKETING_SHOCK_FREQ,
   'EXO_EXPERIENCE': EXO_EXPERIENCE,
   'SOURCE_POOL': SOURCE_POOL,
   'THRESHOLD': THRESHOLD, 
   'LEAK_COEFFICIENT': LEAK_COEFFICIENT,
}