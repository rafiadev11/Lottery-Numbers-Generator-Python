"""
Rachid Rafia
MET CS 521
10-8-19
Final Project
Description: Generate Lottery numbers using the delta system or the most frequent winning numbers
"""

from classes.delta_system import DeltaSystem
from classes.frequent_winning_numbers import FrequentWinningNumbers

# declare empty variables
lottery_game = ''
lottery_method = ''


def get_user_delta_numbers(game):
    """
    Call DeltaSystem class and generate delta numbers
    :param str game:
    :return: Delta numbers to be played
    """

    # declare empty list
    delta_nums = []

    # instantiate the DeltaSystem class
    delta = DeltaSystem(game)

    # assign a value to lottery_max_number attribute based on the game selected
    delta.lottery_max_number = 69 if game == 'p' else 75

    # prompt the user to select if he/she wants to review the delta system number selection guideline
    guide = input("Would you like to review how to select the delta system numbers?"
                  " Y = Yes, Press enter to skip : ").strip()

    if guide.lower() == 'y':
        # Display the guideline
        delta.display_guide()
    while True:
        # prompt the user to enter delta system numbers
        user_inputs = input(
            "Enter the delta system numbers separated by comma: ").strip().split(",")

        try:
            # convert the numbers to integers
            delta_nums = [int(num) for num in user_inputs]

            # validate the numbers
            validate_delta_numbers(delta_nums, delta)
            break
        except Exception as exception:
            print(exception)
            continue

    # assign the numbers to the DeltaSystem instance attribute using set_numbers method
    delta.set_numbers(delta_nums)

    # return the results
    return "Use the following lottery numbers in any order: {0}".format(delta.generate_numbers())


def validate_delta_numbers(delta_nums, delta):
    """
    Delta system numbers validation
    :param list delta_nums:
    :param instance delta:
    """

    # check if each number in the list is within valid range
    if any(number not in range(1, delta.lottery_max_number + 1) for number in delta_nums):
        raise Exception("Please select numbers between 1 and {}".format(delta.lottery_max_number))

    # validate list length
    if len(delta_nums) != 6:
        raise Exception("You entered {0}. Please, enter 6 numbers.".format(len(delta_nums)))

    # add all users numbers and check if the total is greater than the valid lottery max number
    if not delta.check_total():
        raise Exception("The sum of your numbers {0} is greater than {1}. Try again."
                        .format(sum(delta.get_numbers()), delta.lottery_max_number))


def frequent_winning_numbers(frequent_nums):
    """
    generate the numbers to be played from the FrequentWinningNumbers class
    :param instance frequent_nums:
    :return: numbers to be played
    """

    # display guidelines
    frequent_nums.display_guide()

    while True:
        # prompt the user to select the accuracy level
        user_input = input(
            "Enter the accuracy level 1 = Level1, 2 = Level2, 3 = Level3, 4 = Level4, 5 = Level5: ").strip()
        try:
            # convert user input to integer
            level = int(user_input)

            # check if user input is out of range
            if level not in range(1, 6):
                raise Exception("Please, pick a number from 1 to 5.")

            # assign level to the level attribute in FrequentWinningNumbers class
            frequent_nums.level = level
            break
        except Exception as exception:
            print(exception)
            continue

    # return the results
    return frequent_nums.generate_numbers()


def update_winning_numbers_file(frequent_nums):
    """
    Update the files that contains the winning numbers
    :param instance frequent_nums:
    :return: a success message when the files are updated
    """
    while True:
        # declare empty list
        numbers = []
        # prompt the user to enter the new winning numbers
        user_input = input(
            "Enter the new winning numbers separated by comma.: ").strip().split(",")
        try:
            # convert the user numbers to integers
            numbers = [int(num) for num in user_input]

            # check if user input is out of range
            for number in numbers:
                if number not in range(1, frequent_nums.lottery_max_number+1):
                    raise Exception("Your number {0} is out of range. Your number must be between 1 and {1}"
                                    .format(number, frequent_nums.lottery_max_number))
            break
        except Exception as exception:
            print(exception)
            continue

    # return the results
    return frequent_nums.update_file(numbers)


def frequent_winning_numbers_menu(game):
    """
    Display the frequent winning numbers method menu
    :param str game:
    :return: the menu
    """

    # declare a variable
    selection = 0
    while True:
        try:
            print("Menu:")
            print("----------------------------------------")
            print("1: Generate the numbers")
            print("2: Add new winning numbers to the file")
            print("----------------------------------------")

            # prompt the user to select from the menu
            user_selection = input("pick 1 or 2 from the menu: ").strip()

            # convert user input to integer
            selection = int(user_selection)

            # check if user input is out of range
            if selection not in range(1, 3):
                raise Exception("Please, enter 1 or 2. Try again")
            break
        except Exception as e:
            print(e)
            continue

    # instantiate the FrequentWinningNumbers class
    frequent_nums = FrequentWinningNumbers(game)

    # assign a value to lottery_max_number attribute based on the game selected
    frequent_nums.lottery_max_number = 69 if game == 'p' else 75

    # call the frequent_winning_numbers function to generate numbers if user selects 1; otherwise,
    # call the update_winning_numbers function to update the files
    if selection == 1:
        return "Use the following lottery numbers in any order: {0}".format(frequent_winning_numbers(frequent_nums))
    if selection == 2:
        return update_winning_numbers_file(frequent_nums)


def display_numbers(method, game):
    """
    based on user selected mehtod, call the appropriate function
    :param str method:
    :param str game:
    :return: lottery method to be used. (delta system or frequent winning numbers method)
    """
    if method == 'd':
        return get_user_delta_numbers(game)
    else:
        return frequent_winning_numbers_menu(game)


if __name__ == '__main__':
    while True:
        try:
            # prompt the user to select a lottery method
            lottery_method = input("Select the number's generator method? "
                                   "D: Delta System - F: Frequent Winning Numbers: ").strip()

            # make sure the user entered D or F
            if lottery_method.lower() == "d" or lottery_method.lower() == "f":
                break
            raise Exception("Please, enter D for the Delta System or F for the Frequent Winning Numbers")
        except Exception as e:
            print(e)

    while True:
        try:
            # prompt the user to select a lottery game
            lottery_game = input("Select a lottery game? P: PowerBall - M: Mega Millions: ").strip()

            # make sure the user entered P or M
            if lottery_game.lower() == "p" or lottery_game.lower() == "m":
                break
            raise Exception("Please, enter P for Powerball or M for Mega Millions")
        except Exception as e:
            print(e)

    # Display the results
    print(display_numbers(lottery_method.lower(), lottery_game.lower()))
