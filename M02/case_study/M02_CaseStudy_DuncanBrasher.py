from typing import Callable

__author__ = "Duncan Brasher"
__filename__ = "M02_CaseStudy_DuncanBrasher.py"
"""
As directed on IvyLearn (https://ivylearn.ivytech.edu/courses/1241113/assignments/19822231):
    ask for and accept a student's last name.
    quit processing student records if the last name entered is 'ZZZ'.
    ask for and accept a student's first name.
    ask for and accept the student's GPA as a float.
    test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
    test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
"""


def str_isfloat(txt: str) -> bool:
    """
    This is necessary because `str.isdigit` annoyingly returns false if the value is a float (ie has a decimal point)
    """
    try:
        _ = float(txt)
    except ValueError:
        return False
    return True


def get_input(msg: str = "Please enter a value", prompt: str = "\n> ", err_msg: str = "Invalid input, please try again", msg_suffix: str = " or press <Ctrl>-C to quit", check: Callable = lambda txt: txt is not None) -> str | None:
    _msg_suffix = msg_suffix+prompt
    txt = input(msg+_msg_suffix)
    while not check(txt):
        txt = input(err_msg+_msg_suffix)
    return txt if check(txt) else None


def main(args: list[str] = []) -> int:
    try:
        lname = get_input(msg="Please enter the student\'s last name")
        if lname.lower() == "zzz":
            print(f"Last name is three Z\'s ({lname}), exiting with code 1")
            return 1
        fname = get_input(msg="Please enter the student\'s first name")
        fullname = f"{fname} {lname}"
        gpa = float(get_input(msg="Please enter the student\'s GPA", check=lambda txt: txt is not None and str_isfloat(txt)))

        if gpa >= 3.5:
            print(f"{fullname} has made the Dean\'s List.")
        if gpa >= 3.25:
            print(f"{fullname} has made the Honor Roll.")

        return 0
    except KeyboardInterrupt:
        print("Received KeyboardInterrupt, exiting with code 0.")
        return 0


if __name__ == "__main__":
    from sys import argv
    exit(main(argv))

