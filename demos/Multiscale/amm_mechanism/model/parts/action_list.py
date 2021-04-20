# Behaviors

def actionDecoder(params, step, history, prev_state):
    '''
    In this simplified model of Uniswap, we have not modeled user behavior. Instead, we map events to actions. Depending on the input system parameters 'params' a given action sequence is induced.
    '''
    
    action = {
        'q_sold': 0,     # q to r swap
        'ri_sold': 0,     # r to q swap
        'ri_deposit': 0,   # add liq
        'q_deposit': 0,  # if symmetric add liq
        'Si_burn': 0,    # remove liq    
        'action_id' : str(),
        'agent_id' : 0,
        'asset_id' : str(),
        'direction': str() 
    }
    
    ACTION_LIST =  params['ACTION_LIST']
    # print(ACTION_LIST)


    timestep = prev_state['timestep']

    ############ CHOOSE ASSET TYPE #############################
    ####### PREVIOUS MULTIPLE SUBSTEP TO EXECUTE EACH INSTANCE ###########
    # if step == 1 or step == 2:
    #     action['asset_id'] = 'i'
    # if step == 3 or step == 4:
    #     action['asset_id'] = 'j'
    ############ CHOOSE ASSET TYPE #############################


    ############ CHOOSE ASSET TYPE #############################
    ### USE A PARAM TO CHOOSE COMPOSITE AND ASSET TYPE TRANSACTIONS 
    
    if params['exo_asset'] == 'alternating':
        if timestep % 2 == 0:
            action['asset_id'] = 'i'
        elif timestep % 2 == 1:
            action['asset_id'] = 'j'

    if params['exo_asset'] == 'i_only':
        action['asset_id'] = 'i'

    if params['exo_asset'] == 'j_only':
        action['asset_id'] = 'j'

    ############ CHOOSE ASSET TYPE #############################
    
    ############ CHOOSE COMPOSITE ACTION TYPE #############################
    ### WILL USE A PARAM TO CHOOSE COMPOSITE AND ASSET TYPE TRANSACTIONS 
    
    # if params['exo_composite'] == 'alternating':
    if timestep % len(ACTION_LIST) == 0:
            params['exo_trade'] = ACTION_LIST[0] # automate this
            # params['exo_trade'] = 'test_r_for_q' # automate this
            params['exo_liq'] = ACTION_LIST[0]
            # params['exo_liq'] = 'test_remove'
            # params['exo_trade'] = 'pass'
            # params['exo_trade'] = 'test_r_for_r' # automate this
            # params['exo_trade'] = 'test_r_for_r' # automate this
    elif timestep % len(ACTION_LIST)  == 1:
            params['exo_trade'] = ACTION_LIST[1] # automate this
            # params['exo_trade'] = 'test_r_for_q' # automate this
            params['exo_liq'] = ACTION_LIST[1]
            # params['exo_liq'] = 'test_remove'
    # elif timestep % len(ACTION_LIST)  == 2:
    #         params['exo_trade'] = ACTION_LIST[2] # automate this
    #         # params['exo_trade'] = 'test_r_for_q' # automate this
    #         params['exo_liq'] = ACTION_LIST[2]
    #         # params['exo_liq'] = 'test_remove'        
    # elif timestep % len(ACTION_LIST)  == 3:
    #         params['exo_trade'] = ACTION_LIST[3] # automate this
    #         # params['exo_trade'] = 'test_r_for_q' # automate this
    #         params['exo_liq'] = ACTION_LIST[3]
    #         # params['exo_liq'] = 'test_remove'    
    # elif timestep % len(ACTION_LIST)  == 4:
    #         params['exo_trade'] = ACTION_LIST[4] # automate this
    #         # params['exo_trade'] = 'test_r_for_q' # automate this
    #         params['exo_liq'] = ACTION_LIST[4]
    #         # params['exo_liq'] = 'test_remove'   

    ############ CHOOSE COMPOSITE ACTION TYPE #############################
    ### WILL USE A PARAM TO CHOOSE COMPOSITE AND ASSET TYPE TRANSACTIONS 
    
    # if params['exo_composite'] == 'alternating':
    #     if timestep % 2 == 0:
    #         params['exo_trade'] = 'test_q_for_r' # automate this
    #         # params['exo_trade'] = 'test_r_for_q' # automate this
    #         params['exo_liq'] = 'pass'
    #         # params['exo_liq'] = 'test_remove'
    #         # params['exo_trade'] = 'pass'
    #         # params['exo_trade'] = 'test_r_for_r' # automate this
    #         # params['exo_trade'] = 'test_r_for_r' # automate this



    #         # print(timestep, params['exo_trade'], action['asset_id'])
    #     elif timestep % 2 == 1:
    #         params['exo_liq'] = 'pass'
    #         # params['exo_liq'] = 'test_add'
    #         # params['exo_liq'] = 'test_remove'
    #         # params['exo_trade'] = 'pass'
    #         params['exo_trade'] = 'test_r_for_q' # automate this

    #         # params['exo_trade'] = 'test_r_for_r' # automate this
            
            # print(timestep, params['exo_liq'], action['asset_id'] )
    ############ CHOOSE COMPOSITE ACTION TYPE  #############################

    if timestep == 2:
            params['exo_trade'] = ACTION_LIST[0] # automate this
            params['exo_liq'] = ACTION_LIST[0]
            action['asset_id'] = 'i'
    elif timestep == 990:
            params['exo_trade'] = ACTION_LIST[4] # automate this
            params['exo_liq'] = ACTION_LIST[4]
            action['asset_id'] = 'i'
            # print('---------------------------------------------------')
            # print('timestep', timestep)
    else:
        list_index = timestep % 3 + 1
        params['exo_trade'] = ACTION_LIST[list_index]
        params['exo_liq'] = ACTION_LIST[list_index]
    ########## TEMP TEST SELL Q FOR R ############
    ####### AGENT 0 ######################
    if params['exo_trade'] == 'test_q_for_r':
        action['q_sold'] = 1000
        action['action_id'] = 'Ri_Purchase'
        # temp choose first agent
        action['agent_id'] = prev_state['uni_agents']['m'][0]
        if action['asset_id'] == 'j':
            action['agent_id'] = prev_state['uni_agents']['m'][0]
            action['q_sold'] = 1000
    ###############################################

    ########## TEMP TEST SELL Q FOR R ############
    ####### AGENT 1 ######################
    if params['exo_trade'] == 'test_r_for_q':
        action['ri_sold'] = 1000
        action['action_id'] = 'Q_Purchase'
        # temp choose first agent
        action['agent_id'] = prev_state['uni_agents']['m'][1]
        if action['asset_id'] == 'j':
            action['agent_id'] = prev_state['uni_agents']['m'][1]
            action['ri_sold'] = 1000
    ###############################################

    ########## TEMP TEST ADD LIQ ############
    ####### AGENT 2 ######################
    if params['exo_liq'] == 'test_add':
        action['ri_deposit'] = 50000
        action['action_id'] = 'AddLiquidity'
        # temp choose first agent
        action['agent_id'] = prev_state['uni_agents']['m'][2]
        if action['asset_id'] == 'j':
            action['agent_id'] = prev_state['uni_agents']['m'][6]
            action['ri_deposit'] = 50000
    ###############################################

    ########## TEMP TEST REMOVE LIQ ############
    ####### AGENT 3 ######################
    if params['exo_liq'] == 'test_remove':
        action['UNI_burn'] = 500
        # action['UNI_burn'] = 7071 # a = 1.5
        # action['UNI_burn'] = 35.36 # a = 0.5

        action['action_id'] = 'RemoveLiquidity'
        # temp choose first agent
        action['agent_id'] = prev_state['uni_agents']['m'][2]
        if action['asset_id'] == 'j':
            # print('remove j',step,action['asset_id'])
            action['agent_id'] = prev_state['uni_agents']['m'][6]
            action['UNI_burn'] = 500
    ###############################################

    ########## TEMP TEST SELL R FOR R ############
    ####### AGENT 5 ######################
    if params['exo_trade'] == 'test_r_for_r':
        action['ri_sold'] = 100
        action['action_id'] = 'R_Swap'
        action['purchased_asset_id'] = 'j'
        action['direction'] = 'ij'

        # temp choose first agent
        action['agent_id'] = prev_state['uni_agents']['m'][3]
        if action['asset_id'] == 'j':
            action['agent_id'] = prev_state['uni_agents']['m'][3]
            action['ri_sold'] = 50
            action['purchased_asset_id'] = 'i'
            action['direction'] = 'ji'


    ###############################################

    # print(step,action['asset_id'])
    # print(timestep, action)
    return action