from abs_mission import AbsMission

class Mission(AbsMission):
    def __init__(self, description):
        self.description = description
        self.elements = []

    def add_element(self, element):
        if isinstance(element, AbsMission):
            self.elements.append(element)

    def calculerCout(self):
        return sum(element.calculerCout() for element in self.elements)

    def view(self, level=0):
        indent = "  " * level
        print(f"{indent}Mission: {self.description}")
        for element in self.elements:
            element.view(level + 1)
