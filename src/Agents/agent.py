""" 
Parent class for agents, takes the patch it is located 
on as a parameter 
"""
class Agent():
    def __init__(self, display=-1) -> None:
        self.display = display

    def step(self, temp):
        return self

    def toString(self):
        return self.display

