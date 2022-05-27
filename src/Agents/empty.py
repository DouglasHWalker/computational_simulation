
from src.Agents.agent import Agent

"""
    Represents an empty agent, This agent does not perform any action
    display: the string representing the type of agent. 
    display is Uused to display the agent in the world grid amd test equality
"""
class Empty(Agent):
    def __init__(self) -> None:
        super().__init__(display='0')

    """perform and empty step"""
    def step(self, temp, infected):
        return super().step(temp, infected)

    """ return the string representing this empty agent, deafult 0"""
    def toString(self):
        return super().toString()