"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
from scipy import stats
import math
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison



def create_sample_dists(cleaned_data, y_var=None, x_var=None, categories=[], samplesize=50, numsamples=50):
    np.random.seed(0)
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

def compare_pval_alpha(p_val, alpha):
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status


def hypothesis_test_one(cleaned_data, alpha = .05):
    """
    This function takes in cleaned data, then uses create sample dists to grab the required
    categories. From there the function perfoms an Anova on the groups and returns whether or
    not to reject he null
    :param alpha: the critical value of choice
    :param cleaned_data: our cleaned dataset
    :return:
    """
    # Get data for tests
    comparison_groups = create_sample_dists(cleaned_data, y_var='ticket', x_var='color', categories=['BLACK','WHITE','RED','BLUE', 'GRAY', 'SILVER'])

    ###
    # perform f test (ANOVA) on the groups
    ###
    F, p = stats.f_oneway(comparison_groups[0],comparison_groups[1],comparison_groups[2],comparison_groups[3],comparison_groups[4],comparison_groups[5])
    p_val=p
    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference in citation rate between these colors')
    pass
#     if assertion == 'can':
#         print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
#     else:
#         print(".")

#     return status

def hypothesis_test_two(cleaned_data, alpha = .05):
    """
    This function takes in cleaned data, then uses create sample dists to grab the required
    categories. From there the function performs tukeys HSD analysis and displays a chart of all
    the pairwise compairisons and their signifigance
    :param alpha: the critical value of choice
    :param cleaned_data: our cleaned dataset
    :return:
    """
    #Get data for tests
    categories=['BLACK','WHITE','RED','BLUE', 'GRAY', 'SILVER']
    comparison_groups = create_sample_dists(cleaned_data, y_var='ticket', x_var='color', categories=categories )
    list_for_tukey=[]
    for i in range(len(categories)):
        cat_list=[categories[i]] * 50
        tktemp=zip(list(comparison_groups[i]),cat_list)
        list_for_tukey += list(tktemp)
    
    df_tukey =pd.DataFrame(list_for_tukey) 
    
    ###
    # perform tukeys HSD for the groups
    ###
    mc = MultiComparison(df_tukey[0], df_tukey[1])
    result = mc.tukeyhsd()
    # we need to convert the simpletable from the tukey result object into a dataframe
    result_summary = result.summary().as_html()
    tukey_df= pd.read_html(result_summary, header=0, index_col=0)[0]
    tukey_df.columns = ["Second Color","Mean Difference","Min Difference", "Max Difference", "Signifigant Difference?"]
    tukey_df.index.names = ['First Color']
    
    return tukey_df

def hypothesis_test_three(cleaned_data, alpha= .05):
    """
    This function takes in cleaned data, then uses create sample dists to grab the required
    categories. From there the function perfoms an Anova on the groups and returns whether or
    not to reject he null
    :param alpha: the critical value of choice
    :param cleaned_data: our cleaned dataset
    :return:
    """
    # Get data for tests
    comparison_groups = create_sample_dists(cleaned_data, y_var='ticket', x_var='make', categories=['NISS','FORD','HOND','TOY'], samplesize=50, numsamples=50)

    ###
    # perform f test (ANOVA) on the groups
    ###
    F, p = stats.f_oneway(comparison_groups[0],comparison_groups[1],comparison_groups[2],comparison_groups[3])
    p_val=p
    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference in citation rate between these colors')

#     if assertion == 'can':
#         print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
#     else:
#         print(".")

#     return status

    pass

def hypothesis_test_four(cleaned_data, alpha = .05):
    """
    This function takes in cleaned data, then uses create sample dists to grab the required
    categories. From there the function performs tukeys HSD analysis and displays a chart of all
    the pairwise compairisons and their signifigance
    :param alpha: the critical value of choice
    :param cleaned_data: our cleaned dataset
    :return:
    """
    #Get data for tests
    categories=['NISS','FORD','HOND','TOY']
    comparison_groups = create_sample_dists(cleaned_data, y_var='ticket', x_var='make', categories=categories )
    list_for_tukey=[]
    for i in range(len(categories)):
        cat_list=[categories[i]] * 50
        tktemp=zip(list(comparison_groups[i]),cat_list)
        list_for_tukey += list(tktemp)
    
    df_tukey =pd.DataFrame(list_for_tukey) 
    
    ###
    # perform tukeys HSD for the groups
    ###
    mc = MultiComparison(df_tukey[0], df_tukey[1])
    result = mc.tukeyhsd()
    # we need to convert the simpletable from the tukey result object into a dataframe
    result_summary = result.summary().as_html()
    tukey_df= pd.read_html(result_summary, header=0, index_col=0)[0]
    tukey_df.columns = ["Second Make","Mean Difference","Min Difference", "Max Difference", "Signifigant Difference?"]
    tukey_df.index.names = ['First Make']
    
    return tukey_df
