#Author: Josiah Thacker
#File Name: M02_Lab-CaseStudy.py
#Description: This app accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.

while True:
    last_name = input("Enter student's last name: ")
    if last_name == "ZZZ":
        print("Requests Ended")
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")


