"""
This module is for your data cleaning.
It should be repeatable.

## PRECLEANING
There should be a seperate script recording how you transformed the json api calls into a dataframe and csv.

## SUPPORT FUNCTIONS
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd

def support_function_one():
    pass

def support_function_two():
    pass

def support_function_three():
    pass


def full_clean(dirty_dala):
    """
    This is the one function called that will run all the support functions.
    :param dirty_dala: should be a saved csv
    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    cleaning_data = support_function_one(dirty_data)
    cleaning_data2 = support_function_two(cleaning_data1)
    cleaned_data= support_function_three(cleaning_data2)
    cleaned_data.to_csv('./data/cleaned_for_testing.csv')
    return cleaned_data
