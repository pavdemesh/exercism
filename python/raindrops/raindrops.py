"""If a given number:
- has 3 as a factor, add 'Pling' to the result.
- has 5 as a factor, add 'Plang' to the result.
- has 7 as a factor, add 'Plong' to the result.
- does not have any of 3, 5, or 7 as a factor,
the result should be the digits of the number.
"""


def convert(number):
    conversion_table = {3: "Pling", 5: "Plang", 7: "Plong"}
    res = "".join(conversion_table[key] for key in sorted(conversion_table.keys()) if number % key == 0)
    return res if res else str(number)


print(convert(21))
print(convert(15))
print(convert(105))
print(convert(104))
