# Practice_writing_simple_Python_scripts
A few hands-on exercises to help you practice writing simple Python scripts

# A step by step guide on how to...

**2 ...write a script that asks the user to enter a temperature in Celsius and converts it to Fahrenheit using the provided formula:**

Step 1: Prompt the user to enter the temperature in Celsius
Use the 'input()' function to get the user's input. Display a prompt message asking the user to enter a temperature in Celsius and store the input in a variable called 'celsius':

`celsius = float(input("Please enter the temperature in Celsius: "))`

The `float()` function is used to convert the user's input into a floating-point number.
Step 2: Convert the temperature to Fahrenheit
Apply the conversion formula, `F = (C * 9/5) + 32`, where `F` is the temperature in Fahrenheit and `C` is the temperature in Celsius. Calculate the temperature in Fahrenheit and store it in a variable called `fahrenheit`:

`fahrenheit = (celsius * 9/5) + 32`

Step 3: Print the converted temperature
Print the converted temperature in Fahrenheit using a formatted message. For example:

`print(f"The temperature in Fahrenheit is: {fahrenheit} degrees")`

Putting it all together:
Here's the complete script:

```
celsius = float(input("Please enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit} degrees")
```

When you run this script, it will prompt the user for a temperature in Celsius, convert it to Fahrenheit, and then display the converted temperature.
I hope this helps you write the script you need! Let me know if you have any further questions or need any additional assistance.