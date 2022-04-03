from tkinter import Label
import time
import datetime as dt


class ElapsedTimeClock(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.lastTime = ""
        t = time.localtime()
        self.zeroTime = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
        self.tick()

    def tick(self):
        now = dt.datetime(1, 1, 1).now()
        elapsedTime = now - self.zeroTime
        time2 = elapsedTime.strftime('%H:%M:%S')
        if time2 != self.lastTime:
            self.lastTime = time2
            self.config(text=f'                                                     Runtime: {time2}')
        self.after(200, self.tick)