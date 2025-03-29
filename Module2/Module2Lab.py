# Krystal Michaelis
# Module2Lab
# This app will take the student's first + last name along with the student's GPA and determine
# if the student has made the Dean's List, Honor Roll or neither.


def main():
    # Student's name inputs
    while True:
        last_name = input("Student's last name: ")
        if last_name.upper() == "ZZZ":
            print("Quitting the program.")
            break
        
        first_name = input("Student's first name: ")
        
    # GPA Input
    while True:
        try:
            gpa = float(input("Student's GPA: "))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                    print("Please enter a valid GPA between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. Please enter a numeric GPA.")
        
        # Determine GPA qualifications
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List nor Honor Roll.")

        print("-" * 50)  # Separator for readability

# Runs the program
if __name__ == "__main__":
    main()