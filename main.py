'''EXAMPLE MAIN'''
from steeringapp import SteeringApp
from agent import Agent
from MathLib import Vector2

def main():
    '''main execution func'''
    game = SteeringApp("Concrete Game")
    # make gameobjects to participate in game
    aa = Agent(Vector2(250, 250), 125)
    game.addtobatch(aa)
    game.run()
    

if __name__ == "__main__":
    main()