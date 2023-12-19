import tkinter as Tk
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import logic

class CookingRecipeApp(object):

    def __init__(self, root: Tk):
        super().__init__()
        self.root = root
        self.root.geometry('540x420')
        self.root.title('Книга рецептов')
        self.root.resizable(False, False)

        columns = 'Название', 'Категория', 'Описание'
        self.tree = ttk.Treeview(root, columns=columns, show='headings', selectmode="browse")
        self.tree.heading('Название', text='Название')
        self.tree.heading('Категория', text='Категория')
        self.tree.heading('Описание', text='Описание')

        self.tree.column('Название', width=100, anchor=Tk.W)
        self.tree.column('Категория', width=100, anchor=Tk.W)
        self.tree.column('Описание', width=100, anchor=Tk.W)
        self.tree.bind("<<TreeviewSelect>>", self.on_treeview_select)
        self.selectedIndex = None

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
        self.nameEntry.bind("<FocusIn>", lambda args: self.on_entry_click(self.nameEntry,
                                                                                 "Укажите название"))
        self.nameEntry.bind("<FocusOut>", lambda args: self.on_focus_out(self.nameEntry,
                                                                                "Укажите название"))
        self.nameEntry.pack()

        label2 = Tk.Label(entryFrame, text="Описание:")
        label2.pack(pady=(10, 0))
        self.descriptionEntry = Tk.Entry(entryFrame, font=('sans-serif 12'))
        self.descriptionEntry.bind("<FocusIn>", lambda args: self.on_entry_click(self.descriptionEntry,
                                                                    "Укажите описание"))
        self.descriptionEntry.bind("<FocusOut>", lambda args: self.on_focus_out(self.descriptionEntry,
                                                                    "Укажите описание"))
        self.descriptionEntry.pack()
        self.on_focus_out(self.nameEntry, "Укажите название")
        self.on_focus_out(self.descriptionEntry, "Укажите описание")

        label = ttk.Label(entryFrame, text="Категория:")
        label.pack(pady=(10, 0))
        self.categoryCombobox = ttk.Combobox(entryFrame, textvariable=Tk.StringVar(value=logic.categories[0]),
                                             values=logic.categories, font=('sans-serif 12'))
        self.categoryCombobox.current(0)
        self.categoryCombobox.pack()

        # добавляем фреймы в качестве вкладок
        notebook.add(entryFrame, text="Конфигурация")

        ingredientsFrame = Tk.Frame(notebook)
        ingredientsFrame.pack(fill=Tk.BOTH, expand=True)

        self.ingredients_listbox = Tk.Listbox(ingredientsFrame, selectmode=Tk.SINGLE, font=("sans-serif", 10))
        self.ingredients_listbox.pack(pady=10)

        # Создаем поля для ввода названия и количества ингредиента
        ttk.Label(ingredientsFrame, text="Название ингредента:").pack(pady=(10, 0))
        self.name_entry = Tk.Entry(ingredientsFrame, width=20, font=("sans-serif", 12))
        self.name_entry.pack(pady=5)

        # Создаем кнопки для добавления и удаления ингредиентов
        self.add_button = Tk.Button(ingredientsFrame, text="Добавить", command=self.add_ingredient)
        self.add_button.pack(side=Tk.LEFT, padx=5)
        self.remove_button = Tk.Button(ingredientsFrame, text="Убрать", command=self.remove_ingredient)
        self.remove_button.pack(side=Tk.LEFT, padx=5)

        notebook.add(ingredientsFrame, text="Ингредиенты")

        buttonFrame = Tk.Frame(root)
        buttonFrame.pack(side=Tk.BOTTOM, pady=20)

        self.addButton = Tk.Button(buttonFrame, text="Добавить рецепт", font=("sans-serif", 10),
                                    bg="white", command=self.addRecipeHandler)
        self.addButton.pack(side=Tk.RIGHT, padx=5)

        self.deleteButton = Tk.Button(buttonFrame, text="Удалить запись", font=("sans-serif", 10),
                                       bg="white", command=self.deleteRecipeHandler)
        self.deleteButton.pack(side=Tk.RIGHT, padx=5)

    def add_ingredient(self):
        if self.selectedIndex is None:
            messagebox.showerror("Ошибка", "Рецепт не выбран")
            return
        # Получаем значения из полей ввода
        name = self.name_entry.get()

        # Проверяем, что оба поля заполнены
        if not name:
            messagebox.showwarning("Ошибка", "Введите название ингредиента")
            return

        # Добавляем ингредиент в список и отображаем в Listbox
        self.ingredients_listbox.insert(Tk.END, name)
        logic.recipes[self.selectedIndex].ingredients.append(name)
        # Очищаем поля ввода
        self.name_entry.delete(0, Tk.END)

    def remove_ingredient(self):
        # Получаем индекс выбранного элемента
        selected_index = self.ingredients_listbox.curselection()

        # Проверяем, что элемент выбран
        if not selected_index:
            return

        # Удаляем ингредиент из списка и Listbox
        self.ingredients_listbox.delete(selected_index)
        print(selected_index)
        logic.recipes[self.selectedIndex].ingredients.pop(selected_index[0])

    def on_entry_click(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, Tk.END)
            entry.config(fg='black')  # Change text color to black

    def on_focus_out(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg='grey')  # Change text color to grey

    def on_treeview_select(self, event):
        selected_items = self.tree.selection()
        selected_indices = []

        for item in selected_items:
            selected_indices.append(self.tree.index(item))

        if len(selected_indices) > 0:
            self.selectedIndex = selected_indices[0]
            self.ingredients_listbox.delete(0, Tk.END)
            index = 0
            for ingredient in logic.recipes[self.selectedIndex].ingredients:
                self.ingredients_listbox.insert(index, ingredient)
                index+=1
        else: self.selectedIndex = None

        print(f"Selected Indices: {selected_indices}")

    def update_view(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in logic.recipes:
            self.tree.insert('', Tk.END, values=item.display_info())

    def addRecipeHandler(self):
        recipeName = self.nameEntry.get().replace(" ", "_")
        recipeDescription = self.descriptionEntry.get().replace(" ", "_")

        if(len(recipeName) <= 0 or len(recipeDescription) <= 0):
            messagebox.showerror("Ошибка", "Текстовое поле не заполнено")
            return

        for recipe in logic.recipes:
            if recipe.name == recipeName:
                messagebox.showerror("Ошибка", "Рецепт с таким название существует")
                return

        newRecipe = logic.RecipeModel(name=recipeName, description=recipeDescription,
                                      category=self.categoryCombobox.get().replace(" ", "_"), )
        logic.recipes.append(newRecipe)
        self.update_view()
        self.nameEntry.delete(0, Tk.END)
        self.descriptionEntry.delete(0, Tk.END)
        # self.on_focus_out(self.nameEntry, "Укажите название")
        # self.on_focus_out(self.descriptionEntry, "Укажите описание")

    def deleteRecipeHandler(self):
        if self.selectedIndex is None:
            return
        logic.recipes.pop(self.selectedIndex)
        self.update_view()


if __name__ == '__main__':
    root = Tk.Tk()
    cookbook = CookingRecipeApp(root)
    root.mainloop()
