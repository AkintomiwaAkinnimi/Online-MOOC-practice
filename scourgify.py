import sys
import csv


if len(sys.argv) ==  3:
    if sys.argv[1][-3:] == 'csv' and sys.argv[2][-3:] == 'csv':
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                students = []
                with open(sys.argv[2], "a") as file2:
                    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in reader:
                        students.append({"name": row["name"], "house": row["house"]})
                    for student in students:
                        student['lastname'], student['firstname'] = student['name'].split(",")
                        student['firstname'] = student['firstname'].lstrip()
                        writer.writerow({"first": student['firstname'], "last": student['lastname'], "house": student['house']})
        except FileNotFoundError:
            sys.exit(f"Could not find {sys.argv[1]}")
    elif sys.argv[1][-3:] != 'csv' and sys.argv[2][-3:] != 'csv':
         sys.exit("Not a csv file")
elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
print(students)
