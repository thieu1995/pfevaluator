#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 20:45, 05/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from pfevaluator.root import Root
from numpy import sum, zeros, mean, sqrt
from numpy.linalg import norm


class Metric(Root):
    """
        This class is for:
            + Evaluating obtained front from each test
            + No need True Pareto front
    """

    def __init__(self, pareto_front=None, reference_fronts=None, **kwargs):
        super().__init__(pareto_front, reference_fronts)
        ## Other parameters
        for key, value in kwargs.items():
            setattr(self, key, value)

    ##
    ## Distribution: Metrics Focusing on Distribution of the Solutions
    ##
    def uniform_distribution(self, pareto_front=None, xichma_shared=100):  ## UD function
        """ It measures the distribution of non-dominated individuals on the found trade-off surface. """
        pareto_front = self.check_convert_front(pareto_front)
        pf_size = len(pareto_front)
        list_niches = zeros(pf_size)
        for i in range(0, pf_size):
            niche_count = 0
            for j in range(0, pf_size):
                if i != j:
                    dist = norm(pareto_front[i] - pareto_front[j])
                    niche_count += 1 if dist < xichma_shared else 0
            list_niches[i] = niche_count
        niche_mean = mean(list_niches)
        S_nc = sqrt((sum((list_niches - niche_mean) ** 2)) / (pf_size - 1))
        return 1.0 / (1.0 + S_nc)

    def number_of_distinct_choices(self, pareto_front=None):  ## NDC function
        pass

    # Distribution: Metrics Focusing on Distribution of the Solutions
    UD = uniform_distribution
    NDC = number_of_distinct_choices

