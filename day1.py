# The function has a loop that iterates over all the input and add 1 
# to counter if it finds a "(" and remove 1 from counter if it finds a ")"
def part1(input):
    counter = 0

    for parenthesis in input:
        if parenthesis == "(":
            counter += 1
        else:
            counter -= 1

    return counter

# In this case we want to do the same but we add a little complexity,
# we have to control when the floor first gets to basement (value = -1)
# and return the position when it first arrived
def part2(input):
    position = 0
    floor = 0

    for parenthesis in input:
        position += 1
        if parenthesis == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return position

    return -1


f = open("input/day1", "r")
input = f.read()

print(part1(input))
print(part2(input))
