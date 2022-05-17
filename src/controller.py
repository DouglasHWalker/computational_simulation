
class Controller:
    def __init__(self, world, number_of_steps):
        self.world = world
        self.ticks = number_of_steps

        self.current_tick = 0

    def run(self):
        while self.current_tick < self.ticks:
            self.__tick()

    def __setup(self):
        pass
    
    def __tick(self):
        self.world.step()
        self.current_tick += 1