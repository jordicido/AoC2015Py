# The function has a loop that iterates over all the input and make the calculations as required in the assignment
def part1(input):
    paper_sqrmt = 0

    for box in input:
        measures = [int(i) for i in box.split("x")]
        area_of_sides = [measures[0]*measures[1], measures[1]*measures[2], measures[0]*measures[2]]
        paper_sqrmt += 2*area_of_sides[0] + 2*area_of_sides[1] + 2*area_of_sides[2] + min(area_of_sides)

    return paper_sqrmt

# Same as the first part but it adds some extra calculation that require to take the 2 smaller measures of each box
def part2(input):
    ribbon_sqrmt = 0

    for box in input:
        measures = [int(i) for i in box.split("x")]
        ribbon_sqrmt += (measures[0]*measures[1]*measures[2])
        measures.sort()
        ribbon_sqrmt += measures[0] + measures[0] + measures[1] + measures[1]

    return ribbon_sqrmt


f = open("input/day2", "r")
input = f.read()

print(part1(input.split("\n")))
print(part2(input.split("\n")))
