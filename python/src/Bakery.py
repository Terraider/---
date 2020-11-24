from src.Baker import Baker
from src.Pastry import Pastry


class Bakery:
    """Class bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Class constructor."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.recipes = {}
        self.bakers = []
        self.pastries = []

    def add_baker(self, baker: Baker) -> Baker:
        """Add baker."""
        if baker.experience_level >= self.min_experience_level:
            self.bakers.append(baker)
            return baker

    def remove_baker(self, baker: Baker):
        """Remove baker."""
        self.bakers.remove(baker)

    def add_recipe(self, name: str):
        """Add recipe."""
        sloznost = abs(len(name) * len(self.bakers) - (self.min_experience_level))
        self.recipes[name] = sloznost
        self.budget -= abs(len(name))
        if name not in self.recipes:
            self.recipes[name] = sloznost
        else:
            pass

    def make_order(self, name: str) -> Pastry:
        """Make order."""
        sloznost = abs(len(name) * len(self.bakers) - (self.min_experience_level))
        baker = (baker for baker in self.bakers)
        if name in self.recipes:
            for baker in self.bakers:
                if sloznost <= baker.experience_level:
                    self.budget += abs(len(name)) * 2
                    baker.money += abs(len(name)) * 2
                    baker.experience_level += abs(len(name))
                    self.pastries.append(Pastry(name, len(name)))
                    return Pastry(name, len(name))
        else:
            pass

    def get_recipes(self) -> dict:
        """Get recipes."""
        self.recipes.values()
        return self.recipes

    def get_pastries(self) -> list:
        """Get pastries."""
        self.pastries.copy()
        return self.pastries

    def get_bakers(self) -> list:
        """Get baker."""
        self.bakers.copy()
        return self.bakers

    def __str__(self):
        """Represent object in string format."""
        return "Bakery {}: {} baker(s)".format(self.name, len(self.bakers))
