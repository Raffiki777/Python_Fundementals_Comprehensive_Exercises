# Problem - More Data Structures (Sets)

In this exercise, you will work with Python sets, focusing on adding, removing, and comparing elements within sets. You will write functions to manipulate the data in sets and explore operations such as printing, modifying, and calculating differences between sets.

## Instructions

Modify `more_data_structures.py` to complete the following functions:

1. **print_set**: Print the given set of names and numbers.
2. **remove_katlego**: Remove the name 'Katlego' from the set and print the new set.
3. **add_names**: Add the names 'Kyle' and 'Sihle' to the set and print the new set.
4. **difference**: Print the difference between two sets (`set_two` compared to `set_one`).

### Expected Output

1. **print_set**:
    - Output:
      ```
      {'Anele', 'Litha', 'Nontando', 39, 'Gomolemo', 'Tshegofatso', 'Tanatswa', 38, 'Monwabisi', 'Vuyisile', 'Dikeledi', 77, 'Rafiki'}
      ```

2. **remove_katlego**:
    - Output:
      ```
      {'Anele', 'Litha', 'Nontando', 39, 'Gomolemo', 'Tshegofatso', 'Tanatswa', 38, 'Monwabisi', 'Vuyisile', 'Dikeledi', 77, 'Rafiki'}
      ```

3. **add_names**:
    - Output:
      ```
      {'Anele', 'Litha', 'Nontando', 39, 'Gomolemo', 'Tshegofatso', 'Katlego', 'Tanatswa', 38, 'Monwabisi', 'Vuyisile', 'Dikeledi', 77, 'Rafiki', 'Kyle', 'Sihle'}
      ```

4. **difference**:
    - Output:
      ```
      {'Kyle', 'Tshegofatso'}
      ```

## To Run

To run the program, use the following command:
```bash
python3 more_data_structures.py
```

## To Test

You can test the functions by running the test cases in `more_data_structures_test.py`. The test cases will ensure the correct functionality of your set operations.

1. To run all unit tests:
   ```bash
   python3 -m unittest more_data_structures_test.py
   ```

2. To run specific tests:
   - Test `print_set`:
     ```bash
     python3 -m unittest more_data_structures_test.TestExercise06.test_print_set
     ```
   - Test `remove_katlego`:
     ```bash
     python3 -m unittest more_data_structures_test.TestExercise06.test_remove_
     ```
   - Test `add_names`:
     ```bash
     python3 -m unittest more_data_structures_test.TestExercise06.test_add_names
     ```
   - Test `difference`:
     ```bash
     python3 -m unittest more_data_structures_test.TestExercise06.test_difference
     ```

**Note**: Ensure that your code passes all tests to verify the correct implementation of set operations.
