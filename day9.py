from itertools import permutations

def calculate_total_distance(perm, paths):
    distance = 0
    for i in range(1, len(perm)):
        distance += paths[(perm[i-1], perm[i])]

    return distance

def part1(input):

    locations = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight']
    all_permutations = permutations(locations)
    paths = {}
    for path in input:
        cities = path.split(" = ")[0].split(" to ")
        cost = int(path.split(" = ")[1])
        paths[(cities[0], cities[1])] = cost
        paths[(cities[1], cities[0])] = cost

    min_distance = float('inf')

    for perm in all_permutations:
        distance = calculate_total_distance(perm, paths)
        if distance < min_distance:
            min_distance = distance

    return min_distance
    
def part2(input):
    locations = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight']
    all_permutations = permutations(locations)
    paths = {}
    for path in input:
        cities = path.split(" = ")[0].split(" to ")
        cost = int(path.split(" = ")[1])
        paths[(cities[0], cities[1])] = cost
        paths[(cities[1], cities[0])] = cost

    max_distance = float('-inf')

    for perm in all_permutations:
        distance = calculate_total_distance(perm, paths)
        if distance > max_distance:
            max_distance = distance

    return max_distance


f = open("input/day9", "r")
input = f.read()

print(part1(input.split("\n")))
print(part2(input.split("\n")))
