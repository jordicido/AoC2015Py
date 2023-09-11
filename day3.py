def update_position(position, signal):
    if signal == "^":
        position[0] += 1
    elif signal == "v":
        position[0] -= 1
    elif signal == ">":
        position[1] += 1
    else:
        position[1] -= 1

    return position

# In this first part we are asked, given a set of instructions, how many positions are visited in an
# infinite two dimensional array. In this case I use a two position integer array to control the actual
# position and a set of arrays to control the uniqueness of the positions visited
def part1(input):
    point = [0,0]
    houses = set()


    for signal in input:
        houses.add(tuple(point))
        point = update_position(point, signal)
        
    return len(houses)

# Same idea of the previous part but in this case we add a second position that is traversing the array
def part2(input):
    point_santa = [0,0]
    point_robot = [0,0]
    houses = set()
    turn = 0
    houses.add(tuple(point_santa))
    for signal in input:
        if turn % 2 == 0:
            point_santa = update_position(point_santa, signal)
            houses.add(tuple(point_santa))
        else:
            point_robot = update_position(point_robot, signal)
            houses.add(tuple(point_robot))
        
        turn += 1
        
    return len(houses)


f = open("input/day3", "r")
input = f.read()

print(part1(input))
print(part2(input))
