from pong.timer import SquareWave

strobe = SquareWave(period_length=50)

while 1:
    strobe.update()
    print(strobe.getState())