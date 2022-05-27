
from math import log

""" 
Represents the invidiual cells in the world. 
Patches have a temperature which changes over time and are 
effected by the world and the agents in their neighbourhood 
"""
class Patch():
    def __init__(self, pos, agent, temp=0.0) -> None:
        self.pos = pos
        self.agent = agent
        self.temp = temp

    """
    Execute one step in the daisyworld. Calculate the temperature 
    and execute a step of the agent
    returns the result of agents step
    surface albedo: the albedo of the surface patch
    solar_luminosity: the luminosity of the planet
    """
    def step(self, surface_albedo, solar_lumniosity, infected):
        self.calc_temp(surface_albedo, solar_lumniosity)
        result = self.agent.step(self.temp, infected)
        return result

    """
    Calculated the temperature of the patch based on the:
    surface albedo of daisyworld, the solar luminosity and any absored 
    albedo from an agent on the patch
    surface albedo: the albedo of the surface patch
    solar_luminosity: the luminosity of the planet
    """
    def calc_temp(self, surface_albedo, solar_luminosity):
        # absorbed luminosity
        if self.agent.display != '0': 
            absorbed_lumniosity = ((1 - self.agent.albedo) * solar_luminosity)
        else: absorbed_lumniosity = (1 - surface_albedo) * solar_luminosity
        # gloabl heating
        if absorbed_lumniosity > 0:
            local_heating = 72 * log(absorbed_lumniosity) + 80
        else: local_heating = 80
        # final temperature
        temp = ((self.temp + local_heating) / 2)
        self.temp = temp

    """set the agent to the given agent"""
    def set_agent(self, agent):
        self.agent = agent

    """get a string representing the patch, get the agent toString"""
    def toString(self):
        return self.agent.toString()
