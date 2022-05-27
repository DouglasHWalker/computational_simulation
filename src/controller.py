import csv

"""
The controller class handles the communication between the user (main) file and the daisyworld.
"""
class Controller:
    def __init__(self, world, lifespan):
        self.world = world
        self.lifespan = lifespan
        self.current_tick = 0

    """
    Run the daisyworld, executing steps from 0 to the given lifespan of the world
    """
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
                row = [self.current_tick, population[0], population[1], population[2], 
                self.world.getGlobalTemperature(), self.world.getLuminosity(), 
                infection[0], infection[1], infection[2], infection[3]]
                csvwriter.writerow(row)
                self.__tick()
                self.toString()

                if self.extinct():break

    """
    Checks whether the daisyworld has become extinct (zero daisy population)
    """
    def extinct(self):
        is_extinct = self.world.getPopulation()[0] == 0
        if is_extinct:
            print("------EXTINCTION------")
            print()
        return is_extinct

    """
    Output the daisyworld to the terminal
    """
    def toString(self):
        self.world.displayGrid()
        print(self.world.getPopulation())
        print(self.world.getSIR())
        print(self.world.getGlobalTemperature())
        print(self.current_tick)
        print()

    """
    Reset the daisyworld so that no ticks have occured and there is no disease
    """
    def __setup(self):
        self.current_tick = 0
        self.world.killed_by_disease = 0

    """
    Execute one step in the daisyworld, update the current tick counter
    """
    def __tick(self):
        self.world.worldGrid = self.world.step()
        self.current_tick += 1

    """
    Gets the current tick count
    """
    def getTick(self):
        return self.current_tick
