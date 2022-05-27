""" 
Parent class for agents, takes the patch it is located 
on as a parameter 
display: the string representing the type of agent. 
display is Uused to display the agent in the world grid amd test equality
"""
class Agent():
    def __init__(self, display=-1) -> None:
        self.display = display

    """
    Abstract step method, 
    temperature and infected are unused in the abstract agent 
    """
    def step(self, temp):
        return self

    """Displays the display number fo this agent"""
    def toString(self):
        return self.display

