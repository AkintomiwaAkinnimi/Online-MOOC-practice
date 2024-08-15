import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #9:00 AM to 5:00 PM
    #9 AM to 5 PM
    if match := re.search(r"^([0-9]+):([0-9]+) (AM|PM) to ([0-9]+):([0-9]+) (AM|PM)$", s, re.IGNORECASE):
        if match.group(2):
            if int(match.group(2)) >= 60:
                raise ValueError
        if match.group(5):
            if int(match.group(5)) >= 60:
                raise ValueError
        hour1 = int(match.group(1))
        if match.group(3) == 'PM':
            hour1 += 12
        elif match.group(3) == 'AM' and hour1 == 12:
            hour1 -= 12
        minutes1 = match.group(2)
        hour2 = int(match.group(4))
        if match.group(6) == 'PM':
            hour2 += 12
        elif match.group(6) == 'AM' and hour1 == 12:
            hour2 -= 12
        minutes2 = match.group(5)
        time = f"{hour1}:{minutes1} to {hour2}:{minutes2}"
        return time
    elif clock := re.search(r"^([0-9]+) (AM|PM) to ([0-9]+) (AM|PM)", s, re.IGNORECASE):
        hour1 = int(clock.group(1))
        if clock.group(2) == 'PM':
            hour1 += 12
        elif clock.group(2) == 'AM' and hour1 == 12:
            hour1 -= 12
        hour2 = int(clock.group(3))
        if clock.group(4) == 'PM':
            hour2 += 12
        elif clock.group(4) == 'AM' and hour2 == 12:
            hour2 -= 12
        time = f"{hour1}:00 to {hour2}:00"
        return time
    else:
        raise ValueError


if __name__ == "__main__":
    main()
