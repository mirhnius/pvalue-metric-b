import numpy as np
import pnadas as pd
from scipy import stats
from pathlib import Path
from pvlaue_metric import metric

def test_for_all_volumes(path:Path,
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
    for region in regions:
        tests_outputs, _ = metric.pvalue_test(data, n_bootstrap, n_permutation, **kwargs)
        pvalue, _, _ = tests_outputs
        

