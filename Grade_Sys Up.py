"""
Grade System - Convert marks to letter grades with improved code structure.
"""

# Grade thresholds and corresponding grades
GRADE_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "E")
]

# Grade feedback messages
GRADE_FEEDBACK = {
    "A": "Excellent performance!",
    "B": "Good performance!",
    "C": "Satisfactory performance.",
    "D": "Needs improvement.",
    "E": "Significant improvement needed."
}


def is_valid_mark(mark):
    """
    Check if mark is within valid range (0-100).
    
    Args:
        mark (float): The mark to validate
        
    Returns:
        bool: True if mark is valid, False otherwise
    """
    return 0 <= mark <= 100


def get_grade(mark):
    """
    Convert a mark to a letter grade.
    
    Args:
        mark (float): The mark to convert (0-100)
        
    Returns:
        str: Letter grade (A, B, C, D, or E)
    """
    for threshold, grade in GRADE_THRESHOLDS:
        if mark >= threshold:
            return grade
    return "E"


def get_mark_input():
    """
    Get and validate mark input from user.
    
    Returns:
        float or None: Valid mark (0-100) or None if user wants to quit
    """
    while True:
        user_input = input("Enter a mark (0-100) or 'q' to quit: ").strip()
        
        if user_input.lower() == 'q':
            return None
        
        try:
            mark = float(user_input)
            if is_valid_mark(mark):
                return mark
            else:
                print("Invalid mark. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


def display_grade_result(mark, grade):
    """
    Display the mark and corresponding grade with feedback.
    
    Args:
        mark (float): The entered mark
        grade (str): The corresponding grade
    """
    feedback = GRADE_FEEDBACK.get(grade, "")
    print(f"Entered mark: {mark}")
    print(f"Grade: {grade}")
    if feedback:
        print(f"Feedback: {feedback}")


def main():
    """Main program loop."""
    print("Welcome to the Grade System!")
    print("-" * 40)
    
    while True:
        mark = get_mark_input()
        
        if mark is None:
            print("-" * 40)
            print("Program ended. Thank you!")
            break
        
        grade = get_grade(mark)
        display_grade_result(mark, grade)
        print()


if __name__ == "__main__":
    main()