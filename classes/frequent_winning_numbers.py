import collections
import random


class FrequentWinningNumbers:
    """
    This class handles the frequent winning numbers system.
    It manages selecting the most frequent numbers based on user's accuracy level
    It also allows the user to update the files containing the winning numbers
    """

    # declare class attributes
    lottery_max_number = 69
    __numbers_to_play = []

    def __init__(self, game, level=1, file_path=str()):
        """
        Initialize class attributes
        :param str game:
        :param int level:
        :param str file_path:
        """
        self.__game = game
        self.level = level
        self.file_path = file_path

        # if file path is empty, use the default file paths
        if self.file_path == '':
            # assign the correct file and lottery max number based on selected game
            if self.__game == 'p':
                self.file_path = 'files/powerball_winning_numbers.txt'
                self.lottery_max_number = 69
            else:
                self.file_path = 'files/mega_millions_winning_numbers.txt'
                self.lottery_max_number = 75

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

    def generate_numbers(self):
        """
        select most frequent winning numbers and randomize their order
        :return: list numbers
        """
        return random.sample(self.__get_winning_numbers(), len(self.__get_winning_numbers()))

    def __get_winning_numbers(self):
        """
        open file for reading only, read all the numbers and add them to the list
        call the __most_frequent_numbers method to select the numbers to be played
        :return: list numbers
        """
        # open file
        file = open(self.file_path, 'r')

        # read all file data and split it
        file_content = file.read().strip().split()

        # convert numbers to integer and save to the numbers list
        numbers = [int(num) for num in file_content]

        # close the file
        file.close()

        # call the __most_frequent_numbers to get numbers to be played
        for number in self.__most_frequent_numbers(numbers):
            self.__numbers_to_play.append(number[0])

        # return the numbers
        return random.sample(self.__numbers_to_play, 6)

    def __most_frequent_numbers(self, numbers):
        """
        use the counter method from the collection library to select most common winning numbers
        :param list numbers:
        :return: common numbers based on accuracy level
        """
        counter = collections.Counter(numbers)
        return counter.most_common(self.__accuracy_level() if self.__accuracy_level() != 0 else len(numbers))

    def __accuracy_level(self):
        """
        Select how many common numbers to select from based on user accuracy level
        :return: total numbers
        """
        if self.level == 1:
            return 6
        if self.level == 2:
            return 20
        if self.level == 3:
            return 50
        if self.level == 4:
            return 100
        if self.level == 5:
            return 0

    def update_file(self, numbers):
        """
        append user numbers to one of the files
        :param list numbers:
        :return: success message when file is updated
        """

        # open file with append mode
        file = open(self.file_path, 'a')
        counter = 0

        # iterate through the user numbers and append to the file
        for number in numbers:
            # if counter is 0, move the cursor to a new line
            if counter == 0:
                file.write("\n")
            # write the number to the file
            file.write(str(number))

            # write a space
            file.write(" ")

            # if counter is 5, move the cursor to a new line
            if counter == 5:
                file.write("\n")
                counter = 0
            counter += 1

        # close the file
        file.close()
        return "{0} file has been updated. Thank you.".format(self.file_path)

    @staticmethod
    def display_guide():
        """
        Display guidelines
        """
        print('---------------------------------------------------------------------------')
        print('                             Accuracy Level                                ')
        print('---------------------------------------------------------------------------')
        print('Level 1: Always return the top 6 most frequent winning numbers')
        print('Level 2: Randomly select 6 numbers out of 20 most frequent winning numbers')
        print('Level 3: Randomly select 6 numbers out of 50 most frequent winning numbers')
        print('Level 4: Randomly select 6 numbers out of 100 most frequent winning numbers')
        print('Level 5: Randomly select 6 numbers out of all winning numbers')
        print('---------------------------------------------------------------------------')

    def __repr__(self):
        """
        :return: class information
        """
        return "FrequentWinningNumbers: game = {0}, level = {1}".format(self.__game, self.level)


# Testing FrequentWinningNumbers class methods
if __name__ == '__main__':
    import os.path as path

    # instantiate the FrequentWinningNumbers
    frequent_winning_number = FrequentWinningNumbers('p', 1)

    # get the correct files' path
    frequent_winning_number.file_path = "../{}".format(frequent_winning_number.file_path)

    # make sure path exists
    # frequent_winning_number.file_path = "../../{}".format(frequent_winning_number.file_path)
    assert path.isfile(frequent_winning_number.file_path), \
        print("{0} file does not exist".format(frequent_winning_number.file_path))

    # test generate_numbers() method
    assert type(frequent_winning_number.generate_numbers()) == list and \
        len(frequent_winning_number.generate_numbers()) == 6, \
        print("Numbers property must be a type of list and length equals to 6")

    # display error message if user numbers are greater than the lottery's max number
    numbers = [1, 2, 3, 4, 5, 6]
    # numbers = [100, 200, 300, 400, 500, 600]
    for num in numbers:
        assert num <= frequent_winning_number.lottery_max_number, \
            print("{0} is greater than {1}".format(num, frequent_winning_number.lottery_max_number))

    # test the update_file() method
    assert "file has been updated" in frequent_winning_number.update_file(numbers), \
        print("There was an error writing to {} file".format(frequent_winning_number.file_path))

    # display success message when all tests pass
    print("Success!!!")
