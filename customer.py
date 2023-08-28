from .review import Review


class Customer:
    customers = []  # class variable list to store all customers

    def __init__(self, given_name, family_name):  # initialize the constructor
        self._given_name = given_name
        self._family_name = family_name
        self.reviews = []
        self.customers.append(self)

    @property
    def given_name(self):  # get the given name(first name)
        return self._given_name

    @given_name.setter
    def given_name(self, new_given_name):  # set the given name to new name
        self._given_name = new_given_name

    @property
    def family_name(self):  # get family name(last name)
        return self._family_name

    @family_name.setter  # set to a new name
    def family_name(self, new_family_name):
        self._family_name = new_family_name

    # return fullname
    # access it as an attribute rather than a method
    @property
    def full_name(self):
        return '{} {}'.format(self._given_name, self._family_name)

    # use class method to print all customer in the list
    # use property to access all methos as an attribute
    @classmethod
    def all(cls):
        return [customer.full_name for customer in cls.customers]

    @property
    def restaurants(self):
        #   Returns a **unique** list of all restaurants a customer has reviewed
        return list({reviews.restaurant for reviews in self.reviews})

    @property
    def add_review(self, restaurant, rating):
        # creates a new review and associates it with that
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

        # Aggregation and Association
    def num_reviews(self):
        # Returns the total number of reviews that a customer has authored
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        # given a string of a **full name**, returns the **first customer** whose full name matches
        for customer in cls.customers:
            if customer.full_name == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        # given a string of a given name, returns an **list** containing all customers with that given name
        return [customer for customer in cls.customers if customer.given_name == name]
