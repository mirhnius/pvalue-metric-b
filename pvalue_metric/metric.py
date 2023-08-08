import numpy as np
from pvalue_metric import helper

def mean_euclidean_distance(pvalues:np.array):

    n_bootstrap = len(pvalues)
    uniform_CDF = np.cumsum(np.ones((len(pvalues)))) / n_bootstrap
    p_CDF = np.cumsum(np.sort(pvalues)) / np.sum(pvalues)

    return np.mean(np.power(p_CDF - uniform_CDF, 2))

def CDF_test(deltas, original_delta):
    
    sorted_deltas = np.sort(deltas)
    delta_CDF = np.cumsum(sorted_deltas) / np.sum(deltas)
    #add exception here or use scipy to find the index
    threshold__list =  np.ravel(np.where((sorted_deltas > original_delta) | (sorted_deltas == original_delta)))
    threshold_index  = threshold__list[0] if len(threshold__list) > 0 else len(delta_CDF) - 1

    return delta_CDF[-1] - delta_CDF[threshold_index], delta_CDF, threshold_index

def pvalue_test(data, Hypothesis_testing_func, n_bootstrap, n_permutation, **kwargs):

    G1_permutations, G2_permutations = helper.permutated_cohorts(data, n_permutation)

    mean_deltas = np.zeros((n_permutation,))
    for permutation_itr in range(n_permutation):
        G1_bootstraps, G2_bootstraps = helper.bootstrapped_cohorts([G1_permutations[permutation_itr], G2_permutations[permutation_itr]], n_bootstrap)
        p_values = np.zeros((n_bootstrap,))

        for bootstrap_itr in range(n_bootstrap):
            p_values[bootstrap_itr] = Hypothesis_testing_func(G1_bootstraps[bootstrap_itr],\
                                                G2_bootstraps[bootstrap_itr], **kwargs)[1]

        mean_deltas[permutation_itr] = mean_euclidean_distance(p_values)

    original_cohort_G1_bootstrapes, original_cohort_G2_bootstrapes = \
        helper.bootstrapped_cohorts(data, n_bootstrap)
     
    original_cohort_pvalues = [Hypothesis_testing_func(original_cohort_G1_bootstrapes[i],\
                                original_cohort_G2_bootstrapes[i], **kwargs)[1] for i in range(n_bootstrap)]

    original_mean_delta = mean_euclidean_distance(original_cohort_pvalues)
    
    return CDF_test(mean_deltas, original_mean_delta), original_mean_delta

   