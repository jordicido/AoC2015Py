
def part1(input):
    grid = [[0 for x in range(1000)] for y in range(1000)]
    
    for command in input:
        command_splitted = command.split(' ')
        initial_point = []
        final_point = []
        if command_splitted[0] == "toggle":
            initial_point = [int(x) for x in command_splitted[1].split(',')]
            final_point = [int(x) for x in command_splitted[3].split(',')]
            for x in range(initial_point[0], final_point[0]+1): 
                for y in range(initial_point[1], final_point[1]+1):
                    grid[x][y] = (grid[x][y] + 1) % 2
        elif command_splitted[1] == "on":    
            initial_point = [int(x) for x in command_splitted[2].split(',')]
            final_point = [int(x) for x in command_splitted[4].split(',')]
            for x in range(initial_point[0], final_point[0]+1): 
                for y in range(initial_point[1], final_point[1]+1):
                    grid[x][y] = 1
        else:
            initial_point = [int(x) for x in command_splitted[2].split(',')]
            final_point = [int(x) for x in command_splitted[4].split(',')]
            for x in range(initial_point[0], final_point[0]+1): 
                for y in range(initial_point[1], final_point[1]+1):
                    grid[x][y] = 0
        
    return sum(line.count(1) for line in grid)


def part2(input):
    grid = [[0 for x in range(1000)] for y in range(1000)]
    
    for command in input:
        command_splitted = command.split(' ')
        initial_point = []
        final_point = []
        if command_splitted[0] == "toggle":
            initial_point = [int(x) for x in command_splitted[1].split(',')]
            final_point = [int(x) for x in command_splitted[3].split(',')]
            for x in range(initial_point[0], final_point[0]+1): 
                for y in range(initial_point[1], final_point[1]+1):
                    grid[x][y] += 2
        elif command_splitted[1] == "on":    
            initial_point = [int(x) for x in command_splitted[2].split(',')]
            final_point = [int(x) for x in command_splitted[4].split(',')]
            for x in range(initial_point[0], final_point[0]+1): 
                for y in range(initial_point[1], final_point[1]+1):
                    grid[x][y] += 1
        else:
            initial_point = [int(x) for x in command_splitted[2].split(',')]
            final_point = [int(x) for x in command_splitted[4].split(',')]
            for x in range(initial_point[0], final_point[0]+1): 
                for y in range(initial_point[1], final_point[1]+1):
                    grid[x][y] -= 1
                    if grid[x][y] < 0:
                        grid[x][y] = 0
        
    return sum([sum(i) for i in zip(*grid)])


f = open("input/day6", "r")
input = f.read()

print(part1(input.split("\n")))
print(part2(input.split("\n")))
