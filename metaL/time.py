from metaL import *

import datetime as dt

class Time(Object):
    def __init__(self, V=None):
        self.now = dt.datetime.now()
        self.date = self.now.strftime('%d.%m.%Y')
        self.time = self.now.strftime('%H:%M:%S')
        super().__init__(f'{self.date} {self.time}')

    def json(self):
        return {"date": f"{self.date}", "time": f"{self.time}"}
