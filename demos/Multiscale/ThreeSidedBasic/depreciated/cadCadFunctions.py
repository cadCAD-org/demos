'''
cadCAD helper functions.
Individual functions developed by Michael Zargham, Matthew Barlin, and Andrew Clark.
'''

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def aggregate_runs(df,aggregate_dimension):
    '''
    Function to aggregate the monte carlo runs along a single dimension.

    Parameters:
    df: dataframe name
    aggregate_dimension: the dimension you would like to aggregate on, the standard one is timestep.

    Example run:
    mean_df,median_df,std_df,min_df = aggregate_runs(df,'timestep')
    '''
    aggregate_dimension = aggregate_dimension

    mean_df = df.groupby(aggregate_dimension).mean().reset_index()
    median_df = df.groupby(aggregate_dimension).median().reset_index()
    std_df = df.groupby(aggregate_dimension).std().reset_index()
    min_df = df.groupby(aggregate_dimension).min().reset_index()

    return mean_df,median_df,std_df,min_df

def plot_averaged_runs(df,aggregate_dimension,x, y,run_count,lx=False,ly=False, suppMin=False):
    '''
    Function to plot the mean, median, etc of the monte carlo runs along a single variable.

    Parameters:
    df: dataframe name
    aggregate_dimension: the dimension you would like to aggregate on, the standard one is timestep.
    x = x axis variable for plotting
    y = y axis variable for plotting
    run_count = the number of monte carlo simulations
    lx = True/False for if the x axis should be logged
    ly = True/False for if the x axis should be logged
    suppMin: True/False for if the miniumum value should be plotted

    Note: Run aggregate_runs before using this function

    Example run:
    plot_averaged_runs('timestep', 'revenue',100, suppMin=True)

    '''
    mean_df,median_df,std_df,min_df = aggregate_runs(df,aggregate_dimension)

    plt.figure(figsize=(10,6))
    if not(suppMin):
        plt.plot(mean_df[x].values, mean_df[y].values,
             mean_df[x].values,median_df[y].values,
             mean_df[x].values,mean_df[y].values+std_df[y].values,
             mean_df[x].values,min_df[y].values)
        plt.legend(['mean', 'median', 'mean+ 1*std', 'min'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    else:
        plt.plot(mean_df[x].values, mean_df[y].values,
             mean_df[x].values,median_df[y].values,
             mean_df[x].values,mean_df[y].values+std_df[y].values,
             mean_df[x].values,mean_df[y].values-std_df[y].values)
        plt.legend(['mean', 'median', 'mean+ 1*std', 'mean - 1*std'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.xlabel(x)
    plt.ylabel(y)
    title_text = 'Performance of ' + y + ' over all of ' + str(run_count) + ' Monte Carlo runs'
    plt.title(title_text)
    if lx:
        plt.xscale('log')

    if ly:
        plt.yscale('log')


def first_five_plot(df,aggregate_dimension,x,y,run_count):
    '''
    A function that generates timeseries plot of at most the first five Monte Carlo runs. 

    Parameters:
    df: dataframe name
    aggregate_dimension: the dimension you would like to aggregate on, the standard one is timestep.
    x = x axis variable for plotting
    y = y axis variable for plotting
    run_count = the number of monte carlo simulations

    Note: Run aggregate_runs before using this function
    Example run:
    first_five_plot(df,'revenue',100)
    '''
    mean_df,median_df,std_df,min_df = aggregate_runs(df,aggregate_dimension)
    plt.figure(figsize=(10,6))
    if run_count < 5:
        runs = run_count
    else:
        runs = 5
    for r in range(1,runs+1):
        legend_name = 'Run ' + str(r)
        plt.plot(df[df.run==r].timestep, df[df.run==r][y], label = legend_name )
    plt.plot(mean_df[x], mean_df[y], label = 'Mean', color = 'black')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel(x)
    plt.ylabel(y)
    title_text = 'Performance of ' + y + ' over the First ' + str(runs) + ' Monte Carlo Runs'
    plt.title(title_text)
