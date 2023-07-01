# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**4 ...Write a script that asks the user to enter a series of numbers (separated by commas) and calculates the sum of those numbers. And prints the sum to the console.**


Step 1: Prompt the user for input
Use the input() function to ask the user to enter a series of numbers separated by commas. Store the user input in a variable, let's call it "numbers_input".

Step 2: Split the input into a list of numbers
Use the split() function to split "numbers_input" into a list of individual numbers. Pass "," as the argument to split() to separate the numbers based on the commas. Assign the resulting list to a variable, let's call it "numbers_list".

Step 3: Convert the list of numbers to integers
Loop through each number in "numbers_list" and convert them to integers using the int() function. Replace the original string values in "numbers_list" with the converted integers.

Step 4: Calculate the sum of the numbers
Use the sum() function to calculate the sum of all the numbers in "numbers_list". Assign the sum to a variable, let's call it "sum_of_numbers".

Step 5: Print the result
Use the print() function to display the sum of the numbers to the console.
Here's the complete script:


# Step 1: Prompt the user for input
numbers_input = input("Enter a series of numbers separated by commas: ")

# Step 2: Split the input into a list of numbers
numbers_list = numbers_input.split(",")

# Step 3: Convert the list of numbers to integers
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

# Step 4: Calculate the sum of the numbers
sum_of_numbers = sum(numbers_list)

# Step 5: Print the result
print("The sum of the numbers is:", sum_of_numbers)
