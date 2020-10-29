# Epidemiological analysis with cadCAD

cadCAD SIR, SEIR and SEIRD modelling in a dynamical system approach.

## File Structure

* images/ - Folder for the model mechanism and stock & flow diagrams 
* lab_notebook.ipynb - The notebook for experimenting and visualizing
* run.py - Script for running all configurated experiments
* seir/ - Folder for the SEIR simulation model
* seird/ - Folder for the SEIRD simulation model
* sir/ - Folder for the SIR simulation model
* stochastic_seir/ - Folder for the SEIR stochastic simulation model
* {simulation}/config.py - Simulation configuration object
* {simulation}/sim_params.py - Simulation parameters
* {simulation}/model/partial_state_update_block.py - The structure of the logic behind the model
* {simulation}/model/state_variables.py - Model initial state
* {simulation}/model/sys_params.py - Model parameters
* {simulation}/model/parts/ - Model logic
