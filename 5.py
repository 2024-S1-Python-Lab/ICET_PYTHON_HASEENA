filename=input("enter file name")
try:
    with open(filename,'r')as file1:
        lines=file1.readlines()
    lines=[line.strip() for line in lines]
    print("lines from the file:",lines)
except FileNotFoundError:
        print(f"Error:the file'{filename}'does not exist.")
