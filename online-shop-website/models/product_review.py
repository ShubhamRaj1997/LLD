import itertools


class ProductReview(object):
    itr = itertools.count()
    def __init__(self, product_id, user_id, title, rating, description):
        self.id = next(self.itr)
        self.product_id = product_id
        self.user_id = user_id
        self.title = title
        self.rating = rating
        self.description = description

# implement properties and setters
