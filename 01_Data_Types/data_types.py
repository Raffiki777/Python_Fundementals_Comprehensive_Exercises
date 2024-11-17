def boolean():
    """
    Question 1 - Boolean

    Using the variable below, give it the value 'True', then print it.
    """
    # enter your code here
    staying_alive = True
    return staying_alive

print(boolean())

def integer():
    """
    Question 2 - Integer

    Create a program to accept two numbers from a user and multiply them, then print the product.
    """

    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))

    result = num1 * num2
    return result
print(integer())

def string():
    """
    Question 3 - String

    Assign a name to the variable below and print it.
    """
    your_name = "Raffiki"
    return your_name
    
print(string())

def convert_to_float():
    """
    Question 4 - Float

    Convert the following integer to a float then print it.
    """
    int_num = float(60)

    return int_num

print(convert_to_float())

def all_data_types():
    """
    Question 5 - All Data Types

    Output the following sentence using the given variables.

    Welcome to the 2023 WeThinkCode_ bootcamp where True learning costs R0.00
    """

    string_one = "Welcome to the "
    string_two = " WeThinkCode_ bootcamp where "
    string_3 = " learning costs R"
    bool_condition = True
    int_year = 2023
    float_cost = 0.00

    sentence = print(f"{string_one}{int_year}{string_two}{bool_condition}{string_3}{float_cost}")
    return sentence

print(all_data_types())

if __name__ == "__main__":
    """
    Run the entire program from here
    """
    boolean()
    integer()
    string()
    convert_to_float()
    all_data_types()
