# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**7 ...write a script that asks the user to enter the number of terms they want in the Fibonacci sequence and then prints the sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The sequence starts with 0 and 1.**


Step 1: Prompt the user for input
Use the input() function to ask the user to enter the number of terms they want in the Fibonacci sequence. Store the user input in a variable, let's call it "num_terms".

Step 2: Convert the input to an integer
Since the input() function returns user input as a string, we need to convert "num_terms" to an integer using the int() function. Assign the converted integer back to the "num_terms" variable.

Step 3: Calculate the Fibonacci sequence
To generate the Fibonacci sequence, create an empty list called "sequence" to store the sequence. Initialize two variables, "first" and "second", to 0 and 1 respectively, which represents the first two terms of the sequence. Use a for loop to iterate "num_terms" times. In each iteration, append "first" to the "sequence" list, then update the values of "first" and "second" by swapping them.

Step 4: Print the sequence
Use the print() function to display the Fibonacci sequence to the console.
Here's the complete script:

# Step 1: Prompt the user for input
num_terms = input("Enter the number of terms in the Fibonacci sequence: ")

# Step 2: Convert the input to an integer
num_terms = int(num_terms)

# Step 3: Calculate the Fibonacci sequence
sequence = []
first = 0
second = 1
for _ in range(num_terms):
    sequence.append(first)
    first, second = second, first + second

# Step 4: Print the sequence
print("Fibonacci sequence:")
for term in sequence:
    print(term, end=" ")

That's it! The script will prompt the user for the number of terms they want in the Fibonacci sequence, generate the sequence, and then print it to the console. Let me know if you have any further questions.