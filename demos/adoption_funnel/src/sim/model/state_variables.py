from datetime import datetime
# import networkx as nx
import numpy as np

# from copy import deepcopy
# import scipy.stats as stats
# from .sys_params import sys_params
from src.sim.model.utils import *

# Initial Values
signal = 0
# state = 0
adoption = Adoption()
# pool = Adoption_Pool() # Iniialized in config loop using source_pool parameter

## Genesis States #################################################
genesis_states = {
    'timestamp': datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
    'signal': signal,
    # 'adoption': adoption,  # Agent Based
    # 'pool' : pool,  # Iniialized in config loop using source_pool parameter

}