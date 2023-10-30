import numpy as np
# from pvalue_metric import helper
import helper

NonePath = type('NonePath', (), {'resolve': lambda: None})


def mean_euclidean_distance(pvalues:np.array):
    """
    This function calculates the mean euclidean distance between the CDF of the generated pvalues and
    the uniform CDF function(null p value distribution).

    Input:
        pvalues: numpy array of generated pvalues

    Output:
        mean euclidean distance between the CDF of the generated pvalues and
        the uniform CDF function.
    """

    try:
        assert(len(np.unique(pvalues)) == len(pvalues))
    except AssertionError:
        print("pvalues assumed to be unique (because of the CDF is calculated")
        raise

    n_bootstrap = len(pvalues)
    p_CDF = np.arange(1, n_bootstrap+1) / n_bootstrap #CDF function for  bootstrap pvalues
    sorted_pvalues = np.sort(pvalues)
    
    euclidean_distances = np.zeros((n_bootstrap,))
    for (i,p) in enumerate(sorted_pvalues):
        euclidean_distances[i] = np.power(p_CDF[i] - p, 2)  # for uniform  F(p) = p

    return np.mean(euclidean_distances)


def CDF_test(deltas, original_delta):
    """
    This function does the permutation CDF test to check if original cohort's delta
    is significantly different from the generated deltas by permutation.

    Inputs:
        deltas: numpy array of generated deltas
        original_delta: delta of the original cohort

    Outputs:
        pvalue: pvalue of the test
        delta_CDF: CDF of the generated deltas
        threshold_index: index of the threshold in the sorted deltas
    """

    n = len(deltas)
    sorted_deltas = np.sort(deltas)
    delta_CDF = np.arange(1,n+1) / n

    #add exception here or use scipy to find the index
    threshold__list =  np.ravel(np.where((sorted_deltas > original_delta) | (sorted_deltas == original_delta)))
    threshold_index  = threshold__list[0] if len(threshold__list) > 0 else n - 1

    return delta_CDF[-1] - delta_CDF[threshold_index], delta_CDF, threshold_index


def original_cohort_properties(data, Hypothesis_testing_func, n_bootstrap, **kwargs):

    original_cohort_G1_bootstrapes, original_cohort_G2_bootstrapes = \
        helper.bootstrapped_cohorts(data, n_bootstrap)
     
    original_cohort_bootstrap_pvalues = [Hypothesis_testing_func(original_cohort_G1_bootstrapes[i],\
                                original_cohort_G2_bootstrapes[i], **kwargs)[1] for i in range(n_bootstrap)]

    original_delta = mean_euclidean_distance(original_cohort_bootstrap_pvalues)

    return original_delta, original_cohort_bootstrap_pvalues


#should change the name of mean_delta and might add a function for original delta calculation
def pvalue_test(data, Hypothesis_testing_func, n_bootstrap, n_permutation, path=NonePath, name=None, **kwargs):
    """
    This function calculate pmetric for a given data (two set of groups)
    and Hypothesis testing function

    Inputs:
        data: list of data, each element of the list is a tuple of data for each target group
        Hypothesis_testing_func: Hypothesis testing function
        n_bootstrap: number of bootstrap iteration
        n_permutation: number of permutation iterations
        **kwargs: keyword arguments for the Hypothesis testing function

    Outputs:
        CDF_test function's outputs:
            pvalue: pvalue of the test
            delta_CDF: CDF of the generated deltas
            threshold_index: index of the threshold in the sorted deltas
        original_mean_delta: mean delta of the original cohort
    """

    G1_permutations, G2_permutations = helper.permutated_cohorts(data, n_permutation)

    mean_deltas = np.zeros((n_permutation,))
    all_bootstrapes = np.zeros((n_permutation, n_bootstrap))
    for permutation_itr in range(n_permutation):

        G1_bootstraps, G2_bootstraps = helper.bootstrapped_cohorts([G1_permutations[permutation_itr], G2_permutations[permutation_itr]],
         n_bootstrap)
        p_values = np.zeros((n_bootstrap,))

        for bootstrap_itr in range(n_bootstrap):
            p_values[bootstrap_itr] = Hypothesis_testing_func(G1_bootstraps[bootstrap_itr],\
                                                G2_bootstraps[bootstrap_itr], **kwargs)[1]
        
        mean_deltas[permutation_itr] = mean_euclidean_distance(p_values)
        all_bootstrapes[permutation_itr] = p_values[bootstrap_itr]

    original_mean_delta, original_cohort_pvalues = original_cohort_properties(data, \
                                    Hypothesis_testing_func, n_bootstrap, **kwargs)
    if path.resolve() != None:
        np.savetxt(path / f"permeuted_cohorts_pvalues_{name}.txt", all_bootstrapes)
        np.savetxt(path / f"original_cohort_pvalues_{name}.txt", original_cohort_pvalues)
      
    return CDF_test(mean_deltas, original_mean_delta), original_mean_delta

   