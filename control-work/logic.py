from typing import List

class RecipeModel(object):
    def __init__(self, name: str, category: str, description: str):
        self.__name = name
        self.__category = category
        self.__description = description
        self.__ingredients = []

    @property
    def name(self) -> str: return self.__name
    @property
    def category(self) -> str: return self.__category
    @property
    def description(self) -> str: return self.__description
    @property
    def ingredients(self) -> List[str]: return self.__ingredients

    def display_info(self):
        return f'{self.__name} {self.__category} {self.__description}'

recipes = [
    RecipeModel("Мисо_суп", "Первое_блюдо", "Вам_понравится"),
    RecipeModel("Стейк", "Десерт", "Чистый_протеин"),
    RecipeModel("Кофе", "Напиток", "Поможет_не_спать")
]
categories = ["Первые блюда", "Вторый блюда", "Десерты", "Выпечка", "Напитки"]

