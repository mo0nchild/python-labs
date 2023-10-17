import random
from abc import ABC, ABCMeta, abstractmethod
from tokenize import String
from typing import Tuple, List

from logic import LogicBase


class SceneMakerException(Exception):

    def __init__(self, msg: String, size: Tuple[int, int]):
        Exception.__init__(self, msg)
        self.__size = size

    @property
    def size(self) -> Tuple[int, int]: return self.__size


class SceneMaker(object, metaclass=ABCMeta):

    def __init__(self, size: Tuple[int, int]):
        object.__init__(self)
        if size[0] < 3 or size[1] < 3:
            raise SceneMakerException("Неверный раззмер поля", size)

        self.__width = size[0]
        self.__height = size[1]

        self.__field = []
        for height in range(0, self.__height):
            self.__field.append([0] * self.__width)

    @abstractmethod
    def render(self) -> bool: pass

    @property
    def field(self) -> List[List[int]]: return self.__field

    @property
    def width(self) -> int: return self.__width

    @property
    def height(self) -> int: return self.__height


class TikTakScene(SceneMaker):

    def __init__(self, size: Tuple[int, int], logic: LogicBase):
        SceneMaker.__init__(self, size)
        self.__logic = logic

    def render(self) -> bool:
        for rows in self.field:
            [print('|\t{:s}\t'.format('[ x ]' if i == 1 else ('[ 0 ]' if i == -1 else '[ _ ]')), end='') for i in rows]
            print(f'\n{"".join(["-" for i in range(12 * self.width)])}', end='\n')

        stage: LogicBase.LogicResult = self.__logic.calculate(self.field)
        if not (0 in [a for b in self.field for a in b]) or stage.permanent:
            print(f'Игра закончилась: {stage.state}')
            return False
        try:
            (x, y) = map(lambda x: int(x), input('Введите координаты (x y): ').split(' '))
            if self.field[y][x] == 0:
                self.field[y][x] = 1
                botStepList = []
                for y, row in enumerate(self.field):
                    botStepList.extend(list(filter(lambda x: x[2] == 0, [(x, y, col) for x, col in enumerate(row)])))

                botChoice = random.choice(botStepList)
                self.field[botChoice[1]][botChoice[0]] = -1

            else: print('Клетка занята, нужна другая')
        except IndexError as error: print('Неверные координаты')
        except ValueError as error: print('Фигня какая-то, нормально набери емае')
        return True
