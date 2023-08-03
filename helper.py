import numpy as np
import pandas as pd
from pathlib import Path
subject_group = "dx_group"

#you should make sure there is no empty cell in the target column

def get_data(path:Path, target_column: str, target_groups:list):

    df = pd.read_csv(path)
    data_list = []
    for group in target_groups:
        data_list.append(tuple(df[target_column].loc[df[subject_group] == group]))

    return tuple(data_list)



