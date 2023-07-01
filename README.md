# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**6 ...write a script that asks the user to enter an integer and calculates its factorial. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. Print the factorial to the console.**

Step 1: Prompt the user for input
Use the input() function to ask the user to enter an integer. Store the user input in a variable, let's call it "number".

Step 2: Convert the input to an integer
Since the input() function returns user input as a string, we need to convert "number" to an integer using the int() function. Assign the converted integer back to the "number" variable.

Step 3: Calculate the factorial
To calculate the factorial of a number, we can use a loop. Initialize a variable called "factorial" to 1. Then, use a for loop to iterate from 1 to "number" (inclusive). Multiply "factorial" by each number in the loop and update the value of "factorial" in each iteration.

Step 4: Print the result
Use the print() function to display the factorial to the console.
Here's the complete script:

# Step 1: Prompt the user for input
number = input("Enter an integer: ")

# Step 2: Convert the input to an integer
number = int(number)

# Step 3: Calculate the factorial
factorial = 1
for i in range(1, number + 1):
    factorial *= i

# Step 4: Print the result
print("The factorial of", number, "is:", factorial)

That's it! The script will prompt the user for an integer, calculate its factorial, and then print the factorial to the console. Let me know if you have any further questions.