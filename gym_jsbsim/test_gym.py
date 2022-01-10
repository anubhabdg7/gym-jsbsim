import gym
import gym_jsbsim 

env = gym.make("GymJsbsim-HeadingControlTask-v0")
#env = gym.make("k-v0")
env.reset()
done = False

while True :
   action = env.action_space.sample()
   state, reward, done, _ = env.step(action)
   env.render(mode='human')
   print(state)
   #print(reward)
