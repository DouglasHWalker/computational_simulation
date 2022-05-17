import random as rd

from src.Agents.agent import Agent
from src.Agents.empty import Empty

MAX_AGE = 25

""" Represents a daisy, white is represented by integer 1 and black's 2 """
class Daisy(Agent):

    def __init__(self, pos, colour, albedo) -> None:
        super().__init__(pos, str(colour))
        self.age = Daisy.getRandAge(self)
        self.albedo = albedo # fraction (0-1) of energy absorbed as heat from sunlight
        self.temperature = self.calcTemperature()

    def step(self):
        self.age += 1
        # threshold is a parabola with a peak of 1, it drops to 0 at temperatures of 5 degrees and 40 degrees C
        seed_threshold = ((0.1457 * self.temperature) - (0.0032 * (pow(self.temperature, 2))) - 0.6443)
        if self.age >= MAX_AGE: return self.die()
        elif rd.random() < seed_threshold: return self.seed()
        else: return super().step()

    def seed(self):
        return "seed"

    def die(self):
        return "die"

    def toString(self):
        return super().toString()

    def calcTemperature(self):
        return 23.5
    """
    let absorbed-luminosity 0
    let local-heating 0
    ifelse not any? daisies-here
    [   ;; the percentage of absorbed energy is calculated (1 - albedo-of-surface) and then multiplied by the solar-luminosity
        ;; to give a scaled absorbed-luminosity.
        set absorbed-luminosity ((1 - albedo-of-surface) * solar-luminosity)
    ]
    [
        ;; the percentage of absorbed energy is calculated (1 - albedo) and then multiplied by the solar-luminosity
        ;; to give a scaled absorbed-luminosity.
        ask one-of daisies-here
        [set absorbed-luminosity ((1 - albedo) * solar-luminosity)]
    ]
    ;; local-heating is calculated as logarithmic function of solar-luminosity
    ;; where a absorbed-luminosity of 1 yields a local-heating of 80 degrees C
    ;; and an absorbed-luminosity of .5 yields a local-heating of approximately 30 C
    ;; and a absorbed-luminosity of 0.01 yields a local-heating of approximately -273 C
    ifelse absorbed-luminosity > 0
        [set local-heating 72 * ln absorbed-luminosity + 80]
        [set local-heating 80]
    set temperature ((temperature + local-heating) / 2)
        ;; set the temperature at this patch to be the average of the current temperature and the local-heating effect
    end
    """

    @staticmethod
    def getRandAge(self):
        return rd.randint(1, MAX_AGE)