
""" manages the daisyworld, detemrines interactions between agents and the world"""
from src.controller import Controller
from src.world import World

def main():
    daisyWorld = World(0.2, 0.2, patches=5)
    fat_controller = Controller(daisyWorld, 30)

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())

    fat_controller.run()

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())

    fat_controller.run()
    
    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())

if __name__ == "__main__":
    main()
