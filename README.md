# Practice_writing_simple_Python_scripts
A few hands-on exercises to help you practice writing simple Python scripts

# A step by step guide on how to...

**1 ...write a script that asks the user for their name and then prints a greeting message with their name.** 

Here's an example of how you can do this using Python:

Step 1: Prompt the user to enter their name
To get the user's name, you can use the 'input()' function. It will allow you to display a prompt and wait for the user to enter their input. Let's assign their input to a variable called 'name':

`name = input("Please enter your name: ")`

Step 2: Print the greeting message
Once you have the user's name stored in the `name` variable, you can use string concatenation (or f-strings in Python 3.6+) to build the greeting message and print it to the console. For example:

`print("Hello, " + name + "! Nice to meet you!")`

Or using f-strings:

`print(f"Hello, {name}! Nice to meet you!")`

Putting it all together:
Here's the complete script:

`name = input("Please enter your name: ")`
`print(f"Hello, {name}! Nice to meet you!")`

When you run this script, it will ask the user for their name and print a greeting message with their name.
I hope this helps you write the script you need! Let me know if you have any further questions or need any additional assistance.