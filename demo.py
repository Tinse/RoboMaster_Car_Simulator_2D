from env import Env
game = Env(agent_num=4)
game.reset()
# only when render = True
game.play()

game.save_record('./records/record1.npy')