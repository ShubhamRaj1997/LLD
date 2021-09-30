class Bounty(object):
    def __init__(self, reputation, expiry):
        self.__reputation = reputation
        self.__expiry = expiry

    def update_reputation(self, reputation):
        self.__reputation = reputation
