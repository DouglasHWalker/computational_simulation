class Patch():
    def __init__(self, pos, agent, temp=0.0) -> None:
        self.pos = pos
        self.agent = agent
        self.temp = temp

    def step(self):
        return self.agent.step()

    def toString(self):
        return self.agent.toString()