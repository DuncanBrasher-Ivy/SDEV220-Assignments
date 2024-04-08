from typing import Callable


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

