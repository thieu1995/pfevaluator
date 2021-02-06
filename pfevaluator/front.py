#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 20:30, 05/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from pfevaluator.root import Root
from numpy import sum


class Metric(Root):
    """
        This class is for:
            + Evaluating population of obtained front
            + No need True Pareto front
    """

    def __init__(self, pareto_front=None, reference_front=None, **kwargs):
        super().__init__(pareto_front, reference_front)
        ## Other parameters
        for key, value in kwargs.items():
            setattr(self, key, value)

    ##
    ## Metrics Assessing the Number of Pareto Optimal Solutions in the Set
    ##
    def ratio_of_non_dominated_individuals(self, fronts=None):              ## RNI function
        dominated_list = self.find_dominates_list(fronts)
        return (len(dominated_list) - sum(dominated_list)) / len(dominated_list)

    def pareto_dominance_indicator(self, pareto_front=None, reference_front=None):  ## NR function
        pass



    # Metrics Assessing the Number of Pareto Optimal Solutions in the Set
    RNI = ratio_of_non_dominated_individuals
    PDI = pareto_dominance_indicator

