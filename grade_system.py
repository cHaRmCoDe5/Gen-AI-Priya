while True:
    user_input = input("Enter a mark (0-100) or 'q' to quit: ")

    if user_input.lower() == 'q':
        print("Program ended.")
        break

    try:
        mark = float(user_input)

        if mark < 0 or mark > 100:
            print("Invalid mark. Please enter a value between 0 and 100.")
        else:
            if mark >= 90:
                grade = "A"
            elif mark >= 80:
                grade = "B"
            elif mark >= 70:
                grade = "C"
            elif mark >= 60:
                grade = "D"
            else:
                grade = "E"

            print(f"Entered mark: {mark}")
            print(f"Grade: {grade}")

    except ValueError:
        print("Invalid mark. Please enter a value between 0 and 100.")