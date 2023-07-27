       
def part1(input):
    total = 0
    characters_in_mem = 0
    for element in input:
        total += len(element)
        chars_without_quotes = element[1:-1]
        i = 0

        while i < len(chars_without_quotes):
            if chars_without_quotes[i] == "\\":
                if chars_without_quotes[i+1] == "\\" or chars_without_quotes[i+1] == "\"":
                    i += 1
                elif chars_without_quotes[i+1] == "x":
                    i += 3
            characters_in_mem += 1
            i += 1

                
    return total - characters_in_mem


def part2(input):
    total = 0
    chars_after_encoding = 0

    for element in input:
        total += len(element)
        chars_without_quotes = element[1:-1]
        i = 0
        chars_after_encoding += 6
        
        while i < len(chars_without_quotes):
            if chars_without_quotes[i] == "\\":
                if chars_without_quotes[i+1] == "\\" or chars_without_quotes[i+1] == "\"":
                    chars_after_encoding += 4
                    i += 1
                elif chars_without_quotes[i+1] == "x":
                    chars_after_encoding += 5
                    i += 3
            else:
                    chars_after_encoding += 1    
            i += 1

                
    return chars_after_encoding - total


f = open("input/day8", "r")
input = f.read()

print(part1(input.split("\n")))
print(part2(input.split("\n")))
