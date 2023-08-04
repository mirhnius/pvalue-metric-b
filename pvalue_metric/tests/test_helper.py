import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

# Put the pvalue_metric directory on the Python path.
PACKAGE_DIR = Path(__file__).parents[2]
sys.path.append(str(PACKAGE_DIR))

from pvalue_metric.helper import (bootstrapped_cohorts, get_data,
                                  permutated_cohorts)

Data_DIR = Path(PACKAGE_DIR / "study_files/roi_data.csv")

class TestHelper(unittest.TestCase):
    path = Data_DIR
    df = pd.read_csv(path)
    target_column = "Left-Accumbens-area_change"
    target_groups = ["PD-non-MCI", "HC"]
    subject_group = "dx_group"

    def test_get_data(self):
        HC_group = tuple(self.df[self.target_column].loc[self.df[self.subject_group] == "HC"])
        non_MCI_group = tuple(self.df[self.target_column].loc[self.df[self.subject_group] == "PD-non-MCI"])
        data = get_data(self.path, self.target_column, self.target_groups)
        # print(tuple([non_MCI_group, HC_group]))
        # print(data)
        self.assertEqual(data, (non_MCI_group, HC_group))
    
    def test_bootstrapped_cohorts(self):
        data = get_data(self.path, self.target_column, self.target_groups)
        bst_cohorts = bootstrapped_cohorts(data, 100)
        self.assertEqual(len(bst_cohorts), 2)
        self.assertEqual(len(bst_cohorts[0]), 100)
        self.assertEqual(len(bst_cohorts[1]), 100)
        self.assertFalse(np.any(np.isin(bst_cohorts[0][0], bst_cohorts[1][0])))
        self.assertFalse(np.any(np.isin(bst_cohorts[0][66], bst_cohorts[1][56])))
        self.assertTrue(np.all(np.isin(bst_cohorts[0][0], data[0])))

    def test_permuted_cohorts(self):
        data = get_data(self.path, self.target_column, self.target_groups)
        prmt_cohorts = permutated_cohorts(data, 100)
        self.assertEqual(len(prmt_cohorts), 2)
        self.assertEqual(len(prmt_cohorts[0]), 100)
        self.assertEqual(len(prmt_cohorts[1]), 100)
        self.assertFalse(np.any(np.isin(prmt_cohorts[0][0], prmt_cohorts[1][0])))
        self.assertFalse(np.any(np.isin(prmt_cohorts[0][56], prmt_cohorts[1][56])))
    
