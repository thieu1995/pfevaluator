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


class Metric(Root):
    """
        This class is for: Metric Measuring the Closeness of the Solutions to the True Pareto Front
    """

    def __init__(self, pareto_front=None, reference_front=None):
        super().__init__(pareto_front, reference_front)
        self.hv_point = None
        self.hv_slide = 100
        self.error_msg = "Need HyperVolume point (Reference point) to calculate volume. " \
                         "Please set its value or pass another parameter to this function: all_fronts=ndarray"

    def hyper_volume(self, pareto_front=None, reference_front=None, hv_point=None, **kwargs):  ## HV function
        if hv_point is None:
            if "all_fronts" not in kwargs.keys():
                print(self.error_msg)
                exit(0)
            else:
                hv_point = self.find_reference_point(kwargs["all_fronts"])
        if "hv_slide" in kwargs.keys():
            hv_slide = kwargs["hv_slide"]
        else:
            hv_slide = self.hv_slide
        hv_point = hv_point + hv_slide
        pf_fronts, rf_fronts = self.get_pareto_front_reference_front(pareto_front, reference_front, "HV")
        hv_obj = hypervolume(pf_fronts)
        return hv_obj.compute(hv_point)

    def hyper_area_ratio(self, pareto_front=None, reference_front=None, hv_point=None, **kwargs):  ## HAR function
        if hv_point is None:
            if "all_fronts" not in kwargs.keys():
                print(self.error_msg)
                exit(0)
            else:
                hv_point = self.find_reference_point(kwargs["all_fronts"])
        if "hv_slide" in kwargs.keys():
            hv_slide = kwargs["hv_slide"]
        else:
            hv_slide = self.hv_slide
        hv_point = hv_point + hv_slide
        pf_fronts, rf_fronts = self.get_pareto_front_reference_front(pareto_front, reference_front, "HAR")
        hv_pf = hypervolume(pf_fronts)
        hv_rf = hypervolume(reference_front)
        return hv_pf.compute(hv_point) / hv_rf.compute(hv_point)

    HV = hyper_volume
    HAR = hyper_area_ratio

