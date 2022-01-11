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
    
    r=0
    T=T.reshape((4,9))
    print(T)
    heading=0
    state=env.get_observation()
    s=np.array(([state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8]]))
    action=np.dot(T,s)
    for i in range(10000):

        #action = env.action_space.sample()
        
        state, reward, done, _ = env.step(action)
        r+=reward 
        s=np.array(([state[0],state[1],state[2],state[3],state[4],state[5],state[6],state[7],state[8]]))
        action=np.dot(T,s)
        heading+=np.fabs(state[1])
        #print(reward)
        # height.append(reward)
    r/=20000
    heading/=20000
    print(heading)
    return -1*r  

        #print("action =", action, " ---> State =", state, " : Reward =", reward)


if __name__ == "__main__":
    

    h=random_agent
    T0=np.array(([1,-1,1,-1,1,-1,1,-1,1],
                [1,-1,1,-1,1,-1,1,-1,1],
                [1,-1,1,-1,1,-1,1,-1,1],
                [1,-1,1,-1,1,-1,1,-1,1]))
    T0=T0.reshape((1,36))
    sigma0=0.95
    

    T,es=cma.fmin2(h,T0,sigma0)

    

    #es.plot()

    # plt.plot(h)
    # plt.show()