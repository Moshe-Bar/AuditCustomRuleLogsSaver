from datetime import datetime
import re

class ASingleLog():
    def __init__(self, log=None,uts=None,id=None, regex_match:re.Match=None):
        if regex_match :
            self.log = regex_match.group(0)
            self.uts = float(regex_match.group(1))
            self.id = int(regex_match.group(2))
        else :
            self.log = log
            self.uts = float(uts)
            self.id = int(id)

    def __lt__(self, other):
        if self.utf > other.utf:
            return False
        elif self.utf < other.utf or self.index < other.index:
            return True

    def group_id(self):
        return f'{self.uts}:{self.id}
class AFullLog():
    def __init(self,logs:ASingleLog):




class ALog():
    def __init__(self, time_stamp=None, utf=None, index=None, event_type=None, full_log=None, log_key=None, user=None, dir=None,regex_match:re.Match=None):
        if regex_match:
            self.index = int(regex_match.group(2))
            self.utf = float(regex_match.group(1))
            self.event_type = regex_match.group(4)
            self.full_log = regex_match.group(0)
            self.key = regex_match.group(3)
            self.user = regex_match.group(5)
            self.dir = regex_match.group(6)
            self.time_stamp = str(datetime.fromtimestamp(int(regex_match.group(1).split('.')[0])))
        else:
            self.index = int(index)
            self.utf = float(utf)
            self.event_type = event_type
            self.full_log = full_log
            self.key = log_key
            self.user = user
            self.dir = dir
            self.time_stamp = time_stamp

    def fields(self)->():
        return(self.time_stamp,self.utf,self.index, self.event_type ,self.full_log, self.key, self.user,self.dir)

    def __lt__(self, other):
        if self.utf > other.utf:
            return False
        elif self.utf < other.utf or self.index < other.index:
            return True

    def __str__(self) -> str:
        return f'{self.time_stamp} | {str(self.utf)}:{self.index} | {self.event_type} | {self.key} | {self.user} {self.dir}'

# in case the db is empty this log used as latest log in db
log_0 = ALog('00:00:00', 0, 0, 'log_0', 'log_0', 'log_0', 'test_log_0', '/log_0/')