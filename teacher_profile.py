try:
    name = input("Enter your name")
    subject = input("Enter the subject you teach")
    experience = int(input("Enter your e=years of experience"))
    age = int(input("Enter your age"))
    retirement_age = int(input("Enter retirement age"))

    print(f"You are {name} of age {age}. You've been teaching {subject} for {experience} years retiring in {retirement_age - age} years")
except ValueError:
    print("age and retirement must be numbers not words")
