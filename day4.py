import hashlib

def part1(input):
    i = 0

    while True:
        result = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()

        if result.startswith('00000'):
            return i
        
        i += 1


def part2(input):
    i = 0

    while True:
        result = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()

        if result.startswith('000000'):
            return i
        
        i += 1


f = open("input/day4", "r")
input = f.read()

print(part1(input))
print(part2(input))
