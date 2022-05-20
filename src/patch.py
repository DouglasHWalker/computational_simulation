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

    def step(self, surface_albedo, solar_lumniosity):
        self.calc_temp(surface_albedo, solar_lumniosity)
        result = self.agent.step(self.temp)
        return result

    def calc_temp(self, surface_albedo, solar_luminosity):
        absorbed_lumniosity = (1 - surface_albedo) * solar_luminosity
        if self.agent.display != '0': 
            absorbed_lumniosity = ((1 - self.agent.albedo) * solar_luminosity)
        if absorbed_lumniosity > 0:
            local_heating = 72 * log(absorbed_lumniosity) + 80
        else: local_heating = 80
        temp = ((self.temp + local_heating) / 2)
        self.temp = temp

    def set_agent(self, agent):
        self.agent = agent

    def toString(self):
        return self.agent.toString()

    """
    let absorbed-luminosity 0
    let local-heating 0
    ifelse not any? daisies-here
    [   ;; the percentage of absorbed energy is calculated (1 - albedo-of-surface) and then multiplied by the solar-luminosity
        ;; to give a scaled absorbed-luminosity.
        set absorbed-luminosity ((1 - albedo-of-surface) * solar-luminosity)
    ]
    [
        ;; the percentage of absorbed energy is calculated (1 - albedo) and then multiplied by the solar-luminosity
        ;; to give a scaled absorbed-luminosity.
        ask one-of daisies-here
        [set absorbed-luminosity ((1 - albedo) * solar-luminosity)]
    ]
    ;; local-heating is calculated as logarithmic function of solar-luminosity
    ;; where a absorbed-luminosity of 1 yields a local-heating of 80 degrees C
    ;; and an absorbed-luminosity of .5 yields a local-heating of approximately 30 C
    ;; and a absorbed-luminosity of 0.01 yields a local-heating of approximately -273 C
    ifelse absorbed-luminosity > 0
        [set local-heating 72 * ln absorbed-luminosity + 80]
        [set local-heating 80]
    set temperature ((temperature + local-heating) / 2)
        ;; set the temperature at this patch to be the average of the current temperature and the local-heating effect
    end
    """