from app.runtime_comparison import *
from VII_Problems import *
import random

"""
Problem 1
"""
def problem_one():
    functions=[diff_bruteforce, diff_hash]
    tests=generate_runtimes()
    runtime_comparison(functions, tests)
    return

def generate_test_cases():
    tests=[]
    for x in range(0,1000):
        temp=[]
        for y in range(0,100):
            temp.append(random.randint(0,30))
        tests.append(temp)

    return tests


def test(function_list, tests):
    runtime_results=[]
    for function in function_list:
        temp=[]
        for cases in tests:
            sTime = time.time()
            function(cases, 3)
            run_time =  round( (time.time() - sTime), 8)
            temp.append(run_time)
        runtime_results.append(temp)



if __name__ == "__main__":
    tests = generate_test_cases()
    functions=[diff_bruteforce, diff_hash]
    compare_runtime(functions, tests)
