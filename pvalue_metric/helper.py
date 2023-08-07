import itertools
from typing import Union
from pathlib import Path

import numpy as np
import pandas as pd

subject_group = "dx_group"

#you should make sure there is no empty cell in the target column

def get_data(file_name:Union[Path, pd.DataFrame], target_column: str, target_groups:list) -> tuple:
    
    if isinstance(file_name, Path):
        df = pd.read_csv(file_name)
    elif isinstance(file_name, pd.DataFrame):
        df = file_name

    data_list = []
    for group in target_groups:
        data_list.append(tuple(df[target_column].loc[df[subject_group] == group]))

    return tuple(data_list)

def bootstrapped_cohorts(data:list, n:int=1000) -> list:
    
    cohort_list = []
    for group in data:
        bootstrapped = np.zeros((n,len(group)))
        for i in range(n):
            bootstrapped[i] = np.random.choice(group, len(group), replace=True)
        
        cohort_list.append(bootstrapped)

    return cohort_list

def permutated_cohorts(data:tuple, n:int=1000) -> list:

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

