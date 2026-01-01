ui = input("Enter text to write to the file: ")

with open("C:/Users/patel/OneDrive/Desktop/wix images/output.txt", "w") as file:
    file.write(ui + "\n")

print("Data entered successfully to output.txt")

ai = input("\nEnter additional text to append: ")

with open("C:/Users/patel/OneDrive/Desktop/wix images/output.txt", "a") as file:
    file.write(ai + "\n")

print("\nFinal content of output.txt:")
with open("C:/Users/patel/OneDrive/Desktop/wix images/output.txt", "r") as file:
    for line in file:
        print(line.strip())
