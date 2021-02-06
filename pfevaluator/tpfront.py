#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 20:45, 05/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from pfevaluator.root import Root
from numpy import sum, any, all, sqrt, zeros, mean
from numpy import min as np_min
from numpy import max as np_max
from numpy.linalg import norm


class Metric(Root):
    """
        This class is for: Evaluating Obtained front and True Pareto front
    """

    def __init__(self, pareto_fronts=None, reference_fronts=None, **kwargs):
        super().__init__(pareto_fronts, reference_fronts)
        ## Other parameters
        for key, value in kwargs.items():
            setattr(self, key, value)

    ##
    ## Ratio: Metrics Assessing the Number of Pareto Optimal Solutions in the Set
    ##
    def error_ratio(self, pareto_front=None, reference_front=None):     ## ER function
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front, "ER")
        rni = 0
        for point in pareto_front:
            list_flags = [all(point == solution) for solution in reference_front]
            if not any(list_flags):
                rni += 1
        print(f"{rni} - {len(reference_front)}")
        return rni / len(reference_front)

    def overall_non_dominated_vector_generation(self, pareto_front=None, reference_front=None):  ## ONVG function
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front, "ONVG")
        rni = 0
        for point in pareto_front:
            list_flags = [all(point == solution) for solution in reference_front]
            if any(list_flags):
                rni += 1
        print(f"===={rni} - {len(reference_front)}")
        return rni

    ##
    ##  Spread : Metrics Concerning Spread of the Solutions
    ##
    def maximum_spread(self, pareto_front=None, reference_front=None):  ## MS function
        """ It addresses the range of objective function values and takes into account the proximity to the true Pareto front"""
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front)
        n_objs = reference_front.shape[1]
        pf_max = np_max(pareto_front, axis=0)
        pf_min = np_min(pareto_front, axis=0)
        rf_max = np_max(reference_front, axis=0)
        rf_min = np_min(reference_front, axis=0)
        ms = 0
        for i in range(0, n_objs):
            ms += ((min(pf_max[i], rf_max[i]) - max(pf_min[i], rf_min[i])) / (rf_max[i] - rf_min[i])) ** 2
        return sqrt(ms / n_objs)

    ##
    ##  Closeness: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
    ##
    def generational_distance(self, pareto_front=None, reference_front=None):  ## GD function
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front, "GD")
        pf_size, rf_size = len(pareto_front), len(reference_front)
        gd = 0
        for i in range(pf_size):
            dist_min = min([norm(pareto_front[i] - reference_front[j]) for j in range(0, rf_size)])
            gd += dist_min ** 2
        return sqrt(gd) / pf_size

    def inverted_generational_distance(self, pareto_front=None, reference_front=None):  ## IGD function
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front, "IGD")
        pf_size, rf_size = len(pareto_front), len(reference_front)
        igd = 0
        for i in range(rf_size):
            dist_min = min([norm(reference_front[i] - point) for point in pareto_front])
            igd += dist_min ** 2
        return sqrt(igd) / rf_size

    def maximum_pareto_front_error(self, pareto_front=None, reference_front=None):  ## MPFE function
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front, "IGD")
        pf_size, rf_size = len(pareto_front), len(reference_front)
        mpfe_list = zeros(pf_size)
        for i in range(pf_size):
            dist_min = min([norm(reference_front[i] - point) for point in pareto_front])
            mpfe_list[i] = dist_min
        return max(mpfe_list)

    ##
    ## Distribution: Metrics Focusing on Distribution of the Solutions
    ##
    def spacing(self, pareto_front=None, reference_front=None):  ## S function
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front)
        pf_size = len(pareto_front)

        dist_min_list = zeros(pf_size)
        for i in range(pf_size):
            dist_min = min([norm(pareto_front[i] - reference_front[j]) for j in range(pf_size) if i != j])
            dist_min_list[i] = dist_min
        dist_mean = mean(dist_min_list)
        spacing = sqrt(sum((dist_min_list - dist_mean) ** 2) / pf_size)
        return spacing

    def spacing_to_extend(self, pareto_front=None, reference_front=None):  ## STE function
        pareto_front, reference_front = self.get_pareto_front_reference_front(pareto_front, reference_front)
        pf_size = len(pareto_front)
        dist_min_list = zeros(pf_size)
        for i in range(pf_size):
            dist_min = min([norm(pareto_front[i] - reference_front[j]) for j in range(pf_size) if i != j])
            dist_min_list[i] = dist_min
        dist_mean = mean(dist_min_list)
        spacing = sum((dist_min_list - dist_mean) ** 2) / (pf_size - 1)

        f_max = np_max(pareto_front, axis=0)
        f_min = np_min(pareto_front, axis=0)
        extent = sum(abs(f_max - f_min))
        ste = spacing / extent
        return ste


    # Ratio: Metrics Assessing the Number of Pareto Optimal Solutions in the Set
    ER = error_ratio
    ONVG = overall_non_dominated_vector_generation

    # Spread : Metrics Concerning Spread of the Solutions
    MS = maximum_spread

    # Closeness: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
    GD = generational_distance
    IGD = inverted_generational_distance
    MPFE = maximum_pareto_front_error

    # Distribution: Metrics Focusing on Distribution of the Solutions
    S = spacing
    STE = spacing_to_extend


