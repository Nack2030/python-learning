iterations = int(input("Please enter the number of students: "))
i = 1
while i <= iterations:
    try:
        name = input("Enter the student's name: ")
        marks = int(input("Enter the student's marks: "))
    
        if marks >= 90:
            print(f"{name} has scored {marks} on 100 and secure an A grade")
        elif 75 <= marks < 90:
            print(f"{name} has scored {marks} on 100 and secure a B grade")
        elif 60 <= marks < 75:
            print(f"{name} has scored {marks} on 100 and secure a C grade")
        elif 40 <= marks < 60:
            print(f"{name} has scored {marks} on 100 and secure a D grade")
        else:
            print(f"{name} has scored {marks} on 100 and failed")
    except ValueError:
        print(f"Invalid marks entered, going to next student")
    i += 1
