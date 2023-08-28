class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @property
    def all(cls):
        # return all reviews in the list
        return [review for review in cls.reviews]
    @property
    def customer(self):
        # returns the object for that customer
        return self._customer
    @property
    def restaurant(self):
        # returns the object for that restaurant
        return self._restaurant
    

