""" 
Parent class for agents, takes the patch it is located 
on as a parameter 
"""
class Agent():
    def __init__(self, display=-1) -> None:
        self.display = display

    """Abstract step method"""
    def step(self, temp, infected):
        return self

    """Displays the display number fo this agent"""
    def toString(self):
        return self.display

