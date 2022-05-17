

from src.Agents.agent import Agent


class Empty(Agent):
    def __init__(self) -> None:
        super().__init__(display='0')

    def step(self):
        return super().step()
        # if self.age >= self.MAX_AGE: self.grow()

    def toString(self):
        return super().toString()