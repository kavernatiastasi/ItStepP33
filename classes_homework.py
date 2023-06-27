class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def display_info(self):
        print("Car Information:")
        print("Model:", self.model)
        print("Year:", self.year)
        print("Manufacturer:", self.manufacturer)
        print("Engine Capacity:", self.engine_capacity)
        print("Color:", self.color)
        print("Price:", self.price)


my_car = Car("Toyota Camry", 2022, "Toyota", 2.5, "Silver", 25000)
my_car.display_info()

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def display_info(self):
        print("Book Information:")
        print("Title:", self.title)
        print("Year:", self.year)
        print("Publisher:", self.publisher)
        print("Genre:", self.genre)
        print("Author:", self.author)
        print("Price:", self.price)

    def change_price(self, new_price):
        self.price = new_price

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def set_title(self, new_title):
        self.title = new_title

    def set_year(self, new_year):
        self.year = new_year

    def set_publisher(self, new_publisher):
        self.publisher = new_publisher

    def set_genre(self, new_genre):
        self.genre = new_genre

    def set_author(self, new_author):
        self.author = new_author

    def set_price(self, new_price):
        self.price = new_price


my_book = Book("To Kill a Mockingbird", 1960, "Harper Collins", "Fiction", "Harper Lee", 10.99)

my_book.display_info()

print("Title:", my_book.get_title())
print("Year:", my_book.get_year())
print("Publisher:", my_book.get_publisher())
print("Genre:", my_book.get_genre())
print("Author:", my_book.get_author())
print("Price:", my_book.get_price())

my_book.change_price(12.99)

my_book.display_info()

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print("Stadium Information:")
        print("Name:", self.name)
        print("Opening Date:", self.opening_date)
        print("Country:", self.country)
        print("City:", self.city)
        print("Capacity:", self.capacity)

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self, new_name):
        self.name = new_name

    def set_opening_date(self, new_opening_date):
        self.opening_date = new_opening_date

    def set_country(self, new_country):
        self.country = new_country

    def set_city(self, new_city):
        self.city = new_city

    def set_capacity(self, new_capacity):
        self.capacity = new_capacity


my_stadium = Stadium("Динамо", "12 Червня, 1933", "Україна", "Київ", 16873)

my_stadium.display_info()

print("Name:", my_stadium.get_name())
print("Opening Date:", my_stadium.get_opening_date())
print("Country:", my_stadium.get_country())
print("City:", my_stadium.get_city())
print("Capacity:", my_stadium.get_capacity())

my_stadium.change_capacity(23000)

my_stadium.display_info()
