#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 05:58, 03/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from numpy import abs, min, max, sqrt, mean, sum, zeros
from numpy.linalg import norm
from pfevaluator.root import Root


class Metrics(Root):
    """
        This class is for: Metrics Focusing on Distribution of the Solutions
        (Performance Metrics Ensemble for Multiobjective Evolutionary Algorithms)
    """

    def __init__(self, pareto_fronts, reference_fronts):
        super().__init__(pareto_fronts, reference_fronts)

    def uniform_distribution(self, pareto_fronts=None, reference_fronts=None, xichma_shared=100):  ## UD function
        """ It measures the distribution of non-dominated individuals on the found trade-off surface. """
        pareto_fronts = self.check_convert_fronts(pareto_fronts)
        pf_size = len(pareto_fronts)
        list_niches = zeros(pf_size)
        for i in range(0, pf_size):
            niche_count = 0
            for j in range(0, pf_size):
                if i != j:
                    dist = norm(pareto_fronts[i] - pareto_fronts[j])
                    niche_count += 1 if dist < xichma_shared else 0
            list_niches[i] = niche_count
        niche_mean = mean(list_niches)
        S_nc = sqrt( (sum( (list_niches - niche_mean)**2 )) / (pf_size - 1) )
        return 1.0 / (1.0 + S_nc)

    def spacing(self, pareto_fronts=None, reference_fronts=None):  ## S function
        pareto_fronts, reference_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts)
        pf_size = len(pareto_fronts)

        dist_min_list = zeros(pf_size)
        for i in range(pf_size):
            dist_min = min([norm(pareto_fronts[i] - reference_fronts[j]) for j in range(pf_size) if i != j])
            dist_min_list[i] = dist_min
        dist_mean = mean(dist_min_list)
        spacing = sqrt(sum((dist_min_list - dist_mean) ** 2) / pf_size)
        return spacing

    def spacing_to_extend(self, pareto_fronts=None, reference_fronts=None):  ## STE function
        pareto_fronts, reference_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts)
        pf_size = len(pareto_fronts)
        dist_min_list = zeros(pf_size)
        for i in range(pf_size):
            dist_min = min([norm(pareto_fronts[i] - reference_fronts[j]) for j in range(pf_size) if i != j])
            dist_min_list[i] = dist_min
        dist_mean = mean(dist_min_list)
        spacing = sum((dist_min_list - dist_mean) ** 2) / (pf_size - 1)

        f_max = max(pareto_fronts, axis=0)
        f_min = min(pareto_fronts, axis=0)
        extent = sum(abs(f_max - f_min))
        ste = spacing / extent
        return ste

    def number_of_distinct_choices(self, pareto_fronts=None, reference_fronts=None):  ## NDC function
        pass

    UD = uniform_distribution
    S = spacing
    STE = spacing_to_extend


