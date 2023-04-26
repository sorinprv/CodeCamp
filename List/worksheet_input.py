def average_first():
    numlist = []
    while True:
        inp = input("Enter a number: ")
        if inp == 'done':
            break
        value = float(inp)
        numlist.append(value)
    average = sum(numlist) / len(numlist)
    return "average:", average


def average_seconds():
    total = 0
    count = 0
    while True:
        inp = input("Enter a number: ")
        if inp == 'done':
            break
        value = float(inp)
        total = total + value
        count = count + 1
    average = total / count
    return "average:", average


print(average_first())

print(average_seconds())
