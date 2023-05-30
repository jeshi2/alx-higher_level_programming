## General
Why Python programming is awesome
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception

## Explanation Code
### 0-safe_print_list.py
* The safe_print_list function takes two arguments: my_list, which is the input list, and x, which represents the number of elements to print.
* Inside the function, we use a try-except block to handle any potential IndexError that may occur if the value of x is greater than the length of my_list.
* We initialize a variable count to keep track of the number of elements printed.
* We iterate x times using a for loop and print each element of my_list using indexing. If an IndexError occurs, we catch it with the except block and simply pass, as we are done printing the elements available in the list.
* Finally, we print a new line character and return the value of count, representing the number of elements actually printed.

### 1-safe_print_integer.py
* The safe_print_integer function takes one argument, value, which can be of any type.
* Inside the function, we use a try-except block to handle two potential exceptions:
* ValueError: If the value cannot be converted to an integer format using "{:d}".format().
* TypeError: If the value is not of a type that can be converted to an integer.
* Within the try block, we use "{:d}".format(value) to format and print value as an integer.
* If the formatting and printing are successful, we return True, indicating that the value has been correctly printed as an integer.
* If an exception occurs, we catch it with the except block and return False, indicating that the value is not an integer.

### 2-safe_print_list_integers.py
* The safe_print_list_integers function takes two arguments: my_list, which is the input list, and x, which represents the number of elements to access in my_list.
* We initialize a variable count to keep track of the number of integers printed.
* Inside the function, we use a try-except block to handle the potential IndexError that may occur if the value of x is greater than the length of my_list.
* We iterate x times using a for loop and check if each element of my_list is an instance of an integer using the isinstance() function.
* If the element is an integer, we print it using "{:d}".format() to format it as an integer.
* If an IndexError occurs, we catch it with the except block and simply pass, as we are done accessing the elements available in the list.
* Finally, we print a new line character and return the value of count, representing the number of integers actually printed.

### 3-safe_print_division.py
* The safe_print_division function takes two arguments: a and b, which are the integers to be divided.
* Inside the function, we use a try-except-finally block to handle the division and print the result.
* We perform the division operation a / b inside the try block and store the result in the result variable.
* If a ZeroDivisionError occurs, we catch it with the except block and set the result variable to None.
* Finally, we print "Inside result: {}".format(result) to display the result of the division.
* We then return the value of result.

### 4-list_division.py
* The list_division function takes three arguments: my_list_1 and my_list_2, which are the input lists, and list_length, which represents the desired length of the resulting list.
* We initialize an empty list new_list to store the division results.
* Inside the function, we use a for loop to iterate list_length times and perform element-wise division.
* We use a try-except block to handle potential exceptions that may occur during the division.
* If a ZeroDivisionError occurs, we catch it with the first except block and set the quotient to 0. We also print "division by 0".
* If an IndexError occurs, it means that either my_list_1 or my_list_2 is too short. We catch the exception with the second except block, set the quotient to 0, and print "out of range".
* If a TypeError or ValueError occurs, it means that an element in either list is not an integer or float. We catch the exception with the third except block, set the quotient to 0, and print "wrong type".
* Finally, we append the quotient to new_list and return it after the for loop completes.

###  5-raise_exception.py
* The raise_exception function is a simple function that raises a TypeError exception.
* Inside the function, we use the raise keyword followed by the TypeError exception to raise the exception.

### 6-raise_exception_msg.py
* The raise_exception_msg function is a simple function that raises a NameError exception with a custom message.
* Inside the function, we use the raise keyword followed by the NameError exception, passing the message parameter as the argument to the exception.

### 100-safe_print_integer_err.py
* The safe_print_integer_err function takes a value as an argument and attempts to print it as an integer.
* Inside the function, we use a try-except block to handle any exceptions that may occur during the printing process.
* Within the try block, we use the "{:d}".format() syntax to format and print the value as an integer.
* If the value is successfully printed, we return True to indicate that the value is an integer and has been printed correctly.
* If an exception occurs during the printing, we catch it with the except block and print the error message to stderr using print() with the file=sys.stderr argument. We also return False to indicate that the value is not an integer and could not be printed correctly.

### 101-safe_function.py
* The safe_function function takes a function fct and any number of arguments *args.
* Inside the function, we use a try-except block to execute the function fct with the provided arguments.
* If the function executes successfully, we return the result.
* If an exception occurs during the execution, we catch it with the except block and print the error message to stderr using print() with the file=sys.stderr argument. We also return None to indicate that something went wrong during the function execution.

### 102-magic_calculation.py
* The function starts by initializing result to 0.
* It then enters a loop that iterates over the range from 1 to 4 (exclusive).
* Inside the loop, there is a try-except block.
* The try block compares i with a and raises an exception with the message 'Too far' if i is greater than a.
* If no exception is raised, it calculates (a ** b) / i and adds it to the result.
* In case an exception is raised, the except block is executed. It sets result to the sum of a and b and breaks out of the loop.
* After the loop, the function returns the final value of result.

# AUTHOR ANTONY EVANS
