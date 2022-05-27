import csv

class Controller:
    def __init__(self, world, lifespan):
        self.world = world
        self.lifespan = lifespan

        self.current_tick = 0

    def go(self):
        self.__setup()
        fields = ['Tick', 'Total Population', 'White Daisies', 'Black Daisies', 'Global Temperature', 'Luminosity', 'Susceptible', 'Infected', 'Recovered', 'Killed by Disease']
        fileName = "daisyWorldOutput.csv"
        with open(fileName, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            while self.current_tick < self.lifespan:
                self.world.diffuse()
                population = self.world.getPopulation()
                infection = self.world.getSIR()
                row = [self.current_tick, population[0], population[1], population[2], self.world.getGlobalTemperature(), self.world.getLuminosity(), infection[0], infection[1], infection[2], infection[3]]
                csvwriter.writerow(row)
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
        print(self.world.getSIR())
        print(self.world.getGlobalTemperature())
        print(self.current_tick)
        print()

    def __setup(self):
        self.current_tick = 0
        self.world.killed_by_disease = 0
    
    def __tick(self):
        self.world.worldGrid = self.world.step()
        self.current_tick += 1

    def getTick(self):
        return self.current_tick
