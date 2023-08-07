import sys
import unittest
from pathlib import Path

from scipy import stats
import numpy as np
import pandas as pd

# Put the analysis directory on the Python path.
PARENT_DIR = Path(__file__).parents[1]
sys.path.append(str(PARENT_DIR))

import main

Data_DIR = PARENT_DIR.parent[1] / "study_files/roi_data.csv"


class TestMain(unittest.TestCase):
    df = pd.read_csv(Data_DIR)
    target_groups = ["PD-non-MCI", "HC"]
    subject_group = "dx_group"
    ROIs = [
    "Thalamus", "Caudate", "Putamen", "Pallidum",
    "Hippocampus", "Amygdala","Accumbens-area"]
    target_columns = ["thickness_change"] + [region+"_change_pred" for region in ROIs]

    def test_pvalue_test_for_all_volumes(self):
        print(main.pvalue_test_for_all_volumes(Data_DIR, self.target_columns, self.target_groups, 100, 100))

if __name__ == "__main__":
    unittest.main()