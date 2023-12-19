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


recipe1 = RecipeModel("Кофе", "Напиток", "Поможет_не_спать")
recipe1.ingredients.append("Молоко")
recipe1.ingredients.append("Кофе")
recipe1.ingredients.append("Чашка")

recipe2 = RecipeModel("Мисо_суп", "Первое_блюдо", "Вам_понравится")
recipe2.ingredients.append("Вода")
recipe2.ingredients.append("Сыр")
recipe2.ingredients.append("Чашка")

recipe3 = RecipeModel("Стейк", "Десерт", "Чистый_протеин")
recipe3.ingredients.append("Мясо")
recipe3.ingredients.append("Специи")

recipes = [recipe1, recipe2, recipe3]
categories = ["Первые блюда", "Вторый блюда", "Десерты", "Выпечка", "Напитки"]

