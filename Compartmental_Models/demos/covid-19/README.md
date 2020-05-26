# Covid-19 demo

cadCAD Covid-19 SIR, SEIR and SEIRD modelling in an dynamical system approach.

## File Structure

* lab_notebook.ipynb - The notebook for experimenting and visualizing
* run.py - Script for running all configurated experiments
* covid_19_seir/ - Folder for the SEIR simulation model
* covid_19_seird/ - Folder for the SEIRD simulation model
* covid_19_sir/ - Folder for the SIR simulation model
* {simulation}/config.py - Simulation configuration object
* {simulation}/sim_params.py - Simulation parameters
* {simulation}/model/partial_state_update_block.py - The structure of the logic behind the model
* {simulation}/model/state_variables.py - Model initial state
* {simulation}/model/sys_params.py - Model parameters
* {simulation}/model/parts/ - Model logic