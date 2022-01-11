import gym
import gym_jsbsim
import matplotlib.pyplot as plt 
import numpy as np 
import cma

def random_agent(T):

   env = gym.make("GymJsbsim-HeadingControlTask-v0")
   env.reset()
   done = False
   height=[]
    # T=np.array(([1,-1,1,-1,1],
    #             [1,-1,1,-1,1],
    #             [1,-1,1,-1,1],
    #             [1,-1,1,-1,1]))
   state=env.get_observation()
   print(state)
   s=np.array(([state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8]]))
   action=np.dot(T,s)
   r=0
   #T=T.reshape((4,5))
   #print(T)
   for i in range(20000):

      #action = env.action_space.sample()
      
      state, reward, done, _ = env.step(action)
      r+=reward 
      s=np.array(([state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8]]))
      action=np.dot(T,s)
      #print(reward)
      height.append(state[3])
   r/=20000
   print("Done")
   return height

        #print("action =", action, " ---> State =", state, " : Reward =", reward)


if __name__ == "__main__":

    

   
   T0=np.array(([ 0.00575889, -2.27098336,  1.48434751, -1.51558547,  1.12000105, -0.61831949,
   2.35547237, -3.23922453,  1.37604619],
 [ 0.85363138, -1.80614312,  1.09579167,  0.34929059,  2.21464716,  0.43490936,
   0.54581667, -2.11214526,  0.88342211],
 [ 0.96800723, -1.50247225,  0.48622981,  0.1008121,   3.12226111, -1.28142003,
   0.35875837, -1.31312597,  4.14972054],
 [-0.06347886, -0.79196168,  0.56950706, -2.07283184,  0.85761307,  0.22598774,
   1.36823576, -0.51322748, -1.14205766]))
   h=random_agent(T0)

    

    #es.plot()

   plt.plot(h)
   plt.show()