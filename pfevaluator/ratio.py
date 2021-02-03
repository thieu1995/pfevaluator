#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 09:29, 23/09/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieu1995                                                        %
# -------------------------------------------------------------------------------------------------------%

from numpy import sum, any, all
from pfevaluator.root import Root


class Metrics(Root):
    """
        This class is for: Metrics Assessing the Number of Pareto Optimal Solutions in the Set
        (Performance Metrics Ensemble for Multiobjective Evolutionary Algorithms)
    """

    def __init__(self, pareto_fronts, reference_fronts):
        super().__init__(pareto_fronts, reference_fronts)

    def ratio_of_non_dominated_individuals(self, fronts=None):    ## RNI function
        dominated_list = self.find_dominates_list(fronts)
        return (len(dominated_list) - sum(dominated_list)) / len(dominated_list)

    def error_ratio(self, pareto_fronts=None, reference_fronts=None):  ## ER function
        pf_fronts, rf_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts, "ER")
        rni = 0
        for point in pf_fronts:
            list_flags = [all(point == solution) for solution in rf_fronts]
            if any(list_flags):
                rni += 1
        return rni / len(rf_fronts)

    def overall_non_dominated_vector_generation(self, pareto_fronts=None, reference_fronts=None):  ## ONVG function
        pf_fronts, rf_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts, "ONVG")
        rni = 0
        for point in pf_fronts:
            list_flags = [all(point == solution) for solution in rf_fronts]
            if any(list_flags):
                rni += 1
        return rni

    def pareto_dominance_indicator(self, pareto_fronts=None, reference_fronts=None):  ## NR function
        pass

    RNI = ratio_of_non_dominated_individuals
    NR = pareto_dominance_indicator
    ER = error_ratio
    ONVG = overall_non_dominated_vector_generation