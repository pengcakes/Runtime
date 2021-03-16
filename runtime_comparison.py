"""
Finally going to have a formal version of this.

input: functions

output: runtime of functions vs increasingly long inputs


TODO LIST:

- write/find a function that can generate test cases filling a .txt
- might be even better to store tests in XML JSON or a learn a new format
- input reading function
- Make the title, axis, and legend say the right thing
- use a helper func for the graph?
- improve the graph
- make it some kind of package I can import at anytime to check runtime.


Things to exam runtime:
- Dynamic Programming fib() recursive vs for loop but storing



"""
import time, raybeam_questions
import numpy as np
import math, sys
from pylab import *


# takes functions and tests
# returns runtimes for each function+test
def generate_runtimes(function_list, tests):
    runtime_results=[]
    for function in function_list:
        temp=[]
        for cases in tests:
            sTime = time.time()

            function(cases)
            run_time =  round( (time.time() - sTime), 8)

            temp.append(run_time)
        runtime_results.append(temp)

    return runtime_results


def draw_graph(runtimes, tests):
    style.use('seaborn-whitegrid')
    rcParams['figure.figsize'] = [12, 6]
    title("Runtime Comparison")
    xlabel("Increasingly large test cases.")
    ylabel("Runtime")

    # plot each runtime
    for x in runtimes:
        plot(tests, x, 'r', label='n')


    legend(loc='upper right')

    show()

# function to call
def compare_runtime(function_list, tests):
    runtimes=generate_runtimes(function_list, tests)
    draw_graph(runtimes, tests)


if __name__ == "__main__":

    # need better way to prepare inputs (think about running this process from another location)
    function_list=[raybeam_questions.find_all_factors_0,raybeam_questions.find_all_factors_1]

    with open("temp_test.txt", "r") as f:
        tests = f.read().split()
    tests=[int(x) for x in tests]

    compare_runtime(function_list, tests)
