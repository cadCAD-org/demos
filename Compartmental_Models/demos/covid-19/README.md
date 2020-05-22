# Covid-19 demo

cadCAD Covid-19 SIER modelling in an dynamical system approach.

## File Structure

* lab_notebook.ipynb - The notebook for experimenting and visualizing
* run.py - Script for running all configurated experiments
* prey_predator_abm/ - Folder for the ABM simulation and model 
* prey_predator_sd/ - Folder for the SD simulation and model
* {simulation}/config.py - Simulation configuration object
* {simulation}/sim_params.py - Simulation parameters
* {simulation}/model/partial_state_update_block.py - The structure of the logic behind the model
* {simulation}/model/state_variables.py - Model initial state
* {simulation}/model/sys_params.py - Model parameters
* {simulation}/model/parts/ - Model logic