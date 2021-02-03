#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 13:54, 03/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from numpy import sqrt, min, max as np_min, np_max
from pfevaluator.root import Root


class Metrics(Root):
    """
        This class is for: Metrics Concerning Spread of the Solutions
        (Performance Metrics Ensemble for Multiobjective Evolutionary Algorithms)
    """

    def __init__(self, pareto_fronts, reference_fronts):
        super().__init__(pareto_fronts, reference_fronts)

    def maximum_spread(self, pareto_fronts=None, reference_fronts=None):  ## MS function
        """ It addresses the range of objective function values and takes into account the proximity to the true Pareto front"""
        pareto_fronts, reference_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts)
        n_objs = reference_fronts.shape[1]
        pf_max = np_max(pareto_fronts, axis=0)
        pf_min = np_min(pareto_fronts, axis=0)
        rf_max = np_max(reference_fronts, axis=0)
        rf_min = np_min(reference_fronts, axis=0)
        ms = 0
        for i in range(0, n_objs):
            ms += ((min(pf_max[i], rf_max[i]) - max(pf_min[i], rf_min[i])) / (rf_max[i] - rf_min[i]))**2
        return sqrt(ms / n_objs)

    MS = maximum_spread