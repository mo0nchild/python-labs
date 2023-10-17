from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List, Tuple


class LogicBase(metaclass=ABCMeta):

    def __init__(self): object.__init__(self)

    class LogicResult(object):

        class ResultState(Enum):
            PlayerWin = 1; BotWin = 2; Draw = 3

        def __init__(self, state: ResultState, permanent: bool = False):
            object.__init__(self)
            self.__state = state
            self.__permanent = permanent

        @property
        def state(self) -> ResultState: return self.__state

        @property
        def permanent(self) -> bool: return self.__permanent

    @abstractmethod
    def calculate(self, field: List[List[int]]) -> LogicResult: pass


class TikTakLogic(LogicBase):

    def __init__(self): LogicBase.__init__(self)

    class CheckLineResult(object):

        def __init__(self, cells: int, player: int):
            object.__init__(self)
            self.__cells = cells
            self.__player = player

        def __lt__(self, other) -> bool: return self.__cells > other.__cells

        @property
        def cells(self) -> int: return self.__cells

        @property
        def player(self) -> int: return self.__player

    @staticmethod
    def __checkline(line: List[int]) -> CheckLineResult:
        counter, maxCounter = 1, 1
        current, maxCurrent = line[0], line[0]

        for index, cell in enumerate(line):
            if index == 0: continue

            if cell != current: current = cell; counter = 1
            else: counter += 1
            if maxCounter < counter: maxCounter = counter; maxCurrent = current

        return TikTakLogic.CheckLineResult(maxCounter, maxCurrent)

    def calculate(self, field: List[List[int]]) -> LogicBase.LogicResult:
        lineResults: List[TikTakLogic.CheckLineResult] = []
        if len(field[0]) == len(field):
            passive: List[int] = [field[index][(len(field) - 1) - index] for index in range(len(field))]
            lineResults.append(TikTakLogic.__checkline(passive))
            lineResults.append(TikTakLogic.__checkline([field[index][index] for index in range(len(field))]))

        for line in field: lineResults.append(TikTakLogic.__checkline(line))
        for index in range(len(field[0])):
            lineResults.append(TikTakLogic.__checkline([row[index] for row in field]))

        lineResults = list(filter(lambda x: x.player != 0, lineResults))
        lineResults.sort()

        # print([(x.player, x.cells) for x in lineResults])

        if len(lineResults) <= 0:
            return LogicBase.LogicResult(state=LogicBase.LogicResult.ResultState.Draw)

        # if lineResults[0].cells <= 2 and 0 in [a for b in field for a in b]:
        #     return LogicBase.LogicResult(state=LogicBase.LogicResult.ResultState.Draw, permanent=True)

        playerScore = 0
        botScore = 0
        for winner in list(filter(lambda x: x.cells == lineResults[0].cells, lineResults)):
            if winner.player == 1: playerScore += 1
            elif winner.player == -1: botScore += 1

        print(f'player: {playerScore}; bot: {botScore}')

        permanent: bool = max([len(field[0]), len(field)]) <= lineResults[0].cells
        state: LogicBase.LogicResult.ResultState = (
            LogicBase.LogicResult.ResultState.Draw if playerScore == botScore else (
                LogicBase.LogicResult.ResultState.PlayerWin if playerScore > botScore
                else LogicBase.LogicResult.ResultState.BotWin
            )
        )
        # state: LogicBase.LogicResult.ResultState = (
        #     LogicBase.LogicResult.ResultState.Draw) if lineResults[0].cells <= 2 else (
        #     LogicBase.LogicResult.ResultState.PlayerWin if lineResults[0].player == 1 else
        #     LogicBase.LogicResult.ResultState.BotWin)
        return LogicBase.LogicResult(state=state, permanent=permanent)

