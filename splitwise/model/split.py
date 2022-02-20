class Split(object):
    def __init__(self, user):
        self.__user = user
        self.__amount = None

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value


class EqualSplit(Split):
    def __init__(self, user):
        super(EqualSplit, self).__init__(user)


class ExactSplit(Split):
    def __init__(self, user):
        super(ExactSplit, self).__init__(user)


class PercentSplit(Split):
    def __init__(self, user, percentage):
        super(PercentSplit, self).__init__(user)
        self.percentage = percentage
