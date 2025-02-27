# ASSIGNMENT-4-Files-Exceptions-and-Errors-in-Python

Task 1 Functionality:

This Python program defines a function read_file that takes a filename and reads the file’s contents, displaying each line with a line number. It uses a try-except block to manage errors. Within try, it opens the file, iterates over lines using enumerate starting at 1, and prints them with rstrip() to remove trailing newlines. If the file isn’t found, the except FileNotFoundError block outputs an error message with the filename. Called with read_file('sample.txt'), it either lists 'sample.txt'’s contents or reports it’s missing. It’s a straightforward tool for reading text files.

------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2 Functionality:

The Python function write_and_append_to_file() manages file operations in three steps. First, it takes user input and writes it to 'output.txt' in write mode ('w'), overwriting existing content, then confirms success. Next, it takes more input and appends it to the file in append mode ('a'), adding to the end, and confirms again. Finally, it reads and displays the file's contents in read mode ('r'), printing each line without trailing newlines using rstrip(). The result is a file with two lines: the initial and additional inputs, displayed to the user.


______________________________________________________________________________________________________________________________________________________________
