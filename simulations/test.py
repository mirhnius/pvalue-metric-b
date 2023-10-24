# import argparse
# import ast

# parser = argparse.ArgumentParser(description="Reciving aruguments for simulation")
# parser.add_argument("--sample_size", nargs="+", type=int, help="sample size")
# parser.add_argument("--n_bootstrap", nargs="+", type=int, help="number of bootstrap")
# parser.add_argument("--n_permutation", nargs="+", type=int, help="number of permutation")

# parser.add_argument("--model", type=str, help="model name")
# parser.add_argument("--parameters", type=str, help="model parameters")

# args = parser.parse_args()
# # print(args.sample_size, args.n_bootstrap, args.n_permutation)

# import scipy
# import numpy as np
# # def func_test(func, sample_size, **kwargs):
# #     # Generate data
# #     data = np.random.normal(size=sample_size)
# #     # Run test
# #     p_value = func(data, **kwargs)
# #     return p_value

# # model_params = ast.literal_eval(args.parameters)
# # print(func_test(args.model, 10, **model_params))
# model_params = ast.literal_eval(args.parameters)
# print(model_params)

import argparse
import ast

parser = argparse.ArgumentParser(description="Receiving arguments for simulation")
parser.add_argument("--model", type=str, help="model parameters")

args = parser.parse_args()

if args.model:
    model_params = ast.literal_eval(args.model)
    print(model_params)