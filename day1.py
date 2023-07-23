def part1(input):
    counter = 0

    for parenthesis in input:
        if parenthesis == "(":
            counter += 1
        else:
            counter -= 1

    return counter

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
