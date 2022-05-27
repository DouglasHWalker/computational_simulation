
""" manages the daisyworld, detemrines interactions between agents and the world"""
from src.controller import Controller
from src.world import World

def main():
    daisyWorld = World(0.2, 0.2, patches=29, luminosity=1.0, albedo=0.4, whiteAlbedo=0.75, blackAlbedo=0.25)
    fat_controller = Controller(daisyWorld, lifespan=100)

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())
    print(daisyWorld.getGlobalTemperature())

    fat_controller.go()

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())
    print(daisyWorld.getGlobalTemperature())

if __name__ == "__main__":
    main()
