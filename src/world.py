from copy import deepcopy
import random as rd

from src.Agents.daisy import Daisy
from src.Agents.empty import Empty
from src.patch import Patch

VON_NEUMAN = True

""" Class represents the daisyworld holds all of the patches in the world 
At each tick, 
    the model is updated based on the temperature of each of the patches and the survivability of the daisies on the patches. 
    As the model progresses, the survivability of each daisy is checked based on the current conditions of the model.
    If the patch is empty, and the temperature of the patch is in the spawning range, a new daisy is spawned on the patch. The colour of the new daisy has the probability of being the same colour as its neighbours.

     set max-age 25
  set global-temperature 0

"ramp-up-ramp-down":        0.8
"low solar luminosity":     0.6
"our solar luminosity:      1.0 
"high solar luminosity":    1.4
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

        self.worldGrid = self.createWorldGrid()
        self.populateWorld()
    
    def step(self):
        copy = self.worldGrid
        for row in range(len(self.worldGrid)):
            for col in range(len(self.worldGrid[row])):
                cell = self.worldGrid[row][col]
                result = cell.step(self.albedo, self.luminosity)

                if result == "seed":
                    # get random neighbour
                    n = self.getEmptyNeighbour((cell.pos))
                    if n != cell.pos: 
                        # set to same colour daisy
                        y, x = n.pos
                        copy[y][x].set_agent(Daisy(cell.agent.display, cell.agent.albedo))

                if result == "die":
                    copy[row][col].set_agent(Empty())
                    
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

    def getPopulation(self):
        """ Returns a tuple containing the population of daisies (white and black) """
        whitePop, blackPop = (0,0)
        for row in self.worldGrid:
            for cell in row:
                if cell.toString() == '1': whitePop += 1 
                if cell.toString() == '2': blackPop += 1
        return (whitePop, blackPop)

    def getLuminosity(self):
        raise NotImplementedError("NOT YET IMPLEMENTED")

    def getGlobalTemperature(self):
        raise NotImplementedError("NOT YET IMPLEMENTED")

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
        y, x = pos
        if x != 0: # not on left edge
            neighbours.append(self.worldGrid[y][x-1]) # left
        if x != self.patches-1: # not on right edge
            neighbours.append(self.worldGrid[y][x+1]) # right
        if y != 0: # if not in top row
            neighbours.append(self.worldGrid[y-1][x]) # up
        if y != self.patches-1: # if not in bottom row
            neighbours.append(self.worldGrid[y+1][x]) # down
        if VON_NEUMAN:
            pass
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