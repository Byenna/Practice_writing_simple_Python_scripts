# Prompt the user to enter the temperature in Celsius Use the 'input()' function to get the user's input.

celcius = float(input("Please enter the temperature in Celsius: "))

# Convert the temperature to Fahrenheit and store it in a variable called fahrenheit:

farenheit = (celcius * 9/5) + 32

# Print the converted temperature

print(f"The temperature in Farenheit is: {farenheit} degrees.")