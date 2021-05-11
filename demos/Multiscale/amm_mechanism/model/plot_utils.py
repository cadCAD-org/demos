import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy

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

def slippage_plot(experiments,test_title, T, asset_id_list):
    """
    Plot relative liquidity change- delta S for each asset
    """
    asset_S = {k:[] for k in asset_id_list}
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)
    dR = 0
    for asset_id in asset_S:
        for i in range(df.substep.max(),T, df.substep.max()): 
            S = df.pool[i].pool[asset_id]['S']
            R = df.pool[i].pool[asset_id]['R']
            # need to get diff here
            # dR = R - df.pool[i].pool[asset_id]['R']

            # asset_S[str(asset_id)].append(S*dR/R)
            asset_S[str(asset_id)].append(S/R)



    i_in_j = [j / i - 1 for i,j in zip(*asset_S.values())]

    # print(asset_P)
    plt.figure(figsize=(12, 8))
    # for asset_id in asset_id_list:

    #     value_df = pd.DataFrame(asset_S[asset_id])
    #     value_df = value_df.pct_change()
    #     value_df.iloc[0] = 0
    #     # print(value_df)
    #     plt.plot(value_df,label='Asset '+ asset_id, marker='o')
    plt.plot(i_in_j,label='Slippage '+ str(asset_id_list), marker='o')
  
    plt.legend()
    plt.title(test_title + ' for Asset ' + str(asset_id_list))
    plt.xlabel('Timestep')
    plt.ylabel('Asset Liquidity Change')

    plt.show()

def IL_plot(experiments,test_title, periods):
    
    df = experiments.copy()
    df = df[df['substep'] == df.substep.max()]
    df.fillna(method='ffill',inplace=True)
 
    plt.figure(figsize=(12, 8))



    UNI_IL_i = 2* np.sqrt(np.abs(df.UNI_P_RQi.pct_change(periods))) / (1 + df.UNI_P_RQi.pct_change(periods)) - 1
    UNI_IL_j = 2* np.sqrt(np.abs(df.UNI_P_RQj.pct_change(periods))) / (1 + df.UNI_P_RQj.pct_change(periods)) - 1
    
    plt.plot(UNI_IL_i,label='Asset i', marker='o')
    plt.plot(UNI_IL_j,label='Asset j',marker='o')
    plt.legend()
    plt.title(test_title + str(periods))
    plt.xlabel('Timestep')
    plt.ylabel('Windowed Delta Price Ratio')
    plt.show()

def rel_price_plot(experiments,test_title, asset_id_list):
    """
    asset_id_list is an asset pair only to view relative prices
    """
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    reserve_asset_in = df['UNI_ij']
    reserve_asset_out = df['UNI_ji']
    asset_price_in = df['UNI_P_RQi']
    asset_price_out = df['UNI_P_RQj']
    asset_weight_in = df['UNI_Si']
    asset_weight_out = df['UNI_Sj']

    # Compute percent change in reserve
    reserve_in_pct_change = reserve_asset_in.pct_change()
    reserve_out_pct_change = reserve_asset_out.pct_change()

    # Compute price of OUT asset in terms of IN asset
    price_out_for_in = asset_price_in / asset_price_out

    # Compute percent change in price (OUT per IN)
    price_pct_change = price_out_for_in.pct_change()

    # Slippage calculation #1: elasticity of price with respect to transactions size
    elasticity = price_pct_change / reserve_in_pct_change

    # Slippage calculation #2: percentage difference between effective and spot price
    slippage = ( (reserve_in_pct_change / reserve_asset_in) / (reserve_out_pct_change / reserve_asset_out) * (asset_weight_in / asset_weight_out) - 1 )
    plt.figure(figsize=(20,6))
    plt.subplot(131)
    plt.plot(price_pct_change,label='Price Change '+ asset_id_list, marker='o')
    plt.legend()
    plt.xlabel('Timestep')

    plt.subplot(132)
    plt.plot(elasticity,label='Price Elasticity '+ asset_id_list, marker='o')
    plt.legend()
    plt.xlabel('Timestep')

    plt.subplot(133)   
    plt.plot(slippage,label='Price Slippage '+ asset_id_list, marker='o')
    plt.legend()
    plt.xlabel('Timestep')
    plt.ylabel('Price Change')

    plt.suptitle(test_title)
    plt.show()

def rel_price_plot_single(experiments,test_title, asset_id_list):
    """
    asset_id_list is an asset pair only to view relative prices
    """
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    reserve_asset_in = df['UNI_Ri']
    reserve_asset_out = df['UNI_Qi']
    asset_price_in = df['UNI_P_RQi']
    asset_price_out = df['UNI_P_RQj']
    asset_weight_in = df['UNI_Si']
    asset_weight_out = df['UNI_Sj']

    # Compute percent change in reserve
    reserve_in_pct_change = reserve_asset_in.pct_change()
    reserve_out_pct_change = reserve_asset_out.pct_change()

    # Compute price of OUT asset in terms of IN asset
    price_out_for_in = asset_price_in / asset_price_out

    # Compute percent change in price (OUT per IN)
    price_pct_change = price_out_for_in.pct_change()

    # Slippage calculation #1: elasticity of price with respect to transactions size
    elasticity = price_pct_change / reserve_in_pct_change

    # Slippage calculation #2: percentage difference between effective and spot price
    slippage = ( (reserve_in_pct_change / reserve_asset_in) / (reserve_out_pct_change / reserve_asset_out) * (asset_weight_in / asset_weight_out) - 1 )
    plt.figure(figsize=(20,6))
    plt.subplot(131)
    plt.plot(price_pct_change,label='Price Change '+ asset_id_list, marker='o')
    plt.legend()
    plt.xlabel('Timestep')

    plt.subplot(132)
    plt.plot(elasticity,label='Price Elasticity '+ asset_id_list, marker='o')
    plt.legend()
    plt.xlabel('Timestep')

    plt.subplot(133)   
    plt.plot(slippage,label='Price Slippage '+ asset_id_list, marker='o')
    plt.legend()
    plt.xlabel('Timestep')
    plt.ylabel('Price Change')

    plt.suptitle(test_title)
    plt.show()

def param_test_plot(experiments, config_ids, swept_variable, y_variable, *args):
    """
    experiments is the simulation result dataframe.
    config_ids is the list configs executed upon in the simulation.
    swept_variable is the key (string) in config_ids that was being tested against.
    y_variable is the state_variable (string) to be plotted against default timestep.

    *args for plotting more state_variables (string).
    """
    experiments = experiments.sort_values(by =['subset']).reset_index(drop=True)
    cols = 1
    rows = 1
    cc_idx = 0
    while cc_idx<len(experiments):
        cc = experiments.iloc[cc_idx]['subset']

        cc_label = experiments.iloc[cc_idx]['subset']

        secondary_label = [item['M'][swept_variable] for item in config_ids if  item["subset_id"]== cc_label]
        sub_experiments = experiments[experiments['subset']==cc]
        cc_idx += len(sub_experiments)
        fig, axs = plt.subplots(ncols=cols, nrows=rows, figsize=(15*cols,7*rows))

        df = sub_experiments.copy()
        colors = ['orange', 'g', 'magenta', 'r', 'k' ]

        ax = axs
        title = swept_variable + ' Effect on ' + y_variable + '\n' + 'Scenario: ' + str(secondary_label[0]) + ' ' + swept_variable
        # + 'Scenario: ' + str(cc_label)  + ' rules_price'
        ax.set_title(title)
        ax.set_ylabel('Funds')

        df.plot(x='timestep', y=y_variable, label=y_variable, ax=ax, legend=True, kind ='scatter')

        for count, arg in enumerate(args):
            df.plot(x='timestep', y=arg, label=arg, ax=ax, legend=True, color = colors[count], kind ='scatter')

        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax.set_xlabel('Timesteps')
        ax.grid(color='0.9', linestyle='-', linewidth=1)

        plt.tight_layout()
            
    fig.tight_layout(rect=[0, 0, 1, .97])
    fig.patch.set_alpha(1)
    plt.close()
    return display(fig)

def param_fan_plot(experiments, config_ids, swept_variable, y_variable, *args):
    """
    experiments is the simulation result dataframe.
    config_ids is the list configs executed upon in the simulation.
    swept_variable is the key (string) in config_ids that was being tested against.
    y_variable is the state_variable (string) to be plotted against default timestep.

    *args for plotting more state_variables (string).
    """
    experiments = experiments.sort_values(by =['subset']).reset_index(drop=True)
    cols = 1
    rows = 1
    cc_idx = 0
    while cc_idx<len(experiments):
        cc = experiments.iloc[cc_idx]['subset']

        cc_label = experiments.iloc[cc_idx]['subset']

        secondary_label = [item['M'][swept_variable] for item in config_ids if  item["subset_id"]== cc_label]
        sub_experiments = experiments[experiments['subset']==cc]
        cc_idx += len(sub_experiments)
        fig, axs = plt.subplots(ncols=cols, nrows=rows, figsize=(15*cols,7*rows))

        df = sub_experiments.copy()
        df = df.groupby('timestep').agg({y_variable: ['min', 'mean', 'max']}).reset_index()
        colors = ['orange', 'g', 'magenta', 'r', 'k' ]

        ax = axs
        title = swept_variable + ' Effect on ' + y_variable + '\n' + 'Scenario: ' + str(secondary_label[0]) + ' ' + swept_variable
        # + 'Scenario: ' + str(cc_label)  + ' rules_price'
        ax.set_title(title)
        ax.set_ylabel('Funds')

        df.plot(x='timestep', y=(y_variable,'mean'),label = y_variable, ax=ax, legend=True)

        ax.fill_between(df.timestep, df[(y_variable,'min')], df[(y_variable,'max')], alpha=0.5)        
        ax.set_xlabel('Blocks')
        ax.grid(color='0.9', linestyle='-', linewidth=1)

        plt.tight_layout()
            
    fig.tight_layout(rect=[0, 0, 1, .97])
    fig.patch.set_alpha(1)
    plt.close()
    return display(fig)