""" 
Parent class for agents, takes the patch it is located 
on as a parameter 
"""
class Agent():
    def __init__(self, pos, display=-1) -> None:
        self.pos = pos
        self.display = display

    def step(self):
        return self

    def toString(self):
        return self.display

