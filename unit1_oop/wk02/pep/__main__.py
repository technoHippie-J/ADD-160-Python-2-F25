"""
Python Best Practices Exercise
Below is a Python program that needs improvement to fit the best practices and guidelines we discussed. Copy and paste this code into your Python environment.

Original Python Program with Issues
def fx(a, b):
  if a > 0 and b > 0:
    if a > b:
      for i in range(b):
        print(a)
    else:
      for j in range(a):
        print(b)
  elif a == 0 or b == 0:
      return "Zero found"
  else:
      if a < b:
          return a - b
      else:
          return b - a
Follow these step-by-step directions to improve the code:

1. Make Names Meaningful:
    - Replace single-letter variables with meaningful names.
    - Rename the function to reflect its purpose.
2. Add Comments:
    - Explain the purpose of the function.
    - Describe the purpose of each major block of code.
3. Improve Spacing and Indentation:
    - Ensure consistent use of indentation (4 spaces per level).
    - Add blank lines to separate different parts of the code.
4. Simplify the Code:
    - Reduce nesting levels by refactoring the logic.
    - Simplify conditionals where possible.
5. Add Docstrings:
    - Add a docstring to the function to describe its behavior.
6. Handle Errors Gracefully:
    - Add error handling for unexpected inputs.
7. Hand in your updated code by uploading it to GitHub and submitting the link.
"""

# Test Values
value_a = 15
value_b = 10


def repeat_or_nonpos(value_a, value_b):
    """
    Repeating Value or Absolute Value Function
    - Takes two values, checks:
        - is int?
            - no->raise
        - is 0?
            -kill
        - both over 0?
            -get bigger and smaller
                -print bigger(smaller*)
        - otherwise, return non-positive difference (smaller-larger)
    """
    if not isinstance(value_a, int) or not isinstance(value_b, int):
        raise TypeError("Both inputs must be integers.")

    # Check for zero, kill if present
    if value_a == 0 or value_b == 0:
        return "Zero found"

    # Check if both values above 0, set larger and smaller,
    # print the larger number x times = to smaller
    if value_a > 0 and value_b > 0:
        larger = max(value_a, value_b)
        smaller = min(value_a, value_b)

        for i in range(smaller):
            print(larger)

        return None

    # Returns non-positive difference between the two values if one is negative
    return -abs(value_a - value_b)


def main():
    repeat_or_nonpos(value_a, value_b)


if __name__ == "__main__":
    main()
