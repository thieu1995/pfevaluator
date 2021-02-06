# Version 1.1.0

### Change models
+ Compose all methods with same parameters into a single class 
    + **front**: Evaluating all possible of all fronts (No need Reference front)
        + Ratio: Metrics Assessing the Number of Pareto Optimal Solutions in the Set
            + RNI: ratio_of_non_dominated_individuals
            + PDI: pareto_dominance_indicator (not implemented yet) 
    + **pfront (Pareto front)**: Evaluating single Pareto front (No need Reference front)
        + Distribution: Metrics Focusing on Distribution of the Solutions
            + UD = uniform_distribution
            + NDC = number_of_distinct_choices (not implemented yet)
    + **tpfront (True Pareto front)**: Evaluating Pareto front vs Reference front
        + Ratio: Metrics Assessing the Number of Pareto Optimal Solutions in the Set
            + ER: error_ratio
            + ONVG: overall_non_dominated_vector_generation
        + Spread : Metrics Concerning Spread of the Solutions
            + MS = maximum_spread
        + Closeness: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
            + GD: generational_distance
            + IGD: inverted_generational_distance
            + MPFE: maximum_pareto_front_error
        + Distribution: Metrics Focusing on Distribution of the Solutions
            + S: spacing
            + STE: spacing_to_extend
    + **volume** (need both Obtained front and Reference front): I kept this file since it using other library 
        + HV
        + HAR 
    
### Change others
+ Examples: 
    + Add all examples for all metrics
    + Add example for multiple metrics called at the same time
+ Add Change Log file
+ Add README.md file
+ Add support-data folder for test case

---------------------------------------------------------------------
# Version 1.0.0 (First version)

## Models

### root.py file: contains all need functions such as
1. find non-dominated list function
2. print_messages
3. get_pareto_front_reference_front
4. find_reference_front
5. get_metrics_by_name
6. get_metrics_by_list
7. All Metric class will inherit this Root class.

### Closeness: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
1. GD: generational_distance
2. IGD: inverted_generational_distance
3. MPFE: maximum_pareto_front_error

### Closeness_diversity: Metrics Measuring the Closeness of the Solutions to the True Pareto Front
1. HV: hyper_volume (using different library)
2. HAR: hyper_area_ratio (using different library)

### Distribution: Metrics Focusing on Distribution of the Solutions
1. UD: uniform_distribution
2. S: spacing
3. STE: spacing_to_extend
4. NDC: number_of_distinct_choices (not implemented yet)

### Ratio: Metrics Assessing the Number of Pareto Optimal Solutions in the Set
1. RNI: ratio_of_non_dominated_individuals
2. ER: error_ratio
3. ONVG: overall_non_dominated_vector_generation
4. PDI: pareto_dominance_indicator (not implemented yet)

### Spread: Metrics Concerning Spread of the Solutions
1. MS: maximum_spread 


