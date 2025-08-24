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
