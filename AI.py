import gym
import gym_pull

gym_pull.pull()

env = gym.make()
observation = env.reset()
