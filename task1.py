try:
    with open("C:/Users/patel/OneDrive/Desktop/wix images/sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
