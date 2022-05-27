import random as rd

from src.Agents.agent import Agent

MAX_AGE = 25

""" 
    Represents a daisy, white is represented by integer 1 and black's 2 
    A dasiy is either susceptible 0, infected, 1 or recovered 2
    colour: the colour of the daisy
    albedo: the albedo absorbed by the daisy (between 0 and 1)
"""
class Daisy(Agent):
    def __init__(self, colour, albedo) -> None:
        super().__init__(str(colour))
        self.age = Daisy.getRandAge(self)
        self.albedo = albedo # fraction (0-1) of energy absorbed as heat from sunlight

    """
        Performs a step for the daisy. 
        calculates the seed threshold which determines whether an empty nieghbour is seeded
        determines if an daisy has reached the end of its life
        temp: the current temperature of the patch
    """
    def step(self, temp):
        self.age += 1
        # threshold is a parabola with a peak of 1, it drops to 0 at temperatures of 5 degrees and 40 degrees C
        seed_threshold = ((0.1457 * temp) - (0.0032 * (pow(temp,2))) - 0.6443)
        r = rd.random()
        if self.age >= MAX_AGE: return self.die()
        elif r < seed_threshold: 
            return self.seed()
        else: return super().step(temp)

    """Return the result of a seeding"""
    def seed(self):
        return "seed"

    """Return the result of a death"""
    def die(self):
        return "die"

    """Return the string representing this daisy"""
    def toString(self):
        return super().toString()

    """Returns a random age between 1 and MAXAGE (default 25)"""
    @staticmethod
    def getRandAge(self):
        return rd.randint(1, MAX_AGE)