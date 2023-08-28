from review import Review

class Restaurant:
    def __init__(self,name):
        if not isinstance(name,str):
            raise Exception("Name should be a string") # check instance and raise error if it is not a string
        else:
            self._name = name
            self.reviews = []

    @property
    def name(self):
        return self._name
    
    # def __str__(self):
    #     return str(self.name)
    
    @property
    def average_star_rating(self):
        # returns the average star rating for a restaurant based on its reviews
        # Reminder: you can calculate the average by adding up all the ratings and dividing by the number of ratings
        Avarage = 0
        for review in self.reviews:
            Avarage += review.rating
        return Avarage / len(self.reviews)
