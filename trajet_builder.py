from trajet import Trajet
from bon import Bon

class TrajetBuilder:
    def __init__(self):
        self.start = ""
        self.end = ""
        self.departure_date = ""
        self.arrival_date = ""
        self.bons = []

    def set_start(self, start):
        self.start = start
        return self

    def set_end(self, end):
        self.end = end
        return self

    def set_departure_date(self, date):
        self.departure_date = date
        return self

    def set_arrival_date(self, date):
        self.arrival_date = date
        return self

    def add_bon(self, description, cost):
        self.bons.append(Bon(description, cost))
        return self

    def build(self):
        return Trajet(self.start, self.end, self.departure_date, self.arrival_date, self.bons)
