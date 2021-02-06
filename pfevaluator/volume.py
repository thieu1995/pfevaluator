#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 15:09, 03/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from pfevaluator.root import Root
from pygmo.core import hypervolume


class Metrics(Root):
    """
        This class is for: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
        (Performance Metrics Ensemble for Multiobjective Evolutionary Algorithms)
    """

    def __init__(self, pareto_fronts=None, reference_fronts=None):
        super().__init__(pareto_fronts, reference_fronts)
        self.hv_point = None

    def hyper_volume(self, pareto_fronts=None, reference_fronts=None, hv_slide=100):  ## HV function
        pf_fronts, rf_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts, "HV")
        if self.hv_point is None:
            self.messages.append("Hypervolume point is None. Please set its values")
            self.print_messages()
            exit(0)
        hv_point = self.hv_point + hv_slide
        hv_obj = hypervolume(pf_fronts)
        return hv_obj.compute(hv_point)

    def hyper_area_ratio(self, pareto_fronts=None, reference_fronts=None, hv_slide=100):  ## HAR function
        pf_fronts, rf_fronts = self.get_pareto_fronts_reference_fronts(pareto_fronts, reference_fronts, "HAR")
        if self.hv_point is None:
            self.messages.append("Hypervolume point is None. Please set its values")
            self.print_messages()
            exit(0)
        hv_point = self.hv_point + hv_slide
        hv_pf = hypervolume(pf_fronts)
        hv_rf = hypervolume(reference_fronts)
        return hv_pf.compute(hv_point) / hv_rf.compute(hv_point)

    HV = hyper_volume
    HAR = hyper_area_ratio

