import numpy as np
import pnadas as pd
from scipy import stats
from pathlib import Path
from pvlaue_metric import metric


group_column = "dx_group"

def pvalue_test_for_all_volumes(path:Path,
                        regions:list(str),
                        groups:list,
                        n_bootstrap:int,
                        n_permutation:int,
                        **kwargs) -> pd.DataFrame:

    try:
        assert len(groups) == 2
    except AssertionError:
        print("Only two groups are allowed for now")
        raise

    data = pd.dataframe(path)
    results = np.zeros((len(regions),)) 
       
    for (i, region) in enumerate(regions):

        data_columns = []
        for group in groups:
            data_columns.append(data[region].loc[data[group_column] == group])

        data_columns = tuple(data_columns)
    
        tests_outputs, _ = metric.pvalue_test(data_columns, n_bootstrap, n_permutation, **kwargs)
        results[i], _, _ = tests_outputs
        # pandas.Series(data=None, index=None, dtype=None, name=None, copy=None, fastpath=False)[source]

    return pd.Series(results, index=regions, name= group[0] + "_vs_" + group[1]))    #maybe change name  


