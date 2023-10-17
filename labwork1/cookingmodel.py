from typing import List

class CookingRecipeInfo(object):
    def __init__(self, name: str, ingredients: List[str], description: str):
        object.__init__(self)
        self.__recipeName = name
        self.__ingredients = ingredients
        self.__description = description

    @property
    def description(self) -> str: return self.__description

    @property
    def ingredients(self) -> List[str]: return self.__ingredients

    @property
    def recipeName(self) -> str: return self.__recipeName


