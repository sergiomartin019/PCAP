class Book:
    def __init__(self,title,quantity,author,price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None
        
    def set_discount(self,discount):
        self.__discount = discount
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
    def __repr__(self):
        return f"Titulo: \'{self.title}\', Cantidad: {self.quantity}, Author: {self.author}, Precio: {round(self.get_price(),3)}€"

book1 = Book("donquiyote", 13, "doflamingo", 56)
book2 = Book("asd",2, "carmen mola", 67)
book3 = Book("elpepe", 56, "etese", 1)
print(book1)
print(book2)
print(book3)
print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.get_price())


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages
class Academic(Book):
    def __init__(self, title, quantity, author, price,branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch
    def __repr__(self):
        return f"Titulo: \'{self.title}\', Género: {self.branch}, Cantidad: {self.quantity}, Author: {self.author}, Precio: {round(self.get_price(),3)}€"

novela1 = Novel("donquijote", 30,"doflamingo", 30,560)
novela1.set_discount(0.20)

ensayo1 = Academic("libro chulo",12,"escritor chulo chulo",18,"psicologia")
print(ensayo1)
print(novela1)
