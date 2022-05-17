""" 
Represented the invidiual cells in the world. 
Patches have a temperature which changes over time and are 
effected by the world and the agents in their neighbourhood 
"""
class Patch():
    def __init__(self, pos, agent, temp=0.0) -> None:
        self.pos = pos
        self.agent = agent
        self.temp = temp

    def step(self):
        return self.agent.step()

    def toString(self):
        return self.agent.toString()