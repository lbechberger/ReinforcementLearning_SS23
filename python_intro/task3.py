class Book:
	
	def __init__(self, title, weight):
		self.title = title
		self.weight = weight

class Library:

	def __init__(self):
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def total_weight(self):
		weights = [book.weight for book in self.books]
		return sum(weights)

b1 = Book("ML in Python", 100)
b2 = Book("1000 Jokes", 200)
b3 = Book("PhD Thesis", 500)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print("Total weight of books is: ", lib.total_weight())
