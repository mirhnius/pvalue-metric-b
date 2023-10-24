import itertools
from typing import Union
from pathlib import Path

import numpy as np
import pandas as pd

subject_group = "dx_group" #REMOVE IT FROM HERE add to function's inputs list

#you should make sure there is no empty cell in the target column

def get_data(file_name:Union[Path, pd.DataFrame], target_column: str, target_groups:list) -> tuple:

    """
    This function gets the data from a csv file or pandas dataframe and returns
    a tuple of data for each group

    Inputs:
        file_name: path to the csv file or pandas dataframe
        target_column: the column name of the target variable 
        target_groups: list of target groups that we are intrerested in

    Output:
        tuple of data, each element of the tuple is a tuple of data for each group
    """

    if isinstance(file_name, Path):
        df = pd.read_csv(file_name)
    elif isinstance(file_name, pd.DataFrame):
        df = file_name

    data_list = []
    for group in target_groups:
        data_list.append(tuple(df[target_column].loc[df[subject_group] == group]))

    return tuple(data_list)


def bootstrapped_cohorts(data:list, n:int=1000) -> list:
    """
    This function gets a list of data )and returns a list of bootstrapped data

    Inputs:
        data: list of data, each element of the list is a tuple of data for each target group
        n: number of bootstrap iterations

    Output:
        cohort_list: list of bootstrapped data, each element of the list is 
        a tuple of bootstrapped data for each target group
    """
    
    cohort_list = []
    for group in data:
        bootstrapped = np.zeros((n,len(group)))
        for i in range(n):
            bootstrapped[i] = np.random.choice(group, len(group), replace=True)
        
        cohort_list.append(bootstrapped)

    return cohort_list

def permutated_cohorts(data:tuple, n:int=1000) -> list:
    """
    This function gets a tuple of data and returns a list of permuted data

    Inputs:
        data: tuple of data, each element of the tuple is a tuple of data for each target group
        n: number of permutation iterations

    Output:
        permuted_cohorts: list of permuted data, each element of the list is 
        a tuple of permuted data for each target group
    """

    lengths = [len(group) for group in data]
    merged_data = tuple(itertools.chain(*data))

    permuted_cohorts = []
    for length in lengths:
        permuted_cohorts.append(np.zeros((n, length)))

    for i in range(n):
           permuted = np.random.permutation(merged_data)
           for (j, length) in enumerate(lengths):
               permuted_cohorts[j][i] = permuted[:length]
               permuted = permuted[length:]

    return permuted_cohorts

