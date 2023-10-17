from abc import ABC, abstractmethod
from typing import List
from cookingdbaccess import CookingRecipesModel
from cookingmodel import CookingRecipeInfo


class CookingRecipesLogicBase(ABC):
    def __init__(self, username: str): self.__username = username

    @property
    def username(self) -> str: return self.__username

    @username.setter
    def setUsername(self, value: str) -> None: self.__username = value

    @abstractmethod
    def getRecipeIngredient(self, name: str) -> List[str]: pass

    @abstractmethod
    def getRecipeDescription(self, name: str) -> str: pass

    @abstractmethod
    def getCatalogList(self) -> List[str]: pass


class CookingRecipesLogicError(Exception):
    def __init__(self, error: str): self.__errorName = error

    @property
    def name(self) -> str: return self.__errorName


class CookingRecipesLogic(CookingRecipesLogicBase):
    def __init__(self, catalog: CookingRecipesModel):
        CookingRecipesLogicBase.__init__(self, input('Введите ваше имя: '))
        self.__catalog = catalog


    def getCatalogList(self) -> List[str]:
        catalogList: List[str] = []
        for item in self.__catalog.getCatalogList(): catalogList.append(item.recipeName)

        return catalogList

    def getRecipeIngredient(self, name: str) -> List[str]:
        recipe: List[CookingRecipeInfo] = self.__catalog.getCatalogList()
        info: CookingRecipeInfo \
            = next((x for x in recipe if x.recipeName == name), 'none')

        if info == 'none': raise CookingRecipesLogicError('Запись не найдена')
        return info.ingredients

    def getRecipeDescription(self, name: str) -> str:
        for item in self.__catalog.getCatalogList():
            if item.recipeName == name: return item.description

        raise CookingRecipesLogicError('Запись не найдена')
