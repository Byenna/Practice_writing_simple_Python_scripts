# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**9 ...write a script that reads a text file (you can create a sample text file with some content) and prints its contents to the console.**


Step 1: Specify the file path
First, you need to specify the file path of the text file you want to read. Make sure the text file is in the same directory as your script, or you provide the full file path if it's located elsewhere. Let's say the file name is "sample.txt".

Step 2: Open and read the file
Use the open() function to open the file in read mode, and assign it to a variable, let's call it "file". Use the read() method on the file object to read the entire contents of the file and assign it to a variable, let's call it "contents".

Step 3: Print the contents
Use the print() function to display the contents of the file to the console.

Step 4: Close the file
After you have finished reading the file, use the close() method on the file object to close it and free up system resources.
Here's the complete script:

# Step 1: Specify the file path
file_path = "sample.txt"

# Step 2: Open and read the file
file = open(file_path, "r")
contents = file.read()

# Step 3: Print the contents
print(contents)

# Step 4: Close the file
file.close()

That's it! The script will read the contents of the specified text file and print them to the console. Let me know if you have any further questions.