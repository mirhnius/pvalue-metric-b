import sys
import unittest
from pathlib import Path

import matplotlib.pyplot as plt
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


if __name__ == "__main__":
    plot_distance()
    unittest.main()

    
