class Book:
    def __init__(self):
        self.pages = 500
        self.last_read_page = 0  # последняя прочитанная страница
        # если вызываем ф-ю внутри
        self.increment_last_read_page(200)
    def increment_last_read_page(self, read_pages: int):
        """
        Метод увеличивает последнюю прочитанную страницу.
        :param read_pages: Количество прочитанных страниц
        """
        self.last_read_page += read_pages

book = Book()
# если вызываем ф-ю снаружи
book.increment_last_read_page(200) # здесь не пишем self
