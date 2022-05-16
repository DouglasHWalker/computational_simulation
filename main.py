import numpy as np
import random as rd

class World:
    
    numPatches = 29

    def __init__(self, nBlacks, nWhites) -> None:
        self.numBlacks = nBlacks
        self.numWhites = nWhites
    
    def createWorldGrid(self):
        newWorld = []
        for i in range(self.numPatches):
            col = []
            for j in range(self.numPatches):
                col.append(0)
            newWorld.append(col)
        return newWorld
    
    def populateWorld(self, worldGrid):
        for i in range(self.numBlacks):
            position = World.getRandomPosition()
            while(worldGrid[position[0]][position[1]] != 0):
                position = World.getRandomPosition()
                #use 1 to represent black daisies
            worldGrid[position[0]][position[1]] = 1
        for j in range(self.numWhites):
            position = World.getRandomPosition()
            while(worldGrid[position[0]][position[1]] != 0):
                position = World.getRandomPosition()
                #use 2 to represent black daisies
            worldGrid[position[0]][position[1]] = 2
        return worldGrid

    def getRandomPosition():
        x = rd.randint(0, 28)
        y = rd.randint(0, 28)
        return [x, y]

class Daisy:
    maxAge = 25

    #use 1 to represent black daisies
    #use 2 to represent white daisies
    def __init__(self, colour, age) -> None:
        self.colour = colour
        self.age = age

    @staticmethod
    def getRandAge():
        return rd.randint(1, 25)

def main():
    daisyWorld = World(70, 70)
    daisyWorldGrid = daisyWorld.createWorldGrid()
    daisyWorldGrid = daisyWorld.populateWorld(daisyWorldGrid)
   
    for i in daisyWorldGrid:
        print(i,end='')
    print("\n")
   
    


if __name__ == "__main__":
    main()
