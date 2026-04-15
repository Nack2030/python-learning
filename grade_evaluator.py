try:
    name = input("Enter the student's name: ")
    marks = int(input("Enter the student's marks out of 100: "))
    
    if marks >= 90:
        print(f"{name} scored {marks} and got an A grade")
    elif 75 <= marks < 90:
        print(f"{name} scored {marks} and got a B grade")
    elif 60 <= marks < 75:
        print(f"{name} scored {marks} and got a C grade")
    elif 40 <= marks < 60:
        print(f"{name} scored {marks} and got a D grade")
    else:
        print(f"{name} scored {marks} and unfortunately failed")
    
except ValueError:
    print("Please enter a valid number for marks")
