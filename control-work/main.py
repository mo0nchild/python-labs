import tkinter as Tk
from tkinter import ttk
import tkinter.font as font
import logic

class CookingRecipeApp(object):

    def __init__(self, root: Tk):
        super().__init__()
        self.root = root
        self.root.geometry('540x420')
        self.root.title('Книга рецептов')
        self.root.resizable(False, False)

        columns = 'Название', 'Категория', 'Описание'
        self.tree = ttk.Treeview(root, columns=columns, show='headings')
        self.tree.heading('Название', text='Название')
        self.tree.heading('Категория', text='Категория')
        self.tree.heading('Описание', text='Описание')

        self.tree.column('Название', width=100, anchor=Tk.W)
        self.tree.column('Категория', width=100, anchor=Tk.W)
        self.tree.column('Описание', width=100, anchor=Tk.W)

        self.tree.pack(side=Tk.LEFT, fill=Tk.BOTH)
        for item in logic.recipes:
            self.tree.insert('', Tk.END, values=item.display_info())

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=Tk.BOTH)

        # Создание полей ввода справа
        entryFrame = Tk.Frame(notebook)
        entryFrame.pack(fill=Tk.BOTH, expand=True, pady=100)

        label1 = Tk.Label(entryFrame, text="Название рецепта:")
        label1.pack()
        self.nameEntry = Tk.Entry(entryFrame, font=('sans-serif 12'))
        self.nameEntry.pack()

        label2 = Tk.Label(entryFrame, text="Описание:")
        label2.pack(pady=(10, 0))
        self.descriptionEntry = Tk.Entry(entryFrame, font=('sans-serif 12'))
        self.descriptionEntry.pack()

        label = ttk.Label(entryFrame, text="Категория:")
        label.pack(pady=(10, 0))
        self.categoryCombobox = ttk.Combobox(entryFrame, textvariable=Tk.StringVar(value=logic.categories[0]),
                                             values=logic.categories, font=('sans-serif 12'))
        self.categoryCombobox.current(0)
        self.categoryCombobox.pack()

        # добавляем фреймы в качестве вкладок
        notebook.add(entryFrame, text="Конфигурация")

        ingredientsFrame = Tk.Frame(root)
        ingredientsFrame.pack(fill=Tk.BOTH, expand=True)

        notebook.add(ingredientsFrame, text="Ингредиенты")

        buttonFrame = Tk.Frame(root)
        buttonFrame.pack(side=Tk.BOTTOM, pady=20)

        self.infoButton = ttk.Button(buttonFrame, text="Посмотреть рецепт",
                                     command=self.addRecipeHandler)
        self.infoButton.pack(side=Tk.TOP, pady=5, fill=Tk.BOTH)

        self.addButton = ttk.Button(buttonFrame, text="Добавить рецепт",
                                    command=self.addRecipeHandler)
        self.addButton.pack(side=Tk.RIGHT, padx=5)

        self.deleteButton = ttk.Button(buttonFrame, text="Удалить запись",
                                       command=self.deleteRecipeHandler)
        self.deleteButton.pack(side=Tk.RIGHT, padx=5)

    def update_view(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in logic.recipes:
            self.tree.insert('', Tk.END, values=item.display_info())

    def addRecipeHandler(self):
        newRecipe = logic.RecipeModel(self.nameEntry.get().replace(" ", "_"),
                                      self.categoryCombobox.get().replace(" ", "_"),
                                      self.descriptionEntry.get().replace(" ", "_"))
        logic.recipes.append(newRecipe)
        self.update_view()

    def deleteRecipeHandler(self):
        logic.recipes.pop()
        self.update_view()


if __name__ == '__main__':
    root = Tk.Tk()
    cookbook = CookingRecipeApp(root)
    root.mainloop()
