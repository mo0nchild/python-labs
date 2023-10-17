from typing import List, Dict


class WordsData:
    def __init__(self):
        self.__wordList = ["море", "солнце", "яблоко"]
        self.__characters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л',
                             'м', 'н', 'о', 'п', 'р', 'с', 'т',
                             'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        self.__dictWord = {
            'море': 'Подсказка: Большая водная область',
            'солнце': 'Подсказка: Звезда, ярко светящая в нашей солнечной системе.',
            'яблоко': 'Плод дерева, обладающий красивой окраской и сладким вкусом.'
        }

    @property
    def wordList(self) -> List[str]: return self.__wordList

    @property
    def dictWord(self) -> Dict[str, str]: return self.__dictWord

    @property
    def characters(self) -> List[str]: return self.__characters

    def output_stickman(self, frame):
        if 10 > frame >= 6:
            print("     __\n")
            print("           |\n")
            print("           |\n")
            print("           |\n")
            print("           |\n")
            print("           |\n")
            print("__\n")
        elif frame == 5:
            print("     __\n")
            print("     |     |\n")
            print("           |\n")
            print("           |\n")
            print("           |\n")
            print("           |\n")
            print("__\n")
        elif frame == 4:
            print("     __\n")
            print("     |     |\n")
            print("     O     |\n")
            print("           |\n")
            print("           |\n")
            print("           |\n")
            print("__\n")
        elif frame == 3:
            print("     __\n")
            print("     |     |\n")
            print("     O     |\n")
            print("    /|\    |\n")
            print("           |\n")
            print("           |\n")
            print("__\n")
        elif frame == 2:
            print("     __\n")
            print("     |     |\n")
            print("     O     |\n")
            print("    /|\    |\n")
            print("     |     |\n")
            print("           |\n")
            print("__\n")
        elif frame == 1:
            print("     __\n")
            print("     |     |\n")
            print("     O     |\n")
            print("    /|\    |\n")
            print("     |     |\n")
            print("    /      |\n")
            print("__\n")
        elif frame == 0:
            print("     ___\n")
            print("     |     |\n")
            print("     O     |\n")
            print("    /|\    |\n")
            print("     |     |\n")
            print("    / \    |\n")
            print("__\n")