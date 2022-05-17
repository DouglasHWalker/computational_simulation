import random as rd

from src.Agents.agent import Agent

class Empty(Agent):
    def __init__(self, pos) -> None:
        super().__init__(pos, display='0')

    def step(self):
        return super().step()

    def toString(self):
        return super().toString()