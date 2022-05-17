""" Parent class for agents, takes the patch it is located on as a parameter """
from doctest import DocFileSuite


class Agent():
    def __init__(self, display=-1) -> None:
        self.display = display

    def step(self):
        return self

    def toString(self):
        return self.display

