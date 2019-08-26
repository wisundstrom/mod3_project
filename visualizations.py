"""
This module is designed for final visualization code.
"""
# import all the necessory python packages
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

def create_sample_dists(df, y_var=None, x_var=None, categories=[], samplesize=30, numsamples=400):
    np.random.seed(5)
    """
    takes the sample data and retun a list of sample distributions 
    """
#     df = cleaned_data
    
    dflist = []
    
    for cat in categories:
        dftemp = df.loc[ df[x_var].str.contains(cat)][y_var]
        sampler = np.random.choice(dftemp ,size=(samplesize,numsamples))
        sample_prop = sampler.mean(axis=0)
        dflist.append(sample_prop)
    
    return dflist


def overlapping_density(package=None, input_vars=None, target_vars=None, categories=None, output_image_name=None):
    """ 
    Set the characteristics of your overlapping density plot and returns fig
    """

    # Set size of figure
    fig = plt.figure(figsize=(16, 10), dpi=80)
    sns.set(color_codes=True)

    # Starter code for figuring out which package to use
    if package == "sns":
        for counter,value in enumerate(input_vars):
            sns.kdeplot(value, label=categories[counter],shade=True)
            plt.title('Overlapping mean desnsity', fontsize=large)#, figure = fig)
            plt.legend('xyz', fontsize=med)
            plt.xlabel('Means', fontsize=med)#, figure = fig)
            plt.ylabel('Sample counts', fontsize=med)#, figure = fig)
         
            plt.xticks(fontsize=med)
            plt.yticks(fontsize=med)
            
    elif package == 'matplotlib':
        for variable in input_vars:
            plt.plot(variable, label=None, linewidth=None, color=None, figure = fig)


#     plt.savefig(f'img/{output_image_name}.png', transparent = True, figure = fig)
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
    takes the dataframe and returns a plot
    """
    # plot graph
    df.groupby([input_vars,target_vars]).size().unstack().plot(kind='bar',stacked=True)
    row_keys = df[input_vars].unique()
    plt.xlabel('Vehicles colors', fontsize=med)#, figure = fig)
    plt.ylabel('Citation rates', fontsize=med)#, figure = fig)
    plt.title('Commercial vehicles', fontsize=large)#, figure = fig)
    plt.xticks(np.arange(len(row_keys)),row_keys, fontsize=med)#,rotation=0
#      plt.xticks(fontsize=med)
    plt.yticks(fontsize=med)
    
  
    
#     return fig
    

def color_plot(arr,categories=None, output_image_name=None):
    arr_list = np.asarray(arr).mean(axis=1)
    arr_lst = np.vstack((arr_list, 1-arr_list))
    df = pd.DataFrame(arr_lst.T)
    df.plot(kind='bar',stacked=True)
#     sns.set(color_codes=True)
    plt.xlabel('Vehicle makes', fontsize=med)
    plt.ylabel('Citation rates', fontsize=med)
    plt.title('Ticketed vs Non-Ticketed vehicle colors')
    plt.xticks(np.arange(4),categories,rotation=0)#, fontsize=med) 
    plt.legend(labels=['Ticketed','Non-Ticketed'])
    
    
#     plt.savefig(f'img/{output_image_name}.png', transparent = True)#, figure = fig)

    pass

def visualization_three(output_image_name):
    pass

def visualization_four(output_image_name):
    pass
