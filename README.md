# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**5 ...Write a script that asks the user to enter a string and then prints the reverse of that string.**

Step 1: Prompt the user for input
Use the input() function to ask the user to enter a string. Store the user input in a variable, let's call it "input_string".

Step 2: Reverse the string
To reverse the string, you can use string slicing. Use "input_string[::-1]" to create a reversed version of the original string and assign it to a new variable, let's call it "reversed_string".

Step 3: Print the reversed string
Use the print() function to display the reversed string to the console.
Here's the complete script:

# Step 1: Prompt the user for input
input_string = input("Enter a string: ")

# Step 2: Reverse the string
reversed_string = input_string[::-1]

# Step 3: Print the reversed string
print("Reversed string:", reversed_string)