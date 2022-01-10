from simulation import Simulation
from envs.heading_control_task import HeadingControlTask
from catalogs.catalog import DynamicCatalog
import matplotlib.pyplot as plt 
h=HeadingControlTask()
c=DynamicCatalog()
class Test(Simulation):
    def new(self):
        print("OK")
    # def __init__(self):
    #     Simulation()
        
    #     # print(self.aircraft_name)
if __name__ == '__main__' :
    t=Test(init_conditions=h.init_conditions)
    prop=[]
    reward=[]
    for _ in range(10000) :
        state=t.get_sim_state()
        p=t.get_property_value(c.__getattr__("position_h_agl_ft"))
        prop.append(p)
    
        #p=[t.get_property_value(prop) for prop in Catalog.values()]
        #print(p)
        r=h.get_reward(state,t)
        reward.append(r)
        #print(r)
        result=t.run()
        time=t.get_sim_time()
    print(len(prop))
    plt.plot(prop)
    plt.show()
    plt.plot(reward)
    plt.show()
        
    