import unittest
import numpy as np
import pandas as pd
from pathlib import Path
from helper import get_data


class TestHelper(unittest.TestCase):

    def test_get_data(self):
        path = Path("./study_files/roi_data.csv")
        df = pd.read_csv(path)
        target_column = "Left-Accumbens-area_change"
        target_groups = ["PD-non-MCI", "HC"]
        subject_group = "dx_group"
        HC_group = tuple(df[target_column].loc[df[subject_group] == "HC"])
        non_MCI_group = tuple(df[target_column].loc[df[subject_group] == "PD-non-MCI"])
        data = get_data(path, target_column, target_groups)
        # print(tuple([non_MCI_group, HC_group]))
        # print(data)
        self.assertEqual(data, (non_MCI_group, HC_group))