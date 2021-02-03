#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 04:34, 03/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from numpy import all, any, ndarray, array, isfinite, isnan, zeros


class Root:
    """
        This class is Abstract class for all other class to inherit
        (Performance Metrics Ensemble for Multiobjective Evolutionary Algorithms)
    """

    def __init__(self, pareto_fronts=None, reference_fronts=None):
        """
        :param pareto_fronts: list/tuple or 2d-array (matrix) of non-dominated fronts (pareto fronts obtained from your test case)
        :param reference_fronts: list/tuple or 2d-array (matrix) of True pareto-fronts or your appropriate fronts you wish to be reference fronts
        """
        self.messages = []
        self.flag = True
        self.n_objs = 0
        # When creating object, you can pass pareto fronts with different size, or even None. It wont effect the program
        # But when you calling the function, if you pass None or fronts with different size --> this flag will be triggered

        self.pareto_fronts = self.check_convert_fronts(pareto_fronts)
        self.reference_fronts = self.check_convert_fronts(reference_fronts)

    def check_convert_fronts(self, fronts=None, converted_type="float64"):
        if fronts is None:
            return None
        else:
            if type(fronts) in [list, tuple]:
                fronts_temp = array(fronts)
                if type(fronts_temp[0]) is not ndarray:
                    self.messages.append("Some points in your fronts have different size. Please check again")
                    self.flag = False
                    return None
                else:
                    fronts_temp = fronts_temp.astype(converted_type)
                    check_none = isnan(fronts_temp).any()
                    check_infinite = isfinite(fronts_temp).all()
                    if check_none or not check_infinite:
                        self.messages.append("Some points in your fronts contain None/Infinite value. Please check again")
                        self.flag = False
                        return None
                    else:
                        return fronts_temp

    def print_messages(self):
        for msg in self.messages:
            print(msg)

    def dominates(self, fit_a, fit_b):
        return all(fit_a <= fit_b) and any(fit_a < fit_b)

    def find_dominates_list(self, fit_matrix=None):
        size = len(fit_matrix)
        list_dominated = zeros(size)  # 0: non-dominated, 1: dominated by someone
        for i in range(0, size):
            list_dominated[i] = 0
            for j in range(0, i):
                if any(fit_matrix[i] != fit_matrix[j]):
                    if self.dominates(fit_matrix[i], fit_matrix[j]):
                        list_dominated[j] = 1
                    elif self.dominates(fit_matrix[j], fit_matrix[i]):
                        list_dominated[i] = 1
                        break
                else:
                    list_dominated[j] = 1
                    list_dominated[i] = 1
        return list_dominated

    def get_pareto_fronts_reference_fronts(self, pareto_fronts=None, reference_fronts=None, metric=None):
        reference_fronts = self.check_convert_fronts(reference_fronts)
        pareto_fronts = self.check_convert_fronts(pareto_fronts)
        if self.reference_fronts is None:
            if reference_fronts is None:
                self.messages.append(f'To calculate {metric} you need Reference fronts')
                self.print_messages()
                exit(0)
            else:
                if self.pareto_fronts is None:
                    if pareto_fronts is None:
                        self.messages.append(f'To calculate {metric} you need Pareto fronts obtained from yor test case')
                        self.print_messages()
                        exit(0)
                    else:
                        return pareto_fronts, reference_fronts
                else:
                    if pareto_fronts is None:
                        return self.pareto_fronts, reference_fronts
                    else:
                        return pareto_fronts, reference_fronts
        else:
            if reference_fronts is None:
                if self.pareto_fronts is None:
                    if pareto_fronts is None:
                        self.messages.append(f'To calculate {metric} you need Pareto fronts obtained from yor test case')
                        self.print_messages()
                        exit(0)
                    else:
                        return pareto_fronts, self.reference_fronts
                else:
                    if pareto_fronts is None:
                        return self.pareto_fronts, self.reference_fronts
                    else:
                        return pareto_fronts, self.reference_fronts
            else:
                if self.pareto_fronts is None:
                    if pareto_fronts is None:
                        self.messages.append(f'To calculate {metric} you need Pareto fronts obtained from yor test case')
                        self.print_messages()
                        exit(0)
                    else:
                        return pareto_fronts, reference_fronts
                else:
                    if pareto_fronts is None:
                        return self.pareto_fronts, reference_fronts
                    else:
                        return pareto_fronts, reference_fronts

    def get_metrics_by_name(self, *func_names):
        temp = []
        for idx, func_name in enumerate(func_names):
            obj = getattr(self, func_name)
            temp.append(obj())
        return temp

    def get_metrics_by_list(self, func_name_list=None, func_para_list=None):
        temp = []
        for idx, func_name in enumerate(func_name_list):
            obj = getattr(self, func_name)
            if func_para_list is None:
                temp.append(obj())
            else:
                if len(func_name_list) != len(func_para_list):
                    print("Failed! Different length between functions and parameters")
                    exit(0)
                temp.append(obj(**func_para_list[idx]))
        return temp

