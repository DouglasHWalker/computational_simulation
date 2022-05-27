
from src.controller import Controller
from src.world import World

"""
manages the daisyworld, detemrines interactions between agents and the world

percentage_whites, percentage_blacks: the percentage of initial daisies
patches=28: the size of the world 28x28 default
luminosity=1.0: the solar luminosity of the world
albedo=0.4: the surface_albedo, the mount of temp absorbed by the surface
whiteAlbedo=0.75, blackAlbedo=0.25: the amount of temp absorbed by the daisies
"""
def main():
    daisyWorld = World(percentage_whites=0.2, percentage_blacks=0.2, 
        patches=29, luminosity=1.0, albedo=0.4, whiteAlbedo=0.75, blackAlbedo=0.25)

    fat_controller = Controller(daisyWorld, lifespan=500)

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())
    print(daisyWorld.getGlobalTemperature())

    fat_controller.go()

    daisyWorld.displayGrid()
    print(daisyWorld.getPopulation())
    print(daisyWorld.getGlobalTemperature())

if __name__ == "__main__":
    main()
