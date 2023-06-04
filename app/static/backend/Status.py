# Created by RitsukiShuto on 2023/06/04.
# 在室状況のステータス設定を行うクラス
#

class Status:
    def __init__(self):
        self.status = ''
        self.message = ''
        self.end_time = ''
        self.isInSchedule = False

    def setStatus(self, status, message, time):
        self.status = status
        self.message = message
        self.end_time = time

    def setStatus(self, status, message):
        self.status = status
        self.message = message
    
    def getStatus(self):
        return self.status, self.message, self.end_time