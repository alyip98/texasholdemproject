from pypokerengine.api.game import setup_config, start_poker
from players.rvplayer import RVPlayer
from players.randomplayer import RandomPlayer

#TODO:config the config as our wish
config = setup_config(max_round=10, initial_stack=10000, small_blind_amount=10)

config.register_player(name="f1", algorithm=RVPlayer())
config.register_player(name="random", algorithm=RandomPlayer())


game_result = start_poker(config, verbose=1)
