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


class Delay():
    def __init__(self, duration=1000):
        """
        Initializes a timer counting up to duration in milliseconds.  Must call start() to start/restart the timer).
        """
        self.__state=False
        self.__duration = duration


    def start(self, duration=None):
        """
        Starts the timer with the given duration in milliseconds.  If this function is called while the timer is already running, it will restart
        """
        if duration is not None:
            self.__duration = duration
        self.__start_time = datetime.datetime.now()
        self.__state=True

    def getState(self):
        """
        returns True if timer is still running.  Returns false if the timer has ended
        """
        now = datetime.datetime.now()
        diff = now-self.__start_time
        if diff.seconds*1000>=self.__duration:
            self.__state=False
        return self.__state