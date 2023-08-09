import re


def part1(input):
    found = False
    password = list(input)

    while not found:
        i = -1
        new_char = (ord(password[i])+1) % 123
        if new_char < 96:
            new_char += 96
        password[i] = chr(new_char)
        i -= 1
        while ord(password[i]) + 1 == 123:
            new_char = (ord(password[i])+1) % 123
            if new_char < 96:
                new_char += 96
            password[i] = chr(new_char)
            i -= 1
        if password[i+1] == "a":
            password[i] = chr((ord(password[i])+1))

        possible = "".join(password)
        if re.search(r'([a-z])\1{1}[a-z]*([a-z])\2{1}', possible) and not re.search(r'o|i|l', possible) and re.search(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', possible):
            found = True

    return "".join(password)


def part2(input):
    return


print(part1("cqjxjnds"))
print(part2("cqjxjnds"))
