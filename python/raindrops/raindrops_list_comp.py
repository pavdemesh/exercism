"""If a given number:
- has 3 as a factor, add 'Pling' to the result.
- has 5 as a factor, add 'Plang' to the result.
- has 7 as a factor, add 'Plong' to the result.
- does not have any of 3, 5, or 7 as a factor,
the result should be the digits of the number.
"""


def convert(number):
    modulo_results = [True if number % i == 0 else False for i in range(3, 8, 2)]
    res = "".join(["Pling", "Plang", "Plong"][i] for i in range(3) if modulo_results[i])
    return res if res else str(number)


print(convert(21))
print(convert(15))
print(convert(105))
print(convert(104))
