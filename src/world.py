import random as rd
from src.Agents.daisy import Daisy
from src.Agents.empty import Empty
from src.patch import Patch

PATCHES = 5 # 28 x 28 in NetLogo model

""" Class represents the daisyworld holds all of the patches in the world """
class World:
    def __init__(self, percentage_whites, percentage_blacks,  luminosity=1.0, albedo=1.0, whiteAlbedo=0.75, blackAlbedo=0.25) -> None:
        # self.width = PATCHES
        # self.height = PATCHES
        # settings
        self.luminosity = luminosity
        self.albedo = albedo
        # daisies
        self.numWhites = int(PATCHES * percentage_whites)
        self.numBlacks = int(PATCHES * percentage_blacks)
        self.whiteAlbedo = whiteAlbedo
        self.blackAlbedo = blackAlbedo

        self.worldGrid = self.createWorldGrid()
        self.populateWorld()
    
    def step(self):
        for row in range(len(self.worldGrid)):
            for col in range(len(self.worldGrid[row])):
                cell = self.worldGrid[row][col]
                self.worldGrid[row][col] = cell.step()

    def createWorldGrid(self):
        newWorld = []
        for r in range(PATCHES):
            col = []
            for c in range(PATCHES):
                pos = (r,c)
                patch = Patch(pos, Empty())
                col.append(patch)
            newWorld.append(col)
        return newWorld

    def populateWorld(self):
        pos = World.getRandomPosition()
        for i in range(self.numBlacks):
            while(self.worldGrid[pos[0]][pos[1]].toString() != '0'):
                pos = World.getRandomPosition()
                #use 1 to represent black daisies
            self.worldGrid[pos[0]][pos[1]] = Daisy('1')
        for j in range(self.numWhites):
            while(self.worldGrid[pos[0]][pos[1]].toString() != '0'):
                pos = World.getRandomPosition()
                #use 2 to represent black daisies
            self.worldGrid[pos[0]][pos[1]] = Daisy('2')
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

    def getRandomPosition():
        x = rd.randint(0, PATCHES -1)
        y = rd.randint(0, PATCHES -1)
        return (x, y)

    def displayGrid(self):
        """ Prints the current state of the world grid to the terminal """
        for row in self.worldGrid:
            print([cell.toString() for cell in row])