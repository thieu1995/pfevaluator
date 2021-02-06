#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 18:21, 05/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from numpy import zeros, vstack
from pandas import DataFrame, read_csv
from os import getcwd
from pathlib import Path
import pfevaluator

basedir = Path(getcwd()).parent.absolute()

models = ["NSGA-II", "NSGA-III", "MO-ALO", "MO-SSA"]
filename = "100_50_100-results.csv"
trial_max = 10

## Load all results to find reference front
matrix_fitness = zeros((1, 3))
for model in models:
    for trial in range(0, trial_max):
        filepath = f'{basedir}/pfevaluator/support_data/{model}/{trial}/{filename}'
        df = read_csv(filepath, usecols=["Power", "Latency", "Cost"])
        matrix_fitness = vstack((matrix_fitness, df.values))
matrix_fitness = matrix_fitness[1:]
reference_front = pfevaluator.find_reference_front(matrix_fitness)

front_metrics = ["RNI", "PDI"]
pfront_metrics = ["UD", "NDC"]
tpfront_metrics = ["ER", "ONVG", "MS", "GD", "IDG", "MPFE", "S", "STE"]
volume_metrics = ["HV", "HAR"]
cols = ["Model", "Trial", "UD", "NDC", "ER", "ONVG", "MS", "GD", "IDG", "MPFE", "S", "STE", "HV", "HAR"]

## For each model and each trial, calculate its performance metrics
results_full_trials = []
fm = pfevaluator.metric_front(matrix_fitness, front_metrics)        # All possible front obtained in all algorithms
for model in models:
    for trial in range(0, trial_max):
        filepath = f'{basedir}/pfevaluator/support_data/{model}/{trial}/{filename}'
        df = read_csv(filepath, usecols=["Power", "Latency", "Cost"])
        front = df.values
        pm = pfevaluator.metric_pfront(front, pfront_metrics)                       # Evaluate for each algorithm in each trial
        tm = pfevaluator.metric_tpfront(front, reference_front, tpfront_metrics)    # Same above
        vm = pfevaluator.metric_volume(front, reference_front, volume_metrics, None, all_fronts=matrix_fitness)

        # pm = {"UD": 0.5, "NDC": 0.3}
        temp = [model, trial, ]
        for metric in pfront_metrics:
            temp.append(pm[metric])
        for metric in tpfront_metrics:
            temp.append(tm[metric])
        for metric in volume_metrics:
            temp.append(vm[metric])
        results_full_trials.append(temp)

pathsave = f'{basedir}/examples/results/'
Path(pathsave).mkdir(parents=True, exist_ok=True)
df1 = DataFrame(results_full_trials, columns=cols)
df1.to_csv(f'{pathsave}/full_trials.csv', index=False)

