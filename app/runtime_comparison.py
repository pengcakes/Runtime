"""
Author: Austin Peng

Finally going to have a formal version of this.

input:
1) list of functions to compare. functions will need
to take the same test cases

2) list of test cases. At this time only one variable
may be tested against so if there are multiple inputs
to the functions pick one.

output: runtime of functions vs increasingly long inputs displayed in a graph

TODO LIST:
+ write/find a function that can generate test cases filling a .txt ***might not need, could just create a list on the spot***
+ Make the title, axis, and legend say the right thing
+ use a helper func for the graph?
+ improve the graph
- make it some kind of package I can import at anytime to check runtime. ***need to make it work well before uploading***
+ integrate timeit into this? ***nah***
- make this work w/ functions that use more than one input --> EDIT generate_runtimes()


Things to exam runtime:
- Dynamic Programming fib() recursive vs memoization
- Find prime number from coding questions to review
- firstDuplicate questions. Array vs Hashtable
"""
import time, math, sys
import numpy as np
from pylab import *


"""
takes functions and tests
returns runtimes for each function+test
"""
def generate_runtimes(function_list, tests):
    runtime_results=[]
    # appends a list of runtimes for each function
    for function in function_list:
        temp=[]
        for cases in tests:
            sTime = time.time()
            function(cases, 3)
            run_time =  round( (time.time() - sTime), 8)
            temp.append(run_time)
        runtime_results.append(temp)

    return runtime_results

"""
draws graph given runtimes and list of test runs
"""
def draw_graph(function_list, runtimes, tests):
    style.use('ggplot')
    rcParams['figure.figsize'] = [8, 6]
    title("Runtime Comparison")
    xlabel("Increasingly large test cases.")
    ylabel("Runtime")

    # plot each runtime
    for count,x in enumerate(runtimes):
        plot(tests, x, c=np.random.rand(3,), label='{name}'.format(name=function_list[count].__name__))

    legend(loc='upper left')

    show()

"""
Final function to use. Calls draw_graph and generate_runtimes.
"""
def compare_runtime(function_list, tests):
    runtimes=generate_runtimes(function_list, tests)
    draw_graph(function_list, runtimes, tests)


if __name__ == "__main__":
    print('')
    # # need better way to prepare inputs (think about running this process from another location)
    # function_list=[raybeam_questions.find_all_factors_0,raybeam_questions.find_all_factors_1]
    #
    # with open("temp_test.txt", "r") as f:
    #     tests = f.read().split()
    # tests=[int(x) for x in tests]
    #
    # compare_runtime(function_list, tests)
