import numpy as np

from pvalue_metric import helper


def mean_euclidean_distance(pvalues:np.array):

    n_bootstrap = len(pvalues)
    uniform_CDF = np.cumsum(range(1, n_bootstrap+1)) / n_bootstrap
    p_CDF = np.cumsum(np.sort(pvalues)) / np.sum(pvalues)

    return np.mean(np.power(p_CDF - uniform_CDF, 2))


