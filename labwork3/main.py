from logic import LogicBase, TikTakLogic
from scene import TikTakScene, SceneMaker


def gameInit(scene: SceneMaker) -> None:
    while True:
        if not scene.render(): break


if __name__ == '__main__':
    gameInit(scene=TikTakScene(size=(4, 4), logic=TikTakLogic()))
    # tiktak = TikTakLogic()
    # fieldbotwin = [
    #     [1, 1, -1, -1],
    #     [1, -1, 1, -1],
    #     [-1, 1, 1, -1],
    #     [-1, -1, -1, 1]
    # ]
    # print(f'{tiktak.calculate(fieldbotwin).state}')
    # fieldplayerin = [
    #     [1, 1, -1, -1],
    #     [1, -1, 1, -1],
    #     [1, 1, 1, -1],
    #     [-1, -1, 1, 1]
    # ]
    # print(f'{tiktak.calculate(fieldplayerin).state}')
    # fielddraw = [
    #     [1, 1, -1, -1],
    #     [1, -1, 1, -1],
    #     [-1, 1, 1, -1],
    #     [-1, -1, 1, 1]
    # ]
    # print(f'{tiktak.calculate(fielddraw).state}')
    # fieldplayerpermanent = [
    #     [1, 1, -1, -1],
    #     [1, 1, 1, -1],
    #     [-1, 1, 1, -1],
    #     [-1, -1, 1, 1]
    # ]
    # print(f'{tiktak.calculate(fieldplayerpermanent).state}')
