"""
Finally going to have a formal version of this.

input: functions

output: runtime of functions vs increasingly long inputs

"""

import time, raybeam_questions
import numpy as np
import math, sys
from pylab import *



tests=[10, 1000, 10000, 100000, 1000000]

# takes functions and tests
# returns runtimes for each function+test
def generate_runtimes(function_list, tests):
    runtime_results=[]
    for function in function_list:
        for cases in tests:
            sTime = time.time()

            function(cases)
            run_time =  round( (time.time() - sTime), 8)

            runtime_results.append(run_time)

    return runtime_results



if __name__ == "__main__":
    function_list=[raybeam_questions.find_all_factors_0,
    raybeam_questions.find_all_factors_1]
    #generate_runtimes(function_list)


    style.use('seaborn-whitegrid')
    rcParams['figure.figsize'] = [16, 8]
    title("Runtime Comparison")
    xlabel("Increasingly large test cases.")
    ylabel("Runtime")
    plot(tests, runtime_results_1, 'r', label='n')
    plot(tests, runtime_results_2, 'b', label='1/4n')
    legend(loc='upper right')

    show()
