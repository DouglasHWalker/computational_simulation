import csv

class Controller:

    def __init__(self, world, number_of_steps):
        self.world = world
        self.ticks = number_of_steps

        self.current_tick = 0

    def run(self):
        self.__setup()
        fields = ['Tick', 'White Daisies', 'Black Daisies', 'Global Temperature', 'Luminosity']
        fileName = "daisyWorldOutput.csv"
        with open(fileName, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            while self.current_tick < self.ticks:
                self.__tick()
                self.world.displayGrid()
                print(self.world.getPopulation()[0])
                print(self.world.getGlobalTemp())
                print(self.world.getLuminosity())
                print(self.current_tick)
                row = [self.current_tick, self.world.getPopulation()[0], self.world.getPopulation()[1], self.world.getGlobalTemp(), self.world.getLuminosity()]
                csvwriter.writerow(row)
                print()

    def __setup(self):
        self.current_tick = 0
    
    def __tick(self):
        self.world.worldGrid = self.world.step()
        self.current_tick += 1

    def getTick(self):
        return self.current_tick