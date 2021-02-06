# pfevaluator: A library for evaluating performance metrics of Pareto fronts in multiple/many objective optimization problems

[![GitHub release](https://img.shields.io/badge/release-1.1.0-yellow.svg)]()
[![](https://img.shields.io/badge/python-3.7+-orange.svg)](https://www.python.org/downloads/release/python-370/)
[![Wheel](https://img.shields.io/pypi/wheel/gensim.svg)](https://pypi.python.org/pypi/pfevaluator) 
[![PyPI version](https://badge.fury.io/py/permetrics.svg)](https://badge.fury.io/py/pfevaluator)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


---
> "Knowledge is power, sharing it is the premise of progress in life. It seems like a burden to someone, but it is the only way to achieve immortality."
>  --- [Thieu Nguyen](https://www.researchgate.net/profile/Thieu_Nguyen6)
---

## Introduction


### Dependencies
* Python (>= 3.6)
* Numpy (>= 1.18.1)
* pygmo (>= 2.13.0) 

### User installation
Install the [current PyPI release](https://pypi.python.org/pypi/pfevaluator):
```bash
pip install pfevaluator     
```

Or install the development version from GitHub:
```bash
pip install git+https://github.com/thieu1995/pfevaluator
```

### Pareto front Performance Metrics

##### Closeness: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
1. GD: Generational Distance
2. IGD: Inverted Generational Distance
3. MPFE: Maximum Pareto Front Error

##### Closeness - Diversity: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
1. HV: Hyper Volume (Using Different Library)
2. HAR: Hyper Area Ratio (Using Different Library)

##### Distribution: Metrics Focusing on Distribution of the Solutions
1. UD: Uniform Distribution
2. S: Spacing
3. STE: Spacing To Extend
4. NDC: Number of Distinct Choices (Not Implemented Yet)

##### Ratio: Metrics Assessing the Number of Pareto Optimal Solutions in the Set
1. RNI: Ratio of Non-dominated Individuals
2. ER: Error Ratio
3. ONVG: Overall Non-dominated Vector Generation
4. PDI: Pareto Dominance Indicator (Not Implemented Yet)

##### Spread: Metrics Concerning Spread of the Solutions
1. MS: Maximum Spread 


### Examples
```code 

+ front: the file contains class Metric for evaluating all posible solution (population of obtained fronts).
+ pfront (Pareto front): the file contains class Metric for evaluating the obtained front from each test case.
+ tpfront: (True pareto front): the file contains class Metric for evaluating the obtained front and True pareto front
 (Reference front). Means, you need to pass the Reference front in this class.

+ True pareto front (Reference front) can be obtained by:
    1) You provide it (If you know the True Pareto front for your problem)
    2) Calculate from all possible fronts obtained from all test case.
        + Assumption you have N1 algorithms to test. 
        + Each algorithm give you a Obtained front. 
        + Each algorithm you run N2 independent trials --> Number of all possible fronts: N1 * N2 
        + Pass all N1*N2 front in our function to calculate the Non-donminated Solutions (Reference front
 - Approximate Pareto front - True Pareto front)


import pfevaluator

## Some avaiable performance metrics for evaluate each type of Pareto front.
pfront_metrics = ["UD", "NDC"]
tpfront_metrics = ["ER", "ONVG", "MS", "GD", "IDG", "MPFE", "S", "STE"]
volume_metrics = ["HV", "HAR"]

pm = pfevaluator.metric_pfront(obtained_front, pfront_metrics)              # Evaluate for each algorithm in each trial
tm = pfevaluator.metric_tpfront(obtained_front, reference_front, tpfront_metrics)        # Same above
vm = pfevaluator.metric_volume(obtained_front, reference_front, volume_metrics, None, all_fronts=matrix_fitness)

## obtained_front: is your front you found in each test case (each trial of each algorithm)
## reference_front (True Pareto front): is your True Pareto front of your problem.
##      If you don't know your True Pareto front, do the above step to get it from population of obtained fronts.
##      Using this function: reference_front = pfevaluator.find_reference_front(matrix_fitness)
##          matrix_fitness is all of your fronts in all test cases.

## The results is dict such as:     pm = { "UD": 0.2, "NDC": 0.1 } 

```

* The full test case in the file: examples/full.py


### Important links

* Official source code repo: https://github.com/thieu1995/pfevaluator
* Download releases: https://pypi.org/project/pfevaluator/
* Issue tracker: https://github.com/thieu1995/pfevaluator/issues
* Change log: https://github.com/thieu1995/pfevaluator/blob/master/ChangeLog.md

* This project also related to my another projects which are "meta-heuristics" and "neural-network", check it here
    * https://github.com/thieu1995/opfunu
    * https://github.com/thieu1995/metaheuristics
    * https://github.com/thieu1995/mealpy
    * https://github.com/thieu1995/permetrics
    * https://github.com/chasebk
   
## Contributions 

### Citation
+ If you use pfevaluator in your project, please cite my works: 
```code 
@article{nguyen2019efficient,
  title={Efficient Time-Series Forecasting Using Neural Network and Opposition-Based Coral Reefs Optimization},
  author={Nguyen, Thieu and Nguyen, Tu and Nguyen, Binh Minh and Nguyen, Giang},
  journal={International Journal of Computational Intelligence Systems},
  volume={12},
  number={2},
  pages={1144--1161},
  year={2019},
  publisher={Atlantis Press}
}
```

### Documents:

1. Yen, G. G., & He, Z. (2013). Performance metric ensemble for multiobjective evolutionary algorithms. IEEE Transactions on Evolutionary Computation, 18(1), 131-144.
2. Panagant, N., Pholdee, N., Bureerat, S., Yildiz, A. R., & Mirjalili, S. (2021). A Comparative Study of Recent Multi-objective Metaheuristics for Solving Constrained Truss Optimisation Problems. Archives of Computational Methods in Engineering, 1-17.
3. Knowles, J., & Corne, D. (2002, May). On metrics for comparing nondominated sets. In Proceedings of the 2002 Congress on Evolutionary Computation. CEC'02 (Cat. No. 02TH8600) (Vol. 1, pp. 711-716). IEEE.
4. Yen, G. G., & He, Z. (2013). Performance metric ensemble for multiobjective evolutionary algorithms. IEEE Transactions on Evolutionary Computation, 18(1), 131-144.
5. Guerreiro, A. P., Fonseca, C. M., & Paquete, L. (2020). The hypervolume indicator: Problems and algorithms. arXiv preprint arXiv:2005.00515.



