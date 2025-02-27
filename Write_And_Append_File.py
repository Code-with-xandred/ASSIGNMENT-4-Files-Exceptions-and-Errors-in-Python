
def write_and_append_to_file():
    first_input = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(first_input + '\n')  
    print("Data successfully written to output.txt")

    additional_input = input("\nEnter additional text to append: ")
    with open('output.txt', 'a') as file:
        file.write(additional_input + '\n')  
    print("Data successfully appended.")

    with open('output.txt', 'r') as file:
        print("\nFinal content of output.txt:")
        for line in file:
            print(line.rstrip()) 

write_and_append_to_file()