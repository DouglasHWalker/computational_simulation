import random as rd

from src.Agents.agent import Agent

# we wanted to replicate disease in humans
MAX_AGE = 25 # average human age
INIT_INFECT = 0.01

# spanish flu
RECOVER = 0.25 # develop immunity after 4 steps
INFECT = ((1/8) * 3) # R0 of 3
KILL = 0.1 # 10% of infected get killed
LOOSE_IMMUNITY = 0.01 # once you have it you mostly immune


""" 
    Represents a daisy, white is represented by integer 1 and black's 2 
    A dasiy is either susceptible 0, infected, 1 or recovered 2
    colour: the colour of the daisy
    albedo: the albedo absorbed by the daisy (between 0 and 1)
    infected: a parameter to assess whether the daisy starts it life  susceptible 0, infected, 1 or immune 2
"""
class Daisy(Agent):
    def __init__(self, colour, albedo, age=0, infected=0) -> None:
        super().__init__(str(colour))
        self.age = age
        if self.age == 0:
            self.age = Daisy.getRandAge(self)
        self.albedo = albedo # fraction (0-1) of energy absorbed as heat from sunlight
        self.infected = infected

        # if self.infected != 2: # if immunity not passed on
        if rd.random() < INIT_INFECT:
            self.infected = 1
        else: 
            self.infected = 0

    """
        Performs a step for the daisy. 
        Checks the infection results either: infected, recover, die, loose immunity
        calculates the seed threshold which determines whether an empty nieghbour is seeded
        determines if an daisy has reached the end of its life
        temp: the current temperature of the patch
        infected: either 0 or 1, represented whether an neighbour is present
    """
    def step(self, temp, infected):
        self.age += 1
        # threshold is a parabola with a peak of 1, it drops to 0 at temperatures of 5 degrees and 40 degrees C
        seed_threshold = ((0.1457 * temp) - (0.0032 * (pow(temp,2))) - 0.6443)
        r1 = rd.random()
        if self.infected == 0 and infected == 1: # susceptible
            if r1 < INFECT:
                self.infected = 1
        elif self.infected == 1:
            if r1 < KILL:
                return self.die("disease")
            if r1 < RECOVER: 
                self.infected = 2
        elif self.infected == 2:
            if r1 < LOOSE_IMMUNITY:
                self.infected = 0
        # print(self.infected)
        r2 = rd.random()
        if self.age >= MAX_AGE: 
            return self.die("age")
        elif r2 < seed_threshold: 
            return self.seed()
        else: return super().step(temp, infected)

    """Return the result of an infection"""
    def infect(self):
        return "infect"

    """Return the result of a seeding"""
    def seed(self):
        return "seed"

    """Return the result of a death, cause: the cause wither age or disease"""
    def die(self, cause):
        return cause

    """Return the string representing this daisy"""
    def toString(self):
        return super().toString()

    """
        return the infection status of this daisy: 
        A dasiy is either susceptible 0, infected, 1 or recovered 2
    """
    def getInfectionStatus(self): 
        return self.infected

    """Returns a random age between 1 and MAXAGE (default 25)"""
    @staticmethod
    def getRandAge(self):
        return rd.randint(1, MAX_AGE)