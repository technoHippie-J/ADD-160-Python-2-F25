import time
import datetime
from math import factorial, prod
from itertools import permutations
# ********** DO NOT DO THE FOLLOWING IN PRODUCTION ENV **********
import sys
try:
    # just above ~456,574 needed for 100000
    sys.set_int_max_str_digits(600_000)
except AttributeError:
    # Older Python (<3.11) doesn’t have this guard
    pass

# ______ Helper Functions ______
# ------ Slow-Text Helper ------

# print speed knob
PRINT_DELAY = 0.15

# slow text block print speed function


def slow_tblok(text):
    for line in text.splitlines():
        time.sleep(PRINT_DELAY)
        print(line)


# ------ Input Function ------


def accept_input():
    """
    Helper function that safely grabs user input, cleans, and validates.
    Does not make a decision other than raising a ValueError if bad input.
    Only cleans, validates, and delivers the input.

    Raises:
        ValueError: Input must be 1, 2, 3, 4, 5, 6

    Returns:
        user_input: user's menu decision
    """
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
    """
    When called, it:
        - Begins the timer, recording the time to a variable using the time module
        - Begins the timer, recording the time to a variable using the datetime module
            * Both modules used to experiment with the difference
        - Begins error checking try/finally block (no time to solve exception logic, to be immplemented)
        - Returns result of function
        - Then records the stop time to a variable using the time module
        - Records the stop time to a variable using the datetime module
        - Print results
    """

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
    """
    Class with method that runs the battery of tests. Static method is
    used to give access without instantiating the class
    """

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
    """
    Calculates the factorial of 100000.
    """
    factor = factorial(100000)
    return factor


# 2) Matrix permanent (n! terms, #P-complete)


@TimingDecorator
def found_fun_01(A):
    """
    *Product of ChatGPT*
    """
    n = len(A)
    return sum(prod(A[i][p[i]] for i in range(n)) for p in permutations(range(n)))


# 3) Brute-force TSP tour (n! permutations)


@TimingDecorator
def found_fun_02(D):
    """
    *Product of ChatGPT*
    """
    n = len(D)
    return min(sum(D[p[i]][p[(i+1) % n]] for i in range(n)) for p in permutations(range(n)))


# 4) Naive recursive Fibonacci (exponential baseline)


@TimingDecorator
def found_fun_03(req_index):
    """
    *Product of ChatGPT*
    """
    # Nested function prevents recursively calling the @TimingDecorator each recursion (original form printed each recursion)
    def _fib(sub_index):
        return sub_index if sub_index < 2 else _fib(sub_index - 1) + _fib(sub_index - 2)
    return _fib(req_index)


# 4b) Fib Helper Function (counts digits)


# _______ The Program _______
# ------ Main Function ------


def main():
    # Matrices for functions
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
    # ------ Helper Functions ------
    # I wanted to iterate over a tuple,
    # and I was stubborn on that point.
    # Doing this allows me to use a tuple without
    # calling the method when building the tuple.

    def _run_fun():
        tblok = (
            f"{'=' * 60}"
            f"{'\n' * 2}"
            f"Running Factorial"
            f"{'\n' * 2}"
        )
        slow_tblok(tblok)
        tblok = ""
        result_factor = my_fun()
        length = len(str(result_factor))
        tblok = (
            f"{'\n' * 2}"
            f"- Result: The factorial of 100,000 is {length} digits long."
            f"{'\n' * 2}"
        )
        slow_tblok(tblok)

    def _run_permanent():
        tblok = (
            f"{'=' * 60}"
            f"{'\n' * 2}"
            f"- Running Matrix permanent (n! terms, #P-complete)"
            f"{'\n' * 2}"
        )
        slow_tblok(tblok)
        tblok = ""
        result_matrix = found_fun_01(A)
        tblok = (
            f"\nResult: {result_matrix}\n\n"
        )
        slow_tblok(tblok)

    def _run_tsp():
        tblok = (
            f"{'=' * 60}"
            f"{'\n' * 2}"
            f"- Running Brute-force TSP tour (n! permutations)"
            f"{'\n' * 2}"
        )
        slow_tblok(tblok)
        tblok = ""
        result_tsp = found_fun_02(D)
        tblok = (
            f"\nResult: {result_tsp}\n\n"
        )
        slow_tblok(tblok)

    def _run_fib():
        tblok = (
            f"{'=' * 60}"
            f"{'\n' * 2}"
            f"- Running Naive recursive Fibonacci (exponential baseline)"
            f"{'\n' * 2}"
        )
        slow_tblok(tblok)
        tblok = ""
        result_fib = found_fun_03(32)
        tblok = (
            f"\nResult: {result_fib}\n\n"
        )
        slow_tblok(tblok)

    # ------ Function Tuple ------
    # Tuple containing the test battery helper
    # functions, so they are only called when iterated over

    test_battery = (
        _run_fun,
        _run_permanent,
        _run_tsp,
        _run_fib,
    )

    # ------ Menu Loop ------
    # Prints a 6 item menu then waits for user input by
    # calling the input helper when assigning to a variable.
    run = True
    while run == True:
        sel = None
        menu = (
            f"{'\n' * 2}"
            f"{'=' * 60}"
            f"{'\n' * 2}"
            f"Please select an option:"
            f"{'\n' * 2}"
            f"1. Run All\n"
            f"2. Run Factorial\n"
            f"3. Run Matrix Permanent\n"
            f"4. Run Brute-Force TSP Tour\n"
            f"5. Run Naive Recursive Fibonacci\n"
            f"6. Quit"
            f"{'\n' * 2}"
        )
        slow_tblok(menu)
        time.sleep(1)
        sel = accept_input()

        # if/elif/else block that calls the
        # function associated with user input.
        if sel == 1:
            tblok = (
                f"{'\n' * 2}"
                f"Running All Functions"
                f"{'\n' * 2}"
            )
            slow_tblok(tblok)
            tblok = ""
            FunExample.run_func(test_battery)

        elif sel == 2:
            _run_fun()

        elif sel == 3:
            _run_permanent()

        elif sel == 4:
            _run_tsp()

        elif sel == 5:
            _run_fib()

        elif sel == 6:
            run = False
        else:
            raise ValueError


# ------ Run Guard ------
if __name__ == "__main__":
    main()
