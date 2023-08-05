import sys
import unittest
from pathlib import Path

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Put the pvalue_metric directory on the Python path.
PACKAGE_DIR = Path(__file__).parents[2]
sys.path.append(str(PACKAGE_DIR))

from pvalue_metric import metric


class TestMetric(unittest.TestCase):
    
    def test_mean_euclidean_distance(self):
        pvalues = np.array([0.3, 0.2, 0.1, 0.4])
        psum = np.cumsum(np.sort(pvalues))/np.sum(pvalues)
        uniform_CDF = np.cumsum(np.ones((len(pvalues)))) / len(pvalues)
        power = np.power(psum - uniform_CDF, 2)
        print("\npvalues: ", *pvalues)
        print("psums: ", *psum)
        print("uniform", *uniform_CDF)
        print("euclidean_distance: ", *power)
        
        self.assertEqual(metric.mean_euclidean_distance(pvalues), np.mean(power))

def plot_distance():
    pvalues = np.array([0.3, 0.2, 0.1, 0.4])
    psum = np.cumsum(np.sort(pvalues))/np.sum(pvalues)
    uniform_CDF = np.cumsum(np.ones((len(pvalues)))) / len(pvalues)
    plt.figure()
    plt.plot(psum)
    plt.plot(uniform_CDF)
    plt.show()

def plot_CDF_test():
    pvalues = np.array([[0.3, 0.2, 0.1, 0.4], [0.05, 0.01, 0.4, 0.6],\
                        [0.001, 0.2, 0.7, 0.49], [0.13, 0.52, 0.003, 0.45],\
                        [0.6, 0.28, 0.006, 0.4], [0.05, 0.01, 0.4, 0.6],[0.05, 0.001, 0.004, 0.16]])
    deltas = [metric.mean_euclidean_distance(pset)for pset in pvalues] 
    original_delta = metric.mean_euclidean_distance([0.03,0.001, 0.2, 0.3])
    sorted_deltas = np.sort(deltas)
    CDF_delta = np.cumsum(sorted_deltas) / np.sum(deltas)
    threshold_index = np.ravel(np.where((sorted_deltas > original_delta) | (sorted_deltas == original_delta)))[0]
    print(*sorted_deltas)
    print(original_delta)
    print(threshold_index)
    print(sorted_deltas[threshold_index] - original_delta)
    print(*CDF_delta)
    plt.plot(CDF_delta)
    plt.plot([threshold_index] * len(CDF_delta), list(range(len(CDF_delta))), 'r--')
    plt.show()

def pvalue_test_example():

    G1 = np.random.normal(0, 1, 100)
    G2 = np.random.normal(10, 1, 100)
    data = (G1, G2)
    outputs, original_delta = metric.pvalue_test(data, stats.ttest_ind, 500, 500)
    p, delta_cdf, threshold_index = outputs
    plt.plot(delta_cdf)
    plt.plot([threshold_index] * 2, list(range(2)), 'r--')
    plt.show()
    print(p, original_delta, threshold_index)
    print(*delta_cdf)


if __name__ == "__main__":
    pvalue_test_example()
    # plot_distance()
    # plot_CDF_test()
    # unittest.main()

    
