import numpy as np


def mean_euclidean_distance(pvalues:np.array):

    n_bootstrap = len(pvalues)
    uniform_CDF = np.cumsum(np.ones((len(pvalues)))) / n_bootstrap
    p_CDF = np.cumsum(np.sort(pvalues)) / np.sum(pvalues)

    return np.mean(np.power(p_CDF - uniform_CDF, 2))

def CDF_test(deltas, original_delta):
    
    sorted_deltas = np.sort(deltas)
    delta_CDF = np.cumsum(sorted_deltas) / np.sum(deltas)
    #add exception here or use scipy to find the index
    threshold_index = np.ravel(np.where((sorted_deltas > original_delta) | (sorted_deltas == original_delta)))[0]

    return 1 - delta_CDF[threshold_index]



