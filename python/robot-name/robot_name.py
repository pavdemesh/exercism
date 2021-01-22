import string
import random


class Robot:
    list_of_names = list()

    def __init__(self):
        self.name = self.__fn_generate_name()
        while self.name in Robot.list_of_names:
            self.name = self.__fn_generate_name()
        Robot.list_of_names.append(self.name)

    @staticmethod
    def __fn_generate_name():
        first_letter = random.choice(string.ascii_uppercase)
        second_letter = random.choice(string.ascii_uppercase)
        first_digit = str(random.randint(0, 9))
        second_digit = str(random.randint(0, 9))
        third_digit = str(random.randint(0, 9))
        res = first_letter + second_letter + first_digit + second_digit + third_digit
        return res

    def reset(self):
        self.name = self.__fn_generate_name()
        while self.name in Robot.list_of_names:
            self.name = self.__fn_generate_name()
        Robot.list_of_names.append(self.name)
