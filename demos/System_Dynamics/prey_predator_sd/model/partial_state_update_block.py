from .parts.lotka_volterra import *


partial_state_update_block = [
    {
        # lotka_volterra.py
        'policies': {
            'reproduce_prey': reproduce_prey,
            'reproduce_predators': reproduce_predators,
            'eliminate_prey': eliminate_prey,
            'eliminate_predators': eliminate_predators
        },
        'variables': {
            'prey_population': prey_population,
            'predator_population': predator_population            
        }
    }

]