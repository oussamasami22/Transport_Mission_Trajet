from abs_mission import AbsMission
from bon import Bon

class Trajet(AbsMission):
    def __init__(self, start, end, departure_date, arrival_date, bons):
        self.start = start
        self.end = end
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.bons = bons

    def calculerCout(self):
        return sum(bon.get_cost() for bon in self.bons)

    def view(self, level=0):
        indent = "  " * level
        print(f"{indent}Trajet from {self.start} to {self.end}")
        print(f"{indent}Departure: {self.departure_date}, Arrival: {self.arrival_date}")
        for bon in self.bons:
            print(f"{indent}  Bon: {bon.description}, Cost: {bon.get_cost()}")
