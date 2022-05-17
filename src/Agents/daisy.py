import random as rd

from src.Agents.agent import Agent
from src.Agents.empty import Empty


MAX_AGE = 25

""" Represents a daisy, white is represented by integer 1 and black's 2 """
class Daisy(Agent):

    def __init__(self, colour) -> None:
        super().__init__(str(colour))
        self.age = Daisy.getRandAge(self)

    def step(self):
        self.age += 1
        if self.age >= MAX_AGE: 
            return self.die()
        return super().step()

    def die(self):
        return Empty()

    def toString(self):
        return super().toString()

    @staticmethod
    def getRandAge(self):
        return rd.randint(1, MAX_AGE)