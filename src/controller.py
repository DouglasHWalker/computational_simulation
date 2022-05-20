
class Controller:
    def __init__(self, world, number_of_steps):
        self.world = world
        self.ticks = number_of_steps

        self.current_tick = 0

    def run(self):
        self.__setup()
        while self.current_tick < self.ticks:
            self.__tick()
            self.world.displayGrid()
            print(self.world.getPopulation())
            print()

    def __setup(self):
        self.current_tick = 0
    
    def __tick(self):
        self.world.worldGrid = self.world.step()
        self.current_tick += 1