import __init__ as init 
from gym_jsbsim.simulation import Simulation

class Test(init,Simulation):
    def __init__(self):
        print("OK")

if __name__ == '__main__' :
    t=Test(init,Simulation)
    