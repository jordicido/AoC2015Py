def search_instruction(input, signal):
    for element in input:
        if element[1] == signal:
            return element
        
    return

def solve_operation(argument_a, operation, argument_b=0):
    match operation:
        case "AND":
            return int(argument_a) & int(argument_b)
        case "OR":
            return int(argument_a) | int(argument_b)
        case "RSHIFT":
            return int(argument_a) >> int(argument_b)
        case "LSHIFT":
            return int(argument_a) << int(argument_b)
        case "NOT":
            return ~ int(argument_a)
        case default:
            return

def update_stack_with_value(way_to_a_signal, signal, value):
    # iterate through stack with indexes, update values
    return
        
def part1(input):
    input = input.split(" -> ")
    way_to_a_signal = [input[8]]
    while way_to_a_signal:
        signal = way_to_a_signal.top()[0]
        if signal.isnumeric():
            # TODO call for function to replace variables for values in stack
            x = 1
        else:
            if len(signal) == 3:
                if not signal[0].isnumeric():
                    next_signal = search_instruction(input, signal[0])
                    next_signal[0] = next_signal[0].split(" ")
                    way_to_a_signal.push(next_signal)
                elif not signal[2].isnumeric():
                    next_signal = search_instruction(input, signal[2])
                    next_signal[0] = next_signal[0].split(" ")
                    way_to_a_signal.push(next_signal)
                else:
                    solve_operation(signal[0], signal[1], signal[2])
                    # TODO call for function to replace variables for values in stack
                    if signal[1] == "a":
                        return signal[0]
                    way_to_a_signal.pop()
            elif len(signal) == 2:
                if not signal[1].isnumeric():
                    next_signal = search_instruction(input, signal[1])
                    next_signal[0] = next_signal[0].split(" ")
                    way_to_a_signal.push(next_signal)
                else:
                    solve_operation(signal[1], signal[0])
                    # TODO call for function to replace variables for values in stack
                    if signal[1] == "a":
                        return signal[0]
                    way_to_a_signal.pop()



    return


def part2(input):
    return


f = open("inputTest/day7", "r")
input = f.read()

print(part1(input.split("\n")))
print(part2(input.split("\n")))
