#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 08:59, 23/09/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieu1995                                                        %
# -------------------------------------------------------------------------------------------------------%

from numpy import max, sqrt, zeros
from numpy.linalg import norm
from pfevaluator.root import Root


class Metrics(Root):
    """
        This class is for: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
        (Performance Metrics Ensemble for Multiobjective Evolutionary Algorithms)
    """

    def __init__(self, pareto_fronts, reference_fronts):
        super().__init__(pareto_fronts, reference_fronts)

    def generational_distance(self, pareto_fronts=None, reference_fronts=None):  ## GD function
        pf_fronts, rf_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts, "GD")
        pf_size, rf_size = len(pf_fronts), len(rf_fronts)
        gd = 0
        for i in range(pf_size):
            dist_min = min([norm(pf_fronts[i] - rf_fronts[j]) for j in range(0, rf_size)])
            gd += dist_min ** 2
        return sqrt(gd) / pf_size

    def inverted_generational_distance(self, pareto_fronts=None, reference_fronts=None):  ## IGD function
        pareto_fronts, reference_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts, "IGD")
        pf_size, rf_size = len(pareto_fronts), len(reference_fronts)
        igd = 0
        for i in range(rf_size):
            dist_min = min([norm(reference_fronts[i] - point) for point in pareto_fronts])
            igd += dist_min ** 2
        return sqrt(igd) / rf_size

    def maximum_pareto_front_error(self, pareto_fronts=None, reference_fronts=None):  ## MPFE function
        pareto_fronts, reference_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts, "IGD")
        pf_size, rf_size = len(pareto_fronts), len(reference_fronts)
        mpfe_list = zeros(pf_size)
        for i in range(pf_size):
            dist_min = min([norm(reference_fronts[i] - point) for point in pareto_fronts])
            mpfe_list[i] = dist_min
        return max(mpfe_list)

    GD = generational_distance
    IGD = inverted_generational_distance
    MPFE = maximum_pareto_front_error


