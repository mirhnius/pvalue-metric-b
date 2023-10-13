import numpy as np
import pandas as pd
from pathlib import Path
from itertools import product
from pvalue_metric import metric


def simulation(test_func, generator1, generator2, n_bootstrap, n_permutation, func1_args={}, func2_args={}, **kwargs):
    
    g1_samples = generator1(**func1_args)
    g2_samples = generator2(**func2_args)
    _, p = test_func(g1_samples, g2_samples, **kwargs)
    p_metric = metric.pvalue_test([g1_samples, g2_samples],test_func, n_bootstrap, n_permutation, **kwargs)[0][0]

    return {'pvalue': p, 'p_metric': p_metric}

if __name__ == "__main__":
    #chang it from hard coded to command line input

    n_bootstrap = [500]
    n_permutation = [500]
    scale = [1]
    size = [15, 30, 50, 100]
    locations = [0, 0.5, 1, 1.5]

    columns = ['size', 'locations', 'scale',  'n_bootstrap', 'n_permutation']
    combinations = list(product(size, locations, scale, n_bootstrap, n_permutation))
    
    combinations_df = pd.DataFrame(combinations, columns=columns)
    combinations_df.to_csv(Path(__file__).parent.absolute() / 'simulation_combinations.csv')
    




