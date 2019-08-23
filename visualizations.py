"""
This module is for your final visualization code.
One visualization per hypothesis question is required.
A framework for each type of visualization is provided.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics as stats
import pylab as pl
import pandas as pd

# Set specific parameters for the visualizations
large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

def create_sample_dists(cleaned_data, y_var=None, x_var=None, categories=[], samplesize=30, numsamples=400):
    np.random.seed(5)
    """
    Each hypothesis test will require you to create a sample distribution from your data
    Best make a repeatable function
    :param cleaned_data:
    :param y_var: The numeric variable you are comparing
    :param categories: the categories whose means you are comparing
    :return: a list of sample distributions to be used in subsequent t-tests
    """
    df = cleaned_data
    
    dflist = []
    
    for cat in categories:
        dftemp = df.loc[ df[x_var].str.contains(cat)][y_var]
        sampler = np.random.choice(dftemp ,size=(samplesize,numsamples))
        sample_prop = sampler.mean(axis=0)
        dflist.append(sample_prop)
    
    return dflist


def overlapping_density(package=None, input_vars=None, target_vars=None, categories=None):
    """
    Set the characteristics of your overlapping density plot
    All arguments are set to None purely as a filler right now

    Function takes package name, input variables(categories), and target variable as input.
    Returns a figure

    Should be able to call this function in later visualization code.

    PARAMETERS

    :param package:        should only take sns or matplotlib as inputs, any other value should throw and error
    :param input_vars:     should take the x variables/categories you want to plot
    :param target_vars:    the y variable of your plot, what you are comparing
    :return:               fig to be enhanced in subsequent visualization functions
    """

    # Set size of figure
    fig = plt.figure(figsize=(16, 10), dpi=80)
    sns.set(color_codes=True)


    # Starter code for figuring out which package to use
    if package == "sns":
        for counter,value in enumerate(input_vars):
            sns.kdeplot(value, label=categories[counter],shade=True)
#             plt.axvline(stat.mean(value), color='green', linestyle='--', lw=2, label='sample mean')
            plt.xlabel('Means', fontsize=med)#, figure = fig)
            plt.ylabel('Sample counts', fontsize=med)#, figure = fig)
            plt.title('Overlapping mean desnsity', fontsize=large)#, figure = fig)
            plt.xticks(fontsize=med)
            plt.yticks(fontsize=med)
    elif package == 'matplotlib':
        for variable in input_vars:
            plt.plot(variable, label=None, linewidth=None, color=None, figure = fig)

#     return fig



def boxplot_plot(package=None, input_vars=None, target_vars=None):
    """
    Same specifications and requirements as overlapping density plot

    Function takes package name, input variables(categories), and target variable as input.
    Returns a figure

    PARAMETERS

    :param package:        should only take sns or matplotlib as inputs, any other value should throw and error
    :param input_vars:     should take the x variables/categories you want to plot
    :param target_vars:    the y variable of your plot, what you are comparing
    :return:               fig to be enhanced in subsequent visualization functions
    """
    plt.figure(figsize=(16, 10), dpi=80)

    pass


def commercial_ticket_plots(df, target_vars = None, input_vars= None, output_image_name=None):
    """
    The visualization functions are what is used to create each individual image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    # plot graph
    df.groupby([input_vars,target_vars]).size().unstack().plot(kind='bar',stacked=True)
    row_keys = df[input_vars].unique()
    plt.xlabel('Vehicles colors', fontsize=med)#, figure = fig)
    plt.ylabel('Stop counts', fontsize=med)#, figure = fig)
    plt.title('Commercial vehicles', fontsize=large)#, figure = fig)
    plt.xticks(np.arange(len(row_keys)),row_keys,rotation=0, fontsize=med)
#      plt.xticks(fontsize=med)
    plt.yticks(fontsize=med)
    plt.legend()
  
    
#     return fig
    
    ###

    # Starter code for labeling the image
#     plt.xlabel('Vehicles colors', figure = fig)
#     plt.ylabel('Stop counts', figure = fig)
#     plt.title('Commercial vehicles', figure= fig)
#     plt.legend()

    # exporting the image to the img folder
#     plt.savefig(f'img/{output_image_name}.png', transparent = True, figure = fig)
#     return fig


# please fully flesh out this function to meet same specifications of visualization one

def color_plot(arr,categories=None):#output_image_name):
    arr_list = np.asarray(arr).mean(axis=1)
    arr_lst = np.vstack((arr_list, 1-arr_list))
    df = pd.DataFrame(arr_lst.T)
    df.plot(kind='bar',stacked=True)
    plt.xlabel('Vehicles color', fontsize=med)
    plt.ylabel('Stop counts', fontsize=med)
    plt.title('Commercial vehicles')
    plt.xticks(np.arange(len(categories)),categories,rotation=0)#, fontsize=med)

    pass

def visualization_three(output_image_name):
    pass

def visualization_four(output_image_name):
    pass
