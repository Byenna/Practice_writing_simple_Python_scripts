# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**3 ...write a script that asks the user to enter an integer and then determines whether the number is even or odd. And prints an appropriate message to the console.** 

Step 1: Prompt the user for input
Use the input() function to ask the user to enter an integer. Store the user input in a variable, let's call it "number".

`number = input("Enter an integer: ")`

Step 2: Convert the input to an integer
Since the input() function returns user input as a string, we need to convert "number" to an integer using the int() function. Assign the converted integer back to the "number" variable.

`number = int(number)`

Step 3: Check if the number is even or odd
To determine whether the number is even or odd, we can use the modulo operator (%). If "number" % 2 is equal to 0, it means the number is even. Otherwise, it's odd.

Step 4: Print the result.
Use print() to display an appropriate message to the console based on whether the number is even or odd.


```
if number % 2 == 0:
    # Step 4: Print the result
    print(number, "is even.")
else:
    # Step 4: Print the result
    print(number, "is odd.")
```

Hope that helps! Let me know if you have any further questions.