# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**8 ...write a script that asks the user to enter an integer and determines whether it is a prime number. A prime number is a natural number greater than 1 that is divisible only by 1 and itself. Print an appropriate message to the console.**


Step 1: Prompt the user for input

import math

Use the input() function to ask the user to enter an integer. Store the user input in a variable, let's call it "number".

Step 2: Convert the input to an integer
Since the input() function returns user input as a string, we need to convert "number" to an integer using the int() function. Assign the converted integer back to the "number" variable.

Step 3: Check if the number is prime
To determine if a number is prime, we can use a simple loop. Iterate through each number from 2 to the square root of "number" (inclusive). Check if "number" is divisible evenly by any number in the loop. If it is, the number is not prime; otherwise, it is prime.

Step 4: Print the result
Use the print() function to display an appropriate message to the console based on whether the number is prime or not.
Here's the complete script:

import math

# Step 1: Prompt the user for input
number = input("Enter an integer: ")

# Step 2: Convert the input to an integer
number = int(number)

# Step 3: Check if the number is prime
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

# Step 4: Print the result
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

    
That's it! The script will prompt the user for an integer, determine if it is a prime number or not, and inform the user with an appropriate message. Let me know if you have any further questions.