class Cash(object):
    def __init__(self, notes, denomination):
        self.notes = notes
        self.denomination = denomination

    def get_amount(self) -> float:
        return self.denomination * self.notes
