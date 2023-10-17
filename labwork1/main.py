# This is a sample Python script.
from time import sleep

from cookingdbaccess import CookingRecipesFileModel
from cookinglogic import CookingRecipesLogic, CookingRecipesLogicError

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Приветствуем Вас пользователь в системе кулинарных рецептов.\nДля начала необходимо авторизоваться\n')
    logic = CookingRecipesLogic(CookingRecipesFileModel('database.json'))
    print(f'Ну привет, {logic.username}')

    while True:
        print('\nВыберите нужный рецепт из предоставленного списка:\n\t[ № ]\t[ Название: ]')
        currentItem = 0
        for item in logic.getCatalogList():
            print(f'\t-- ({currentItem + 1}) [ {item} ]')
            currentItem += 1

        recipeName: str = input('Введите название: ')
        try:
            print(f'\nВот твой рецентик, {logic.username}:\n\b[ Список ингредиентов ]:')
            for item in logic.getRecipeIngredient(name=recipeName):
                print(f'\t-- ( {item} )')
            print(f'\n[ Описание рецепта ]: {logic.getRecipeDescription(name=recipeName)}')

        except CookingRecipesLogicError as error:
            print(f'\nУПС... Произошла ошибка.\n{error}')
        input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
