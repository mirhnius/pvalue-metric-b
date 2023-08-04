import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

# Put the pvalue_metric directory on the Python path.
PACKAGE_DIR = Path(__file__).parents[2]
sys.path.append(str(PACKAGE_DIR))

from pvalue_metric import metric


class TestMetric(unittest.TestCase):
    
    def test_mean_euclidean_distance(self):
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.125)
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.1)
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.08333333333333333)
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.07142857142857142)
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.0625)
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.05555555555555555)
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.05)
        # pvalues = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2])
        # self.assertEqual(metric.mean_euclidean_distance(pvalues), 0.045454545454545456)
