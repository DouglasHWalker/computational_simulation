
class Controller:
    def __init__(self, world, lifespan):
        self.world = world
        self.lifespan = lifespan

        self.current_tick = 0

    def go(self):
        self.__setup()
        while self.current_tick < self.lifespan:
            self.world.diffuse()
            self.__tick()
            self.toString()

            if self.extinct():break

    def extinct(self):
        is_extinct = self.world.getPopulation()[0] == 0
        if is_extinct:
            print("------EXTINCTION------")
            print()
        return is_extinct

    def toString(self):
        self.world.displayGrid()
        print(self.world.getPopulation())
        print(self.world.getGlobalTemp())
        print(self.current_tick)
        print()

    def __setup(self):
        self.current_tick = 0
    
    def __tick(self):
        self.world.worldGrid = self.world.step()
        self.current_tick += 1

