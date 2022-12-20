class EndEvent():
    def __init__(self):
        self.__game_ended=False
        self.__is_ball_lost=False

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
        self.__is_ball_lost=False
        self.__winning_player=0

    def isBallLost(self):
        return self.__is_ball_lost

    def setBallLost(self):
        """
        This is called by a Ball class if the ball fails to make a collision with any surface for 10 seconds (it has flown off screen).  It will trigger a game reset.
        """
        self.__is_ball_lost=True