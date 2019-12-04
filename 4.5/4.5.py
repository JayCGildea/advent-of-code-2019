start = 136760
end = 595630

def check_number(number, original, last=None, foundDuplicate=False):
    if not number:
        return foundDuplicate

    next = number[-1]

    if last is not None and int(last) < int(next):
        return False

    if original.count(next) == 2:
        foundDuplicate = True

    return check_number(number[:-1], original, next, foundDuplicate)

count = 0
for i in range(start, end):
    if check_number(str(i), str(i)):
        count += 1

print("Count: " + str(count))