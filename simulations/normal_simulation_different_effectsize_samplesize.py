import os
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats
from simulation_helper import simulation

TASK_ID = int(os.environ.get('TASK_ID'))
INPUTFILENAME = os.environ.get('INPUTFILENAME')
cwd = Path(__file__).parent.absolute()


pmetrics = np.zeros(1000)
pvalues = np.zeros(1000)
combinations_df = pd.read_csv(cwd / INPUTFILENAME, header=0, index_col=0)
for i in range(1000):

    combination = combinations_df.iloc[TASK_ID]
    func1_args = {'loc': 0, 'scale': 1, 'size': combination['size']}
    func2_args = {'loc': combination['location'], \
                   'scale': combination['scale'], 'size': combination['size']}
    
    simulation_result = simulation(stats.ttest_ind, np.random.normal, np.random.normal, 
                        combination['n_bootstrap'], combination['n_permutation'],
                        func1_args, func2_args)
    pmetrics[i] = simulation_result['p_metric']
    pvalues[i] = simulation_result['pvalue']

result = pd.DataFrame({'p_metric': pmetrics, 'pvalue': pvalues})
result.to_csv(cwd / f'simulation_result_{TASK_ID}.csv')
