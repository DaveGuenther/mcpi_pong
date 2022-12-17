
import datetime

class SquareWave():

    def __init__(self, period_length=1000):
        """
        This class starts a square wave (on/off) timer at period_length milliseconds and runs in the background.  The class manages a single boolean state (True/False) to indicate which period of the quarewave the instance is on.  It can be used to create flashing objects like sprites on the screen
        """
        self.__last_timestamp = datetime.datetime.now()
        self.__period = period_length
        self.__state=True

    def getState(self):
        return self.__state

    def update(self):
        now = datetime.datetime.now()
        diff = now-self.__last_timestamp
        if diff.seconds*1000>=self.__period:
            self.__state = not self.__state
            self.__last_timestamp=now



