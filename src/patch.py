""" 
Represented the invidiual cells in the world. 
Patches have a temperature which changes over time and are 
effected by the world and the agents in their neighbourhood 
"""
from math import log

class Patch():
    def __init__(self, pos, agent, temp=0.0) -> None:
        self.pos = pos
        self.agent = agent
        self.temp = temp

    """
    Execute one step in the daisyworld. Calculate the temperature and execute a step of the agent
    returns the result of agents step
    """
    def step(self, surface_albedo, solar_lumniosity):
        self.calc_temp(surface_albedo, solar_lumniosity)
        result = self.agent.step(self.temp)
        return result

    """
    Calculated the temperature of the patch based on the:
    surface albedo of daisyworld, the solar luminosity and any absored albedo from an agent on the patch
    """
    def calc_temp(self, surface_albedo, solar_luminosity):
        # absorbed luminosity
        if self.agent.display != '0': 
            absorbed_lumniosity = ((1 - self.agent.albedo) * solar_luminosity)
        else: absorbed_lumniosity = (1 - surface_albedo) * solar_luminosity
        # gloabl heating - 
        if absorbed_lumniosity > 0:
            local_heating = 72 * log(absorbed_lumniosity) + 80
        else: local_heating = 80
        
        temp = ((self.temp + local_heating) / 2)
        self.temp = temp

    def set_agent(self, agent):
        self.agent = agent

    def toString(self):
        return self.agent.toString()