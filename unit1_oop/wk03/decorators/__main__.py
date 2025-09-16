import time
import datetime
from math import factorial, prod
from itertools import permutations

# ______ Helper Functions ______
# ------ Slow-Text Helper ------


PRINT_DELAY = 0.15


def slow_tblok(text):
    for line in text.splitlines():
        time.sleep(PRINT_DELAY)
        print(line)


# ------ Input Function ------


def accept_input():
    while True:
        raw = input("Enter [1-6]: ").strip()
        try:
            user_input = int(raw)
            if user_input not in (1, 2, 3, 4, 5, 6):
                raise ValueError(
                    f"Input must be 1, 2, 3, 4, 5, 6\n"
                )
            return user_input
        except ValueError as e:
            tblok = (
                f"User entered: {raw}\n"
                f"***Input error: {e}\n"
                f"Please try again.\n\n"
            )
            slow_tblok(tblok)
            tblok = ""
            time.sleep(1)


# __________ Classes __________
# ------ Decorator Class ------


class TimingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        start_datetime = datetime.datetime.now()
        try:
            result = self.func(*args, **kwargs)
            return result
        finally:
            end_time = time.time()
            end_datetime = datetime.datetime.now()
            run_time = (end_time - start_time)
            run_datetime = (end_datetime - start_datetime)
            print(
                f"Results (time module):      {run_time:.6f}s\n"
                f"Results (datetime module):  {run_datetime}"
            )


# ------ Demo Class ------


class FunExample():
    def __init__(self, result):
        self.result = result

    @staticmethod
    def run_func(test_battery):
        for method in test_battery:
            method()


# ______ Intense Functions ______
# 1) Calculate the Factorial


@TimingDecorator
def my_fun():
    factor = factorial(100000)
    return factor


# 2) Matrix permanent (n! terms, #P-complete)


@TimingDecorator
def found_fun_01(A):
    n = len(A)
    return sum(prod(A[i][p[i]] for i in range(n)) for p in permutations(range(n)))


# 3) Brute-force TSP tour (n! permutations)


@TimingDecorator
def found_fun_02(D):
    n = len(D)
    return min(sum(D[p[i]][p[(i+1) % n]] for i in range(n)) for p in permutations(range(n)))


# 4) Naive recursive Fibonacci (exponential baseline)


@TimingDecorator
def found_fun_03(n):
    return n if n < 2 else found_fun_03(n-1) + found_fun_03(n-2)


# _______ The Program _______
# ------ Main Function ------


def main():
    # Arguments for functions
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    D = [
        [0,  2,  9, 10],
        [1,  0,  6,  4],
        [15, 7,  0,  8],
        [6,  3, 12,  0],
    ]
    # Helper Functions

    def _run_fun():
        return my_fun()

    def _run_permanent():
        return found_fun_01(A)

    def _run_tsp():
        return found_fun_02(D)

    def _run_fib():
        return found_fun_03(32)
    # ------ Function Tuple ------
    test_battery = (
        _run_fun,
        _run_permanent,
        _run_tsp,
        _run_fib,
    )
    run = True
    while run == True:
        sel = None
        menu = (
            f"{'=' * 50}"
            f"{'\n' * 3}"
            f"Please select an option:"
            f"{'\n' * 2}"
            f"1. Run All\n"
            f"2. Run Factorial\n"
            f"3. Run Matrix Permanent\n"
            f"4. Run Brute-Force TSP Tour\n"
            f"5. Run Naive Recursive Fibonacci"
            f"6. Quit"
            f"{'\n' * 2}"
        )
        slow_tblok(menu)
        time.sleep(1)
        sel = accept_input()

        if sel == 1:
            tblok = (
                f"Running All Functions\n\n"
            )
            slow_tblok(tblok)
            tblok = ""
            FunExample.run_func(test_battery)

        elif sel == 2:
            tblok = (
                f"Running Factorial\n\n"
            )
            slow_tblok(tblok)
            tblok = ""
            my_fun()
        elif sel == 3:
            tblok = (
                f"Running Matrix permanent (n! terms, #P-complete)\n\n"
            )
            slow_tblok(tblok)
            tblok = ""
            found_fun_01(A)
        elif sel == 4:
            tblok = (
                f"Running Brute-force TSP tour (n! permutations)\n\n"
            )
            slow_tblok(tblok)
            tblok = ""
            found_fun_02(D)
        elif sel == 5:
            tblok = (
                f"Running Naive recursive Fibonacci (exponential baseline)\n\n"
            )
            slow_tblok(tblok)
            tblok = ""
            found_fun_03(32)
        elif sel == 6:
            run = False
        else:
            raise ValueError


# ------ Run Guard ------
if __name__ == "__main__":
    main()
