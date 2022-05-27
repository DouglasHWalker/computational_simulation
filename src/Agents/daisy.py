import random as rd

from src.Agents.agent import Agent

# we wanted to replicate disease in humans
MAX_AGE = 25 # average human age
INIT_INFECT = 0.01

# spanish flu
RECOVER = 0.2 # develop immunity after 4 steps
INFECT = ((1/8) * 6)  / (1/RECOVER) # R0 of 6
KILL = 0.1  / (1/RECOVER) # 10% of infected get killed
LOOSE_IMMUNITY = 0.05 # once you have it you mostly immune


""" Represents a daisy, white is represented by integer 1 and black's 2 """
class Daisy(Agent):

    def __init__(self, colour, albedo, infected=0) -> None:
        super().__init__(str(colour))
        self.age = Daisy.getRandAge(self)
        self.albedo = albedo # fraction (0-1) of energy absorbed as heat from sunlight
        self.infected = infected

        if self.infected != 2: # if immunity not passed on
            if rd.random() < INIT_INFECT:
                self.infected = 1
            else: 
                self.infected = 0

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
        if self.age >= MAX_AGE: return self.die("age")
        elif r2 < seed_threshold: 
            return self.seed()
        else: return super().step(temp, infected)

    def infect(self):
        return "infect"

    def seed(self):
        return "seed"

    def die(self, cause):
        return cause

    def toString(self):
        return super().toString()

    def getInfectionStatus(self): 
        return self.infected

    @staticmethod
    def getRandAge(self):
        return rd.randint(1, MAX_AGE)