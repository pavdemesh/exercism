def convert(number):
    # Create an empty string to store the resulting string
    res = ""
    # Subsequently check modulos (meaning that number has 3 / 5 / 7 as a factor)
    # If True --> add corresponding message to the resulting string via concatenation
    if number % 3 == 0:
        res += "Pling"
    if number % 5 == 0:
        res += "Plang"
    if number % 7 == 0:
        res += "Plong"
    # Return number (as string) if length of res is empty, meaning:
    # Number has not 3 / 5 / 7 as factor
    # Else return the string with Pling / Plang / Plong
    return str(number) if len(res) == 0 else res