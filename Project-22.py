students = []

while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("1- show list of students")
    print("2- add a new student")
    print("3- exit")

    menu = int(input("Enter your choice: "))

    if menu == 3:
        print("Goodbye")
        break

    if menu == 2:
        student_number = int(input("Enter student's number: "))
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")

        total_score = 0
        total_units = 0

        while True:
            course_name = input("Enter student's course name: ")
            units = int(input("Enter this course's units: "))
            score = float(input("Enter student's score in this course: "))

            total_score += score * units
            total_units += units

            answer = input("Do you want to add another course? (yes/no): ")
            if answer.lower() == "no":
                break

        total_average_score = total_score / total_units

        students.append({
            "student_number": student_number,
            "first_name": first_name,
            "last_name": last_name,
            "score": total_average_score
        })

        print(f"{first_name} {last_name}'s score is {total_average_score}")

    if menu == 1:
        sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
        print("# First name Last name => Score")
        rank = 1
        for student in sorted_students:
            print(f"{rank}. {student['first_name']} {student['last_name']} => {student['score']}")
            rank += 1
