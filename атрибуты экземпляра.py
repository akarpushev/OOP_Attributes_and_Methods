class Book:
# Метод __init__  подготавливает объект класса к использованию.
# Определение пользовательских атрибутов экземпляра класса должно находиться в этом методе.
# Если атрибут отпределяется во внешнем методе, то
# ставят первональное значение None в __init__
# эти методы обязательно вызывают в__init__.
    def __init__(self):
        self.pages =None
        self.init_pages()
    def init_pages(self):
        self.pages =500

print(dir(Book()))# с помощью функ. dir вывод атрибутов

class Book:
    def __init__(self, name: str):
        self.name = name
# Все пользовательские атрибуты хранятся в атрибуте `__dict__`.
# `__dict__` согласно этой классификации, относится к “системным” (определённым python) атрибутам.
# Его задача — хранить **пользовательские атрибуты**.
# Он представляет собой словарь, в котором:
# - ключом является имя атрибута,
# - значением - значение атрибута.
book = Book("Букварь")
print(book.__dict__)  # {'name': 'Букварь'}

book_1 = Book("Букварь")
book_2 = Book("Азбука")

book_2.notes = "Заметки на полях" # добавление атрибута, которого не было

print(book_1.__dict__)  # {'name': 'Букварь'}
print(book_2.__dict__)  # {'name': 'Азбука', 'notes': 'Заметки на полях'}

class Book:
    ...
# Системный атрибут __class__ содержит в себе ссылку на класс, которому принадлежит экземпляр.
# Содержимое аналогично тому, что возвращает функция type()
book = Book()
print(type(book) is book.__class__)
print(book.__class__)
