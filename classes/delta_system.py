import random


class DeltaSystem:
    """
    This class manages the delta system calculation and returns the numbers that should be played
    """
    # class attributes
    __result = []
    lottery_max_number = 69

    def __init__(self, game, numbers=[]):
        """
        Initialize class attributes
        :param str game:
        :param list numbers:
        """
        self.__game = game
        self.__numbers = numbers
        self.lottery_max_number = 69 if game == 'p' else 75

    def get_game(self):
        """
        :return: self.__game
        """
        return self.__game

    def set_game(self, game):
        """
        assign param (game) to instance attribute (self.__game)
        :param str game:
        """
        self.__game = game

    def get_numbers(self):
        """
        :return: self.__numbers
        """
        return self.__numbers

    def set_numbers(self, numbers):
        """
        randomize the param (numbers) order and assign to instance attribute (self.__numbers)
        :param list numbers:
        """
        self.__numbers = random.sample(numbers, len(numbers))

    def check_total(self):
        """
        Check if lottery numbers are greater than the lottery's max number
        :return: bool
        """
        if sum(self.__numbers) <= self.lottery_max_number:
            return True
        return False

    def generate_numbers(self):
        """
        Calculate the delta numbers, add them to the results list,  and randomize the numbers order
        :return: list numbers
        """
        i = 0
        for number in self.__numbers:
            if len(self.__result) == 0:
                i = number
                self.__result.append(i)
            else:
                i += number
                self.__result.append(i)

        return random.sample(self.__result, len(self.__result))

    def display_guide(self):
        """
        display the guidelines based on the game selected
        """
        if self.__game == 'p':
            print("---------------------------------------------")
            print("How to select the delta numbers for Powerball")
            print("---------------------------------------------")
            print("Step 1: Pick a number between 1 and 5. recommended 1")
            print("Step 2: Pick two numbers between 1 and 8.")
            print("Step 3: Pick a number close to 8. (7 or 9)")
            print("Step 4: Pick two numbers between 8 and 18")
        else:
            print("-------------------------------------------------")
            print("How to select the delta numbers for Mega Millions")
            print("-------------------------------------------------")
            print("Step 1: Pick a number between 1 and 5. recommended 1")
            print("Step 2: Pick two numbers between 1 and 8.")
            print("Step 3: Pick a number close to 8. (7 or 9)")
            print("Step 4: Pick two numbers between 8 and 22")
        print("-------------------------------------------------")

    def __repr__(self):
        """
        :return: class information
        """
        return "DeltaSystem: game = {0}, numbers = {1}".format(self.__game, self.__numbers)


# Testing DeltaSystem class methods
if __name__ == '__main__':
    # instantiate the class
    delta = DeltaSystem('p', [1, 2, 3, 4, 5, 6])

    # calls the __repr__ method and display the result
    print(delta)

    # test the get_game() method
    assert delta.get_game() == 'p' or delta.get_game() == 'f', \
        print("Incorrect game value. Accepted values: D or F".format(delta.get_game()))

    # test the set_game() method
    delta.set_game('f')
    assert delta.get_game() == 'p' or delta.get_game() == 'f', \
        print("Incorrect game value. Accepted values: D or F".format(delta.get_game()))

    # test the get_numbers() method
    assert type(delta.get_numbers()) == list and len(delta.get_numbers()) == 6, \
        print("Numbers property must be a type of list")

    # test the set_numbers() method
    delta.set_numbers([7, 8, 9, 10, 11, 12])
    assert type(delta.get_numbers()) == list and len(delta.get_numbers()) == 6, \
        print("Numbers property must be a type of list and length equals to 6")

    # display error message if user numbers are greater than the lottery's max number
    # delta.set_numbers([100, 200, 300, 400, 500, 600])
    for num in delta.get_numbers():
        assert num <= delta.lottery_max_number, \
            print("{0} is greater than {1}".format(num, delta.lottery_max_number))

    # test the check_total() method
    # delta.set_numbers([100, 200, 300, 400, 500, 600])
    assert delta.check_total(), \
        print("The sum of your numbers {0} is greater than {1}. Try again."
              .format(sum(delta.get_numbers()), delta.lottery_max_number))

    # test the generate_numbers() method
    # delta.set_numbers([1, 2])
    assert len(delta.generate_numbers()) == 6, \
        print("The generated numbers {0} length {1} is not equal to 6"
              .format(delta.generate_numbers(), len(delta.generate_numbers())))

    # display success message when all tests pass
    print("Success!!!")
