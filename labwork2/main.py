# This is a sample Python script.
import os
import string
from random import shuffle
import re
from data import WordsData

class WordsGame:
    def __init__(self):
        self.__turns = 10
        self.__data = WordsData()
        print(f"Привет, Давай сыграем в виселицу! У тебя есть {self.__turns} попыток!")

        shuffle(self.__data.wordList)
        self.__word = self.__data.wordList.pop()

        self.__remaining_word = '%s' % self.__word
        count_chars = len(self.__word)
        self.__guesses = ''

        for i in range(0, count_chars): self.__guesses += '_'

    def __show_characters(self, chars):
        for item in chars:
            if self.__data.characters.count(item) == 1:
                index = self.__data.characters.index(item)
                self.__data.characters[index] = ' '

        for iteration in range(0, len(self.__data.characters)):
            print(self.__data.characters[iteration] + ' ', end='')

    def __check(self, char: string, list_guesses, temp_guesses):
        find = False

        if char in list_guesses:
            print('Уже есть буква')
            return temp_guesses

        if char in self.__remaining_word:
            matches = re.finditer(char, self.__remaining_word)
            indices = [match.start() for match in matches]

            for item in indices:
                temp_guesses = temp_guesses[:item] + char + temp_guesses[item + 1:]
            find = True

        if find:
            self.__remaining_word.replace(char, '')
        else:
            self.__turns -= 1

        print(temp_guesses)
        return temp_guesses

    def __find_word(self, characters_guesses):
        list_guesses = list(characters_guesses)
        for item in self.__word:
            if list_guesses.count(item) >= 1:
                print(f'{item} ', end='')
            else:
                print("_ ", end='')
        print("")

    def render(self):
        while self.__turns > 0:
            os.system('CLS')

            self.__data.output_stickman(self.__turns)
            self.__show_characters(self.__guesses)
            print('')
            self.__find_word(self.__guesses)

            if self.__turns < 6: print(self.__data.dictWord.get(self.__word))

            if self.__guesses == self.__word:
                print('Вы победили')
                break

            ch_word = input()
            self.__guesses = self.__check(ch_word, list(self.__guesses), self.__guesses)

        if self.__turns == 0:
            print('Вы проиграли')

# Press the green button in the gutter to run the script.
if __name__ == '__main__': WordsGame().render()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
