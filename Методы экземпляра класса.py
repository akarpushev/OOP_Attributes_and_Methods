a = '1\n1'
print(a)
print(repr(a))

class Book:
    #def __init__(self):
    def __init__(self, pages):
        #self.pages = 500
        self.pages = pages

    def __str__(self):
        return f"Book = {self.pages}"

    def __repr__(self):
        #return f"Book repr {self.pages}"
        ##return f"Book pages={self.pages}"
        return f"Book repr pages={self.pages!r}"# !r показывает строковый характер

#book = Book()
book = Book(50)
print(book)
print(Book(40))
print([book])
print([Book('50')])

# class Book:
#     def __init__(self, name: str):
#         self.name = name
#
# book = Book("Букварь")
# print(book)
# print(f"{book}")
# print(str(book))

# class Book:
#     def __init__(self, name: str):
#         self.name = name
#
# book = Book("Букварь")
# print(repr(book))
# print(f"{book!r}")

class Book:
    def __init__(self, pages):
        self.pages = pages
        self.last_read_page = 0

    def increment_last_read_page(self, read_pages: int):
        self.last_read_page += read_pages

    def __str__(self):
        return f"Book = {self.pages}"

    def __repr__(self):
        result = f"{self.__class__.__name__}("#узнать название класса
        for key, value in self.__dict__.items():
            result += f",{key}={value!r}"
        return result + ")"

print([Book('100'), Book(200), Book('300')])
book = Book(55)
print(book.__class__.__name__)#узнать название класса