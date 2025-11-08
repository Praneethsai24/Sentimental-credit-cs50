import sys
import get_int

number = get_int("Number: ")
s = str(number)

beginning2 = int(s[:2]) if len(s) >= 2 else -1
beginning1 = int(s[:1]) if len(s) >= 1 else -1

# Checking if the credit card is valid
if not (beginning2 in (34, 37) or beginning1 == 4 or 51 <= beginning2 <= 55):
    print("INVALID")
    sys.exit()

product = 0
everyotherdig = []
others = []

index = len(s) - 2
for j in range(index, -1, -1):
    if (index - j) % 2 == 0:
        dig = int(s[j])
        doubled = dig * 2
        if doubled > 9:
            doubled -= 9
        everyotherdig.append(doubled)
    else:
        others.append(int(s[j]))

others.append(int(s[-1]))

sumdigits = sum(everyotherdig)
othersum = sum(others)
finalsum = sumdigits + othersum

valid = (finalsum % 10 == 0)

nlen = len(s)
if valid and nlen >= 13:
    if nlen == 15 and beginning2 in (34, 37):
        print("AMEX")
        sys.exit()
    elif nlen == 16 and 51 <= beginning2 <= 55:
        print("MASTERCARD")
        sys.exit()
    elif beginning1 == 4 and nlen in (13, 16):
        print("VISA")
        sys.exit()
    else:
        print("INVALID")
        sys.exit()

print("INVALID")

