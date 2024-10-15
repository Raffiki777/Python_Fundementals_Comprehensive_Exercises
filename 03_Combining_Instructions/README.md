# Problem - Combining Instructions

In this exercise, you will work on combining multiple Python concepts such as conditionals, functions, and input handling to solve problems. The tasks will focus on finding the maximum of three numbers and checking if a number falls within a specific range.

## Instructions

Modify `combining_instructions.py` to complete the following functions:

1. **max_three**: Determine the maximum of three numbers entered by the user. 
2. **between_3_and_9**: Check whether a given number falls between 3 and 9.

### Expected Input/Output

1. **max_three**:
    - Input:
      ```
      3
      8
      6
      ```
    - Output:
      ```
      The max of the three numbers is: 8
      ```

2. **between_3_and_9**:
    - Input: `5`
    - Output: `5 is in the range`

    - Input: `2`
    - Output: `The number is outside the given range.`

## To Run

To run the program, use the following command:
```bash
python3 combining_instructions.py
```

## To Test

You can test the functions by running the test cases in `combining_instructions_test.py`. The tests will verify the correctness of your implementation.

1. To run all the unit tests:
   ```bash
   python3 -m unittest combining_instructions_test.py
   ```

2. To run specific tests:
   - Test the `max_three` function:
     ```bash
     python3 -m unittest combining_instructions_test.TestExercise03.test_max_three
     ```
   - Test the `between_3_and_9` function:
     ```bash
     python3 -m unittest combining_instructions_test.TestExercise03.test_between_3_and_9
     ```

**Note**: Ensure that all tests pass to confirm that your code works correctly.
