import re
import sys

if len(sys.argv) == 2:
    print(f"IPv4 Address: {sys.argv[1].strip()}")
matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", sys.argv[1])
if matches:
    a, b, c, d = matches.groups()
    approved = list(range(256))
    if int(a) in approved and int(b) in approved and int(c) in approved and int(d) in approved:
        sys.exit("True")
    else:
        sys.exit("False")
