import os
import numpy as np
import pandas as pd
from pathlib import Path
from scipy import stats
from simulation_helper import simulation

# TASK_ID = int(os.environ.get('TASK_ID'))
# INPUTFILENAME = os.environ.get('INPUTFILENAME')
cwd = Path(__file__).parent.absolute()

TASK_ID = 1
INPUTFILENAME = "simulation_combinations.csv"

pmetrics = np.zeros(1000)
pvalues = np.zeros(1000)

combinations_df = pd.read_csv(cwd / INPUTFILENAME, header=0, index_col=0)
combinations_df.astype({'size': 'int64', 'n_bootstrap': 'int64', 'n_permutation': 'int64'}, copy=False)


for i in range(1):

    combination = combinations_df.loc[TASK_ID] # it doesnt work with correct types

    func1_args = {'loc': 0, 'scale': 1, 'size': combinations_df['size'][TASK_ID]}
    func2_args = {'loc':  combinations_df['locations'][TASK_ID], \
                   'scale': combination['scale'], 'size': combinations_df['size'][TASK_ID]}
    
    simulation_result = simulation(stats.ttest_ind, np.random.normal, np.random.normal, 
                        combinations_df['n_bootstrap'][TASK_ID], combinations_df['n_permutation'][TASK_ID],
                        func1_args, func2_args)
    pmetrics[i] = simulation_result['p_metric']
    pvalues[i] = simulation_result['pvalue']

result = pd.DataFrame({'p_metric': pmetrics, 'pvalue': pvalues})
result.to_csv(cwd / f'simulation_result_{TASK_ID}.csv')
