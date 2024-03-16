import torch
from rmaics import Rmaics
from kernel import record_player
import numpy as np
import DQN

lr = 2e-3
hidden_dim = 128
gamma = 0.98
epsilon = 0.01
target_update = 10
buffer_size = 10000
minimal_size = 500
batch_size = 64
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")


"""启动游戏环境"""
game = Rmaics(agent_num=2, render=True)
game.reset()
replay_buffer = DQN.ReplayBuffer(buffer_size)
state_dim = 1
action_dim = 1
agent = DQN(
    state_dim, hidden_dim, action_dim, lr, gamma, epsilon, target_update, device
)
return_list = []
# action format (int, np.array): [['x', 'y', 'rotate', 'yaw', 'shoot', 'supply', 'shoot_mode', 'auto_aim'], ...]
# action.shape = (car_num, 8)
for i in range(100):
    # actions = np.array([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1,
    # 1, 1, 1]])
    actions = np.array([[1, 1, 1, 1, 1, 1, 1, 1]])
    obs, reward, done, _ = game.step(actions)


# game.save_record('./records/record2.npy')
# player = record_player()
# player.play('./records/record2.npy')
