import json
import time

primitive = (int, str, bool)

def common_iterable(obj):
    if isinstance(obj, dict):
        return obj
    else:
        return (index for index, value in enumerate(obj))

def explore_object(object, result):
    if type(object) == int:
        return result+object
    elif type(object) == str:
        return result
    else:
        for item in common_iterable(object):
            if isinstance(object, dict) and ("red" in object.keys() or "red" in object.values()):
                break
            else: 
                result = explore_object(object[item], result)
    
    return result


def part1(input):
    result = 0
    is_number = False
    partial_number = 0

    for i in range(len(input)):
        if input[i].isnumeric() and not is_number:
            is_number = True
            partial_number += int(input[i])
            if input[i-1] == '-':
                partial_number = - partial_number
        elif input[i].isnumeric() and is_number:
            if partial_number > 0:
                partial_number = (partial_number * 10) + int(input[i])
            else:
                partial_number = (partial_number * 10) - int(input[i])
        elif is_number:
            is_number = False
            result += partial_number
            partial_number = 0

    return result


def part2(input):
    json_object = json.loads(input)

    return explore_object(json_object, 0)


f = open("input/day12", "r")
input = f.read()

print(part1(input))
print(part2(input))
