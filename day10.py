
def part1(input):
    number = input

    for i in range(40):
        new_number = ""
        j = 0
        while j < len(number):
            counter = 1
            k = j + 1 
            while k < len(number) and number[k] == number[j]:
                counter += 1
                k += 1
            new_number += str(counter) + number[j]
            j += counter

        number = new_number

    return len(number)
        
def part2(input):
    number = input

    for i in range(50):
        new_number = ""
        j = 0
        while j < len(number):
            counter = 1
            k = j + 1 
            while k < len(number) and number[k] == number[j]:
                counter += 1
                k += 1
            new_number += str(counter) + number[j]
            j += counter

        number = new_number

    return len(number)

print(part1("3113322113"))
print(part2("3113322113"))
