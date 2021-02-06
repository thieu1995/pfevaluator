#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 11:23, 16/03/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieu1995                                                  %
#-------------------------------------------------------------------------------------------------------%


def find_reference_front(all_possible_fronts):
    from pfevaluator.root import Root
    obj = Root()
    return obj.find_reference_front(all_possible_fronts)


def metric_front(list_fronts, metrics:list) -> dict:
    from pfevaluator.front import Metric
    obj = Metric()
    results_dict = {}
    for metric in metrics:
        result = None
        if hasattr(obj, metric):
            result = getattr(obj, metric)(list_fronts)
        results_dict[metric] = result
    return results_dict


def metric_pfront(front, metrics: list) -> dict:
    from pfevaluator.pfront import Metric
    obj = Metric()
    results_dict = {}
    for metric in metrics:
        result = None
        if hasattr(obj, metric):
            result = getattr(obj, metric)(front)
        results_dict[metric] = result
    return results_dict


def metric_tpfront(pareto_front, reference_front, metrics: list) -> dict:
    from pfevaluator.tpfront import Metric
    obj = Metric()
    results_dict = {}
    for metric in metrics:
        result = None
        if hasattr(obj, metric):
            result = getattr(obj, metric)(pareto_front, reference_front)
        results_dict[metric] = result
    return results_dict


def metric_volume(pareto_front, reference_front, metrics: list, hv_point=None, all_fronts=None) -> dict:
    if hv_point is None:
        if all_fronts is None:
            print("Need HyperVolume point (Reference point) to calculate volume. " 
                  "Please set its value or pass another parameter to this function: all_fronts=ndarray")
            exit(0)
    from pfevaluator.volume import Metric
    obj = Metric()
    results_dict = {}
    for metric in metrics:
        result = None
        if hasattr(obj, metric):
            result = getattr(obj, metric)(pareto_front, reference_front, hv_point, all_fronts=all_fronts)
        results_dict[metric] = result
    return results_dict

