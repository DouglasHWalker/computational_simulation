
from src.Agents.agent import Agent

class Empty(Agent):
    def __init__(self) -> None:
        super().__init__(display='0')

    def step(self, temp):
        return super().step(temp)

    def toString(self):
        return super().toString()