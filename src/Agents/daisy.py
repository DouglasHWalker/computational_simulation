import random as rd

from src.Agents.agent import Agent
from src.Agents.empty import Empty

MAX_AGE = 25

""" Represents a daisy, white is represented by integer 1 and black's 2 """
class Daisy(Agent):

    def __init__(self, colour, albedo) -> None:
        super().__init__(str(colour))
        self.age = Daisy.getRandAge(self)
        self.albedo = albedo # fraction (0-1) of energy absorbed as heat from sunlight

    def step(self, temp):
        self.age += 1
        # threshold is a parabola with a peak of 1, it drops to 0 at temperatures of 5 degrees and 40 degrees C
        seed_threshold = ((0.1457 * temp) - (0.0032 * (pow(temp,2))) - 0.6443)
        r = rd.random()
        if self.age >= MAX_AGE: return self.die()
        elif r < seed_threshold: 
            return self.seed()
        else: return super().step(temp)

    def seed(self):
        return "seed"

    def die(self):
        return "die"

    def toString(self):
        return super().toString()

    @staticmethod
    def getRandAge(self):
        return rd.randint(1, MAX_AGE)