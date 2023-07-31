       
def part1(input):
    for i in range(len(input)):
        input[i] = input[i].split(" = ")
    
    locations = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight']
    locations.sort()
    possible_ways = []
    cost = []
    i = 7

    while i > 0:
        for j in range(0, i):
            stop = input.pop(0)
            stop_cost = int(stop[1])
            stop = stop[0].split(" to ")
            if i == 7:
                possible_ways.append(stop)
                cost.append(stop_cost)
            else:
                for x in range(0, len(possible_ways)):
                    if possible_ways[x][-1] == stop[0]:
                        possible_ways.append(possible_ways[x].copy())
                        cost.append(cost[x])
                        new_last_index = len(possible_ways) - 1
                        possible_ways[new_last_index].append(stop[1])
                        cost[new_last_index] += stop_cost
                    elif possible_ways[x][-1] == stop[1]:
                        possible_ways.append(possible_ways[x].copy())
                        cost.append(cost[x])
                        new_last_index = len(possible_ways) - 1
                        possible_ways[new_last_index].append(stop[0])
                        cost[new_last_index] += stop_cost
        i -= 1

        
    viable_costs = []
    for i in range(len(possible_ways)):
        possible_ways[i].sort()
        if len(possible_ways[i]) == 8 and possible_ways[i] == locations:
            viable_costs.append(cost[i])
            print(possible_ways[i])

    viable_costs.sort()
    return viable_costs

def part2(input):
    return


f = open("input/day9", "r")
input = f.read()

print(part1(input.split("\n")))
print(part2(input.split("\n")))
