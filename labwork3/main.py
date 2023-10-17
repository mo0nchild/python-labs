from logic import LogicBase, TikTakLogic
from scene import TikTakScene, SceneMaker


def gameInit(scene: SceneMaker) -> None:
    while True:
        if not scene.render(): break


if __name__ == '__main__':
    gameInit(scene=TikTakScene(size=(4, 4), logic=TikTakLogic()))
