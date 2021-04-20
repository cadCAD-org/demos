import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def agent_value_plot(experiments,test_title,T): #, agent_index, asset_id):
    """
This function plots agent values for each agent that went through the Uniswap World.
Values are token holdings multiplied by prices.
    """
    agent_h = []
    agent_r_i_out = []
    agent_s_i = []
    agent_r_j_out = []
    agent_s_j = []
    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    number_of_agents = 8
    for agent_index in range(number_of_agents):
        agent_h = []
        agent_r_i_out = []
        agent_s_i = []
        agent_r_j_out = []
        agent_s_j = []
    
        for i in range (0,T): 
            agent_h_list = []
            agent_h_list.append(df.uni_agents.values[i]['h'][agent_index])
            # agent_h.append(np.mean(agent_h_list))
            agent_h.append(agent_h_list)

            asset_id = 'i'
            agent_r_i_out_list= []
            agent_r_i_out_list.append(df.uni_agents.values[i]['r_' + asset_id + '_out'][agent_index])
            p_rq_list = []
            p_rq_list.append(df['UNI_P_RQ' + asset_id].values[i])
            agent_r_i_out.append(np.divide(agent_r_i_out_list,p_rq_list))
    
            agent_s_i_list= []
            s_i_pool = []
            q_reserve = []
            agent_s_i_list.append(df.uni_agents.values[i]['s_' + asset_id][agent_index])
            s_i_pool.append(df['UNI_S' + asset_id].values[i])
            q_reserve.append(df['UNI_S' + asset_id].values[i])        
            agent_s_i.append(np.multiply(np.divide(agent_s_i_list,s_i_pool),q_reserve))

            asset_id = 'j'
            agent_r_j_out_list= []
            agent_r_j_out_list.append(df.uni_agents.values[i]['r_' + asset_id + '_out'][agent_index])
            p_rq_list = []
            p_rq_list.append(df['UNI_P_RQ' + asset_id].values[i])
            agent_r_j_out.append(np.divide(agent_r_j_out_list,p_rq_list))
    
            agent_s_j_list= []
            s_j_pool = []
            q_reserve = []
            agent_s_j_list.append(df.uni_agents.values[i]['s_' + asset_id][agent_index])
            s_j_pool.append(df['UNI_S' + asset_id].values[i])
            q_reserve.append(df['UNI_S' + asset_id].values[i])        
            agent_s_j.append(np.multiply(np.divide(agent_s_j_list,s_j_pool),q_reserve))

        sub_total_i = np.add(agent_r_i_out,agent_s_i)
        sub_total_j = np.add(agent_r_j_out,agent_s_j)

        agent_total = np.add(np.add(sub_total_i,sub_total_j),agent_h)
        # print(agent_s_i)
        fig = plt.figure(figsize=(10, 5))
        plt.plot(range(0,T),agent_h,label='agent_h', marker='o')
        asset_id = 'i'
        plt.plot(range(0,T),agent_r_i_out,label='agent_r_' + asset_id + '_out',marker='o')
        plt.plot(range(0,T),agent_s_i,label='agent_s_' + asset_id,marker='o')
        asset_id = 'j'
        plt.plot(range(0,T),agent_r_j_out,label='agent_r_' + asset_id + '_out',marker='o')
        plt.plot(range(0,T),agent_s_j,label='agent_s_' + asset_id,marker='o')
        plt.plot(range(0,T),agent_total,label='agent_total',marker='o')

        plt.legend()
        plt.title(test_title + ' for Agent ' + str(agent_index))
        plt.xlabel('Timestep')
        plt.ylabel('Agent Holdings Value')
    plt.show()

def agent_plot(experiments,test_title,T):   #, agent_index, asset_id):
    """
This function plots asset holdings for each agent that went through the Uniswap World.
Asset holdings are token quantities held by the agent.
    """
    agent_h = []
    agent_r_i_out = []
    agent_r_i_in = []
    agent_s_i = []
    # asset_P = {k:[] for k in asset_id_list}

    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    number_of_agents = 8
    for agent_index in range(number_of_agents):
        agent_h = []
        agent_r_i_out = []
        agent_r_i_in = []
        agent_r_j_out = []
        agent_r_j_in = []
        for i in range (0,T): 
            agent_h_list = []
            agent_h_list.append(df.uni_agents.values[i]['h'][agent_index])
            agent_h.append(np.mean(agent_h_list))
            asset_id = 'i'
            agent_r_i_out_list= []
            agent_r_i_out_list.append(df.uni_agents.values[i]['r_' + asset_id + '_out'][agent_index])
            agent_r_i_out.append(np.mean(agent_r_i_out_list))
    
            agent_r_i_in_list= []
            agent_r_i_in_list.append(df.uni_agents.values[i]['r_' + asset_id + '_in'][agent_index])
            agent_r_i_in.append(np.mean(agent_r_i_in_list))
            
            asset_id = 'j'
            agent_r_j_out_list= []
            agent_r_j_out_list.append(df.uni_agents.values[i]['r_' + asset_id + '_out'][agent_index])
            agent_r_j_out.append(np.mean(agent_r_i_out_list))
    
            agent_r_j_in_list= []
            agent_r_j_in_list.append(df.uni_agents.values[i]['r_' + asset_id + '_in'][agent_index])
            agent_r_j_in.append(np.mean(agent_r_i_in_list))

        plt.figure(figsize=(10, 5))
        # plt.subplot(121)
        plt.plot(range(0,T),agent_h,label='agent_h', marker='o')
        asset_id = 'i'
        plt.plot(range(0,T),agent_r_i_out,label='agent_r_' + asset_id + '_out',marker='o')
        plt.plot(range(0,T),agent_r_i_in,label='agent_r_' + asset_id + '_in',marker='o')
        asset_id = 'j'
        plt.plot(range(0,T),agent_r_i_out,label='agent_r_' + asset_id + '_out',marker='o')
        plt.plot(range(0,T),agent_r_i_in,label='agent_r_' + asset_id + '_in',marker='o')
        plt.legend()
        plt.title(test_title + str(agent_index))
        plt.xlabel('Timestep')
        plt.ylabel('Tokens')
    plt.show()

def mean_agent_plot(experiments,test_title,T):
    """
This function shows mean agent holdings in the Uniswap World.
    """
    agent_h = []
    agent_r_i_out = []

    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    for i in range(df.substep.max(),T, df.substep.max()): 
        agent_h_list = []
        agent_h_list.append(df.uni_agents.values[i]['h'])
        agent_h.append(np.mean(agent_h_list))
        agent_r_i_out_list= []
        agent_r_i_out_list.append(df.uni_agents.values[i]['r_i_out'])
        agent_r_i_out.append(np.mean(agent_r_i_out_list))
  
    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(df.substep.max(),T, df.substep.max()),agent_h,label='agent_h', marker='o')
    plt.plot(range(df.substep.max(),T, df.substep.max()),agent_r_i_out,label='agent_r_i_out',marker='o')
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Tokens')
    plt.show()

def price_plot(experiments,test_title, price_swap, numerator, denominator):
    """
This function shows two plots of swap prices of two assets in the Uniswap World.
Once where fees are included and once without fees.
    """
      
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)
 
    plt.figure(figsize=(12, 8))
    
    token_ratio =  df[denominator]/ df[numerator]  
    plt.plot(df[price_swap],label='Swap Price', marker='o')
    plt.plot(token_ratio,label='Pool Ratio Price',marker='o')
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Price')
    plt.show()
