try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found. creating a new one...")
    with open("missing_file.txt", "w") as file:
        file.write("Problem solved.")
print("Program finished.")