# -*- coding: utf-8 -*-
# RoboMaster AI Challenge Simulator (RMAICS)

from kernel import Kernel


class Env(object):

    def __init__(self, agent_num, render=True):
        self.game = Kernel(car_num=agent_num, render=render)
        self.g_map = self.game.get_map()
        self.memory = []

    def reset(self):
        self.state = self.game.reset()
        # state, object
        self.obs = self.get_observation(self.state)
        return self.obs

    def step(self, actions):
        state = self.game.step(actions)
        obs = self.get_observation(state)
        rewards = self.get_reward(state)

        self.memory.append([self.obs, actions, rewards])
        self.state = state

        return obs, rewards, state.done, None

    def get_observation(self, state):
        # personalize your observation here
        # obs = [state.vision[0][1], state.vision[1][0], state.agents.x, state.agents.y, state.agents.angle,
        #        state.agents.yaw, state.agents.hp, state.agents.bullet]
        obs = state
        return obs

    def get_reward(self, state):
        # personalize your reward here
        reward_hp = state.agents[6] - 2000
        if state.agents[10]:
            reward_bullet = 1
        else:
            reward_bullet = 0
        reward_hit = -state.agents[14]
        rewards = reward_hp + reward_bullet + reward_hit
        return rewards

    def play(self):
        self.game.play()

    def save_record(self, file):
        self.game.save_record(file)
