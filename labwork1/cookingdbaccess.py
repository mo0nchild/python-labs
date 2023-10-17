from abc import ABC, abstractmethod
from enum import Enum
from json import JSONDecoder
from typing import List, Dict, Any
from cookingmodel import CookingRecipeInfo


class CookingRecipesJSONDecoder(JSONDecoder):
    def __init__(self):
        JSONDecoder.__init__(self, object_hook=self.convertToRecipe)

    @staticmethod
    def convertToRecipe(json: Dict[str, Any]) -> CookingRecipeInfo:
        return CookingRecipeInfo(json['name'], json['ingredients'], json['description'])


class ModelType(Enum):
    FileDatabase: int = 0
    TableDatabase: int = 1
    StaticDatabase: int = 2


class CookingRecipesModel(ABC):
    def __init__(self, type: ModelType): self.__modelType = type

    @abstractmethod
    def getCatalogList(self) -> List[CookingRecipeInfo]: pass

    @property
    def modelType(self) -> ModelType: return self.__modelType


class CookingRecipesFileModel(CookingRecipesModel):
    def __init__(self, filename: str):
        CookingRecipesModel.__init__(self, type=ModelType.FileDatabase)
        self._filename = filename

    @property
    def filename(self) -> str: return self._filename

    def getCatalogList(self) -> List[CookingRecipeInfo]:
        with open(self._filename, encoding='utf-8', mode='r') as filestream:
            return CookingRecipesJSONDecoder().decode(filestream.read())
