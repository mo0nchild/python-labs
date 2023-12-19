import tkinter as Tk
from tkinter import ttk
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

        # Создание полей ввода справа
        entry_frame = Tk.Frame(root)
        entry_frame.pack(side=Tk.TOP)

        label1 = Tk.Label(entry_frame, text="Название рецепта:")
        label1.pack()
        self.nameEntry = Tk.Entry(entry_frame)
        self.nameEntry.pack()

        label2 = Tk.Label(entry_frame, text="Описание:")
        label2.pack(pady=(10, 0))
        self.descriptionEntry = Tk.Entry(entry_frame)
        self.descriptionEntry.pack()

        categories = ["Первые блюда", "Вторый блюда", "Десерты", "Выпечка", "Напитки"]
        categories_var = Tk.StringVar(value=categories[0])

        label = ttk.Label(entry_frame, text="Категория:")
        label.pack(pady=(10, 0))
        self.categoryCombobox = ttk.Combobox(entry_frame, textvariable=categories_var, values=categories)
        self.categoryCombobox.pack()

        buttonFrame = Tk.Frame(root)
        buttonFrame.pack(side=Tk.BOTTOM, pady=20)

        self.addButton = ttk.Button(buttonFrame, text="Добавить рецепт", command=self.addRecipeHandler)
        self.addButton.pack()

        self.deleteButton = ttk.Button(buttonFrame, text="Удалить запись", command=self.deleteRecipeHandler)
        self.deleteButton.pack(pady=5)

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
