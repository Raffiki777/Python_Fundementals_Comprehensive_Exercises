# Problem - Structuring Data

In this exercise, you will work with tuples and lists, along with functions that manipulate and evaluate these data structures. You will also implement a palindrome checker for strings. Follow the instructions to complete the tasks outlined below.

## Instructions

Modify `structuring_data.py` to complete the following functions:

1. **element_in_tuple**: Check whether an element exists in a tuple.
2. **list_to_tuple**: Convert a list to a tuple.
3. **length_of_tuple**: Find the length of a tuple.
4. **sum_of_list**: Return the sum of all numbers in a list.
5. **multiply_list**: Return the product of all numbers in a list.
6. **unique_list**: Return a new list with unique elements from the input list.
7. **palindrome**: Check if a string is a palindrome.

### Expected Input/Output

1. **element_in_tuple**:
    - Input: `r` and `5`
    - Output:
      ```
      Enter r:
      True
      Enter 5:
      False
      ```

2. **list_to_tuple**:
    - Output:
      ```
      [5, 10, 7, 4, 15, 3]
      (5, 10, 7, 4, 15, 3)
      ```

3. **length_of_tuple**:
    - Output:
      ```
      ('W', 'e', 'T', 'h', 'i', 'n', 'k', 'C', 'o', 'd', 'e')
      11
      ```

4. **sum_of_list**:
    - Input: `(1, 5, 43, 2, 23)`
    - Output: `74`

5. **multiply_list**:
    - Input: `(1, 5, 4, -2, 23)`
    - Output: `-920`

6. **unique_list**:
    - Input: `[1, 1, 5, 5, 4, -2, 23, 7, 7, 7]`
    - Output: `[1, 5, 4, -2, 23, 7]`

7. **palindrome**:
    - Input: `racecar`
    - Output: `True`

## To Run

To run the main program, use the following command:
```bash
python3 structuring_data.py
```

## To Test

You can test the functions by running the test cases in `structuring_data_test.py`. The test cases will ensure that each function works as expected.

1. To run all unit tests:
   ```bash
   python3 -m unittest structuring_data_test.py
   ```

2. To run specific tests:
   - Test `element_in_tuple`:
     ```bash
     python3 -m unittest structuring_data_test.TestExercise04.test_element_in_tuple
     ```
   - Test `list_to_tuple`:
     ```bash
     python3 -m unittest structuring_data_test.TestExercise04.test_list_to_tuple
     ```
   - Test `length_of_tuple`:
     ```bash
     python3 -m unittest structuring_data_test.TestExercise04.test_length_of_tuple
     ```
   - Test `sum_of_list`:
     ```bash
     python3 -m unittest structuring_data_test.TestExercise04.test_sum_of_list
     ```
   - Test `multiply_list`:
     ```bash
     python3 -m unittest structuring_data_test.TestExercise04.test_multiply_list
     ```
   - Test `unique_list`:
     ```bash
     python3 -m unittest structuring_data_test.TestExercise04.test_unique_list
     ```
   - Test `palindrome`:
     ```bash
     python3 -m unittest structuring_data_test.TestExercise04.test_palindrome
     ```

**Note**: Ensure all your code passes the tests for technical correctness.
