# Problem - File Input and Output

In this exercise, you will work with file operations such as opening, appending, and reading a file. You will create functions to handle these operations and ensure they work correctly by using Python's file handling features.

## Instructions

Modify `file_input_and_output.py` to complete the following functions:

1. **open_file**: Open a file and return its file object.
2. **append_to_file**: Append a line of text to the file.
3. **print_foods**: Print specific lines (19 to 23) from the file.

### Expected Input/Output

1. **open_file**:
    - Input: `food.txt`
    - Output: The function should open the file and return the file object.

2. **append_to_file**:
    - Input: `Rice`
    - Output:
      ```
      Line appended successfully.
      ```

3. **print_foods**:
    - Input: `wethinkcode.txt`
    - Output:
      ```
      Code,
      Bootcamp
      2023
      !
      ```

## To Run

To run the program, use the following command:
```bash
python3 file_input_and_output.py
```

## To Test

You can test the functions by running the test cases in `file_input_and_output_test.py`. The tests will check that the file operations work as expected.

1. To run all unit tests:
   ```bash
   python3 -m unittest file_input_and_output_test.py
   ```

2. To run specific tests:
   - Test `open_file`:
     ```bash
     python3 -m unittest file_input_and_output_test.TestExercise05.test_open_file
     ```
   - Test `append_to_file`:
     ```bash
     python3 -m unittest file_input_and_output_test.TestExercise05.test_append_to_file
     ```
   - Test `print_foods`:
     ```bash
     python3 -m unittest file_input_and_output_test.TestExercise05.test_print_foods
     ```

**Note**: Ensure your code passes all the tests to confirm correct implementation of file handling.
