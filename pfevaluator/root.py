#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 04:34, 03/02/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%

from numpy import all, any, ndarray, array, isfinite, isnan, zeros, where
from numpy import max as np_max


class Root:
    """
        This class is Abstract class for all other class to inherit
    """

    def __init__(self, pareto_front=None, reference_front=None):
        """
        :param pareto_front: list/tuple or 2d-array (matrix) of non-dominated front (pareto front obtained from your test case)
        :param reference_front: list/tuple or 2d-array (matrix) of True pareto-front or your appropriate front you wish to be reference front
        """
        self.messages = []
        self.flag = True
        self.n_objs = 0
        # When creating object, you can pass pareto front with different size, or even None. It wont effect the program
        # But when you calling the function, if you pass None or front with different size --> this flag will be triggered

        self.pareto_front = self.check_convert_front(pareto_front)
        self.reference_front = self.check_convert_front(reference_front)

    def check_convert_front(self, front=None, converted_type="float64"):
        if front is None:
            return None
        else:
            if type(front) in [list, tuple]:
                front_temp = array(front)
                if type(front_temp[0]) is not ndarray:
                    self.messages.append("Some points in your front have different size. Please check again")
                    self.flag = False
                    return None
                else:
                    front_temp = front_temp.astype(converted_type)
                    check_none = isnan(front_temp).any()
                    check_infinite = isfinite(front_temp).all()
                    if check_none or not check_infinite:
                        self.messages.append("Some points in your front contain None/Infinite value. Please check again")
                        self.flag = False
                        return None
                    else:
                        return front_temp
            if type(front) is ndarray:
                return front

    def print_messages(self):
        for msg in self.messages:
            print(msg)

    def check_hypervolume_point(self, hv_point=None):
        if hv_point is None:
            self.messages.append("Need Hypervolume point to calculate Volume. Please set its values")
            self.print_messages()
            exit(0)

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

    def get_pareto_front_reference_front(self, pareto_front=None, reference_front=None, metric=None):
        reference_front = self.check_convert_front(reference_front)
        pareto_front = self.check_convert_front(pareto_front)
        if self.reference_front is None:
            if reference_front is None:
                self.messages.append(f'To calculate {metric} you need Reference front')
                self.print_messages()
                exit(0)
            else:
                if self.pareto_front is None:
                    if pareto_front is None:
                        self.messages.append(f'To calculate {metric} you need Pareto front obtained from yor test case')
                        self.print_messages()
                        exit(0)
                    else:
                        return pareto_front, reference_front
                else:
                    if pareto_front is None:
                        return self.pareto_front, reference_front
                    else:
                        return pareto_front, reference_front
        else:
            if reference_front is None:
                if self.pareto_front is None:
                    if pareto_front is None:
                        self.messages.append(f'To calculate {metric} you need Pareto front obtained from yor test case')
                        self.print_messages()
                        exit(0)
                    else:
                        return pareto_front, self.reference_front
                else:
                    if pareto_front is None:
                        return self.pareto_front, self.reference_front
                    else:
                        return pareto_front, self.reference_front
            else:
                if self.pareto_front is None:
                    if pareto_front is None:
                        self.messages.append(f'To calculate {metric} you need Pareto front obtained from yor test case')
                        self.print_messages()
                        exit(0)
                    else:
                        return pareto_front, reference_front
                else:
                    if pareto_front is None:
                        return self.pareto_front, reference_front
                    else:
                        return pareto_front, reference_front

    def find_reference_front(self, solutions=None):     # List of non-dominated solutions
        list_solutions = self.check_convert_front(solutions)
        list_dominated = self.find_dominates_list(list_solutions)
        return list_solutions[where(list_dominated == 0)]

    def find_reference_point(self, solutions=None):     # The maximum single point in all dimensions
        list_solutions = self.check_convert_front(solutions)
        return np_max(list_solutions, axis=0)

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

