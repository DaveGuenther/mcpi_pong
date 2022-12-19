class EndEvent():
    def __init__(self):
        self.__game_ended=False

    def setWinningPlayer(self, player:int):
        """
        This function records which user has won the game.
        """
        self.__game_ended=True
        self.__winning_player = player
        print(player, "WINS!")
    
    def isEnded(self):
        return self.__game_ended

    def getWinningPlayer(self):
        return self.__winning_player

    def reset(self):
        self.__game_ended=False
        self.__winning_player=0