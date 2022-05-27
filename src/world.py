import random as rd

from src.Agents.daisy import Daisy
from src.Agents.empty import Empty
from src.patch import Patch

""" Class represents the daisyworld holds all of the patches in the world 
At each tick, 
    the model is updated based on the temperature of each of the patches and the survivability of the daisies on the patches. 
    As the model progresses, the survivability of each daisy is checked based on the current conditions of the model.
    If the patch is empty, and the temperature of the patch is in the spawning range, a new daisy is spawned on the patch. The colour of the new daisy has the probability of being the same colour as its neighbours.
"""
class World:
    def __init__(self, percentage_whites, percentage_blacks,  patches=28, luminosity=1.0, albedo=0.4, whiteAlbedo=0.75, blackAlbedo=0.25) -> None:
        # board size
        self.patches = patches
        # settings
        self.luminosity = luminosity
        self.albedo = albedo
        # daisies
        self.numWhites = int(patches * patches * percentage_whites)
        self.numBlacks = int(patches * patches * percentage_blacks)
        self.whiteAlbedo = whiteAlbedo
        self.blackAlbedo = blackAlbedo

        self.killed_by_disease = 0
        self.worldGrid = self.createWorldGrid()
        self.populateWorld()
    
    def step(self):
        copy = self.worldGrid
        for row in range(len(self.worldGrid)):
            for col in range(len(self.worldGrid[row])):
                cell = self.worldGrid[row][col]
                infected = self.getInfectedNeighbours((cell.pos))
                result = cell.step(self.albedo, self.luminosity, infected)
                if result == "seed":
                    # get random neighbour
                    n = self.getEmptyNeighbour((cell.pos))
                    if n != cell.pos: 
                        # set to same colour daisy
                        y, x = n.pos
                        copy[y][x].set_agent(Daisy(cell.agent.display, cell.agent.albedo, cell.agent.infected))

                if result == "age" or result == "disease":
                    copy[row][col].set_agent(Empty())
                    if result == "disease": 
                        self.killed_by_disease += 1
        self.worldGrid = copy
        return copy

    def createWorldGrid(self):
        newWorld = []
        for r in range(self.patches):
            col = []
            for c in range(self.patches):
                pos = (r,c)
                patch = Patch(pos, Empty())
                col.append(patch)
            newWorld.append(col)
        return newWorld

    def populateWorld(self):
        pos = self.getRandomPosition()
        for i in range(self.numBlacks):
            while(self.worldGrid[pos[0]][pos[1]].toString() != '0'):
                pos = self.getRandomPosition()
                #use 1 to represent black daisies
            self.worldGrid[pos[0]][pos[1]].set_agent(Daisy('1', self.whiteAlbedo))
        for j in range(self.numWhites):
            while(self.worldGrid[pos[0]][pos[1]].toString() != '0'):
                pos = self.getRandomPosition()
                #use 2 to represent black daisies
            self.worldGrid[pos[0]][pos[1]].set_agent(Daisy('2', self.blackAlbedo))
        return self.worldGrid

    """ Tells each patch to give equal shares of (number * 100) percent of the value of patch-variable 
    to its eight neighboring patches. number should be between 0 and 1. Regardless of topology the sum 
    of patch-variable will be conserved across the world. (If a patch has fewer than eight neighbors, 
    each neighbor still gets an eighth share; the patch keeps any leftover shares.) """
    def diffuse(self):
        gridcopy = self.worldGrid
        neighbourcopy = self.worldGrid
        for row in self.worldGrid:
            for cell in row:
                neighbours = self.getNeighbours(cell.pos)

                # take 1 8th of 50% from each neighbour
                # get rid of 1 8th of 50% of own temp for each neighbour
                # oldval = gridcopy[cell.pos[0]][cell.pos[1]].temp
                # for n in neighbours:
                #     old_n_val = gridcopy[n.pos[0]][n.pos[1]].temp
                #     cell.temp += (old_n_val * 0.5) / 8
                # cell.temp -= (oldval * 0.5)
                # cell.temp += ((old_n_val * 0.5) / 8) * (8- len(neighbours))


                # from the source code, still doesn't work...
                # newVal = oldVal + amount * (sum / directions - oldVal)
                # oldval = gridcopy[cell.pos[0]][cell.pos[1]].temp
                # sum = 0
                # for n in neighbours:
                #     sum += n.temp
                # cell.temp = oldval + (0.5 * (sum / 8 - oldval))
                # if len(neighbours) < 8:
                #     cell.temp += (0.5 * (sum / 8 - oldval)) * (8 -len(neighbours))

                while neighbours:
                    n = rd.choice(neighbours)
                    delta = ((cell.temp * (0.5)))
                    n.temp += delta
                    cell.temp -= delta
                    neighbours.remove(n)
                if len(neighbours) < 8:
                    cell.temp += delta * (8 -len(neighbours))
        # self.worldGrid = gridcopy

    def getPopulation(self):
        """ Returns a tuple containing the population of daisies (white and black) """
        whitePop, blackPop = (0,0)
        for row in self.worldGrid:
            for cell in row:
                if cell.toString() == '1': whitePop += 1 
                if cell.toString() == '2': blackPop += 1
        return (whitePop + blackPop, whitePop, blackPop)
    
    def getGlobalTemperature(self):
        """ Returns a tuple containing the population of daisies (white and black) """
        tot_temp = 0
        for row in self.worldGrid:
            for cell in row:
                tot_temp += cell.temp
        avg_temp = tot_temp / (self.patches * self.patches)
        return avg_temp

    def getLuminosity(self):
        return self.luminosity
    
    def getSIR(self):
        susceptible, infected, recovered = (0,0,0)
        for row in self.worldGrid:
            for cell in row:
                if cell.toString() == '1' or cell.toString() == '2':
                    if cell.agent.infected == 0: susceptible += 1 
                    if cell.agent.infected == 1: infected += 1 
                    if cell.agent.infected == 2: recovered += 1
        return (susceptible, infected, recovered, self.killed_by_disease)

    def getRandomPosition(self):
        x = rd.randint(0, self.patches -1)
        y = rd.randint(0, self.patches -1)
        return (x, y)

    def displayGrid(self):
        """ Prints the current state of the world grid to the terminal """
        for row in self.worldGrid:
            print([cell.toString() for cell in row])

    def getNeighbours(self, pos):
        neighbours = []
        row, col = pos
        for x, y in ((row - 1, col), (row + 1, col), (row, col - 1),
            (row, col + 1), (row - 1, col - 1), (row - 1, col + 1),
            (row + 1, col - 1), (row + 1, col + 1)):
            if not (0 <= x < len(self.worldGrid) and 0 <= y < len(self.worldGrid[x])): 
                continue
            neighbours.append(self.worldGrid[x][y])
        return neighbours

    def getRandomNeighbour(self, pos):
        return rd.choice(self.getNeighbours(pos))
    
    def getEmptyNeighbour(self, pos):
        neighbours = self.getNeighbours(pos)
        while neighbours:
            n = rd.choice(neighbours)
            if n.toString() == '0': return n
            neighbours.remove(n)
        return pos

    def getInfectedNeighbours(self, pos):
        neighbours = self.getNeighbours(pos)
        for neighbour in neighbours:
            if neighbour.agent.toString() == '1' or neighbour.agent.toString() == '2':
                if neighbour.agent.getInfectionStatus() == 1:
                    return 1
        return 0