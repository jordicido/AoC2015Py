import re

def part1(input):
    counter = 0

    for word in input:
        if (re.search(r'([aeiou].*){3,}', word) and re.search(r'(.)\1', word) and not re.search(r'ab|cd|pq|xy', word)):
            counter += 1

    return counter
    #"[aeiou]{3,} + ((\w)\2) + ^(?!.*(ab|bc|pq|xy)).*$" 


def part2(input):
    counter = 0

    for word in input:
        if (re.search(r'^.*?([a-z]{2}).*?(\1).*$', word) and re.search(r'([a-zA-Z])\w\1', word)):
            print(word)
            counter += 1

    return counter


f = open("input/day5", "r")
input = f.read()

print(part1(input.split("\n")))
print(part2(input.split("\n")))
