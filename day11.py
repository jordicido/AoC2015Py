import re


def part1(input):
    found = False
    password = list(input)

    while not found:
        i = -1
        while ord(password[i]) == 122:
            password[i] = 'a'
            i -= 1
        password[i] = chr(ord(password[i])+1)

        possible = "".join(password)
        if not re.search(r'o|i|l', possible) and re.search(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', possible) and re.search(r'(.)\1.*(.)\2', possible):
            found = True

    return "".join(password)


def part2(input):
    found = False
    password = list(input)

    while not found:
        i = -1
        while ord(password[i]) == 122:
            password[i] = 'a'
            i -= 1
        password[i] = chr(ord(password[i])+1)

        possible = "".join(password)
        if not re.search(r'o|i|l', possible) and re.search(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', possible) and re.search(r'(.)\1.*(.)\2', possible):
            found = True

    return "".join(password)


print(part1("cqjxjnds"))
print(part2("cqjxxyzz"))
