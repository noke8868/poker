import sys
from holdem import Holdem
from betting import Blinds, NoBetLimit
from arena import PyArena
from timing import HalfSecondTiming

class TheAiGameArena(PyArena, Holdem, Blinds, NoBetLimit, HalfSecondTiming):
    """Arena for testing bots for http://theaigames.com
    Rules are heads-up, no limit hold'em"""
    pass

if __name__ == '__main__':
    arena = TheAiGameArena()
    bot_list = sys.argv[1:]
    arena.run(bot_list)
