
""" manages the daisyworld, detemrines interactions between agents and the world"""
from src.controller import Controller
from src.world import World

def main():
    daisyWorld = World(0.5, 0.5, patches=5, luminosity=1.0, albedo=0.4, whiteAlbedo=0.75, blackAlbedo=0.25)
    fat_controller = Controller(daisyWorld, number_of_steps=18)

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())
    print(daisyWorld.getGlobalTemp())

    fat_controller.run()

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())
    print(daisyWorld.getGlobalTemp())

    fat_controller.run()
    
    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())
    print(daisyWorld.getGlobalTemp())

if __name__ == "__main__":
    main()
