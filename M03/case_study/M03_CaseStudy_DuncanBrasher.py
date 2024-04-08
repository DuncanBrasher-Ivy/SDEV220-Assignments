from typing import Callable

__author__ = "Duncan Brasher"
__filename__ = "M03_CaseStudy_DuncanBrasher.py"
"""
As directed on IvyLearn (https://ivylearn.ivytech.edu/courses/1241113/assignments/19822235)

Write a Python app that has the following classes:

    A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
    A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
        year
        make
        model
        doors (2 or 4)
        roof (solid or sun roof).
    Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
    The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
    The app will then output the data in an easy-to-read and understandable format, such as this:
      Vehicle type: car
      Year: 2022
      Make: Toyota
      Model: Corolla
      Number of doors: 4
      Type of roof: sun roof
"""


class Vehicle():
    def __init__(self, vtype: str) -> None:
        super().__init__()
        self.vtype: str = vtype


class Automobile(Vehicle):
    def __init__(self, vtype: str, year: str, make: str, model: str, doors: str, roof: str) -> None:
        super().__init__(vtype)

        self.year: str = year
        self.make: str = make
        self.model: str = model
        self.doors: str = doors
        self.roof: str = roof

    def __repr__(self) -> str:
        return f"""Vehicle type: {self.vtype}
Year: {self.year}
Make: {self.make}
Model: {self.model}
Number of doors: {self.doors}
Type of roof: {self.roof}"""


def get_input(msg: str = "Please enter a value", prompt: str = "\n> ", err_msg: str = "Invalid input, please try again", msg_suffix: str = " or press <Ctrl>-C to quit", check: Callable = lambda txt: txt is not None) -> str | None:
    _msg_suffix = msg_suffix+prompt
    txt = input(msg+_msg_suffix)
    while not check(txt):
        txt = input(err_msg+_msg_suffix)
    return txt if check(txt) else None


def main(args: list[str] = []) -> int:
    auto = Automobile(get_input("Vehicle type"), get_input("Year"), get_input("Make"), get_input("Model"), get_input("Number of doors"), get_input("Type of roof"))
    print(auto)
    return 0


if __name__ == "__main__":
    from sys import argv
    exit(main(argv))

