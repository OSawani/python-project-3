# Functions used across the project. 
# This include input validation, error handling, and any other reusable code.

def validate_input(user_input, expected_type, range=None):
    """
    Validates the user input.

    :param user_input: The input to validate
    :param expected_type: The type that the input is expected to be
    :param range: An optional range (inclusive) for numeric inputs
    :return: (bool, any) A tuple where the first element is a boolean indicating
             if the input is valid, and the second element is the converted input
             or an error message.
    """
    try:
        # Convert input to expected type
        converted_input = expected_type(user_input)
        # Check if input is within the specified range
        if range and not (range[0] <= converted_input <= range[1]):
            return False, "Input is out of range."
        return True, converted_input
    except ValueError:
        return False, "Invalid input type."
