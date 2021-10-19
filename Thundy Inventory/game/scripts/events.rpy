init python:
    class Calendar(object):
        def __init__(self, Hours, Hour, Days, Day, Months, Month, WeekDays, MonthDays):
            self.Hour = Hour
            self.Hours = Hours
            self.Days = Days
            self.Day = Day
            self.Month = Month
            self.Months = Months
            self.WeekDays = WeekDays
            self.MonthDays = MonthDays
        @property
        def Output(self):
            return self.WeekDays[self.Day] + " " + self.Months[self.Month] + " " + str(self.Days+1) + " " + str(self.Hours).zfill(2) + ":" + "00"

        def AddTime(self, hours):
            self.Hours += hours
            if self.Hours > 23:
                self.Hours -= 24
                self.Day += 1
                self.Days += 1
            if self.Day > 6:
                self.Day = 0
            if self.Days > self.MonthDays[self.Month]:
                self.Month += 1
                self.Days = 0
            if self.Month > 11:
                self.Month = 0

    class Event(object):
        def __init__(self, Hour, Day, Month, Block, IsActive):
            self.Hour = Hour
            self.Day = Day
            self.Month = Month
            self.Block = Block
            self.IsActive = IsActive
        def DateCheck(self,c):
            if self.Day == c.Days and self.Hour == c.Hours and self.Month == c.Month and self.IsActive:
                return True
            else:
                return False
        def SetInactive(self):
            self.IsActive = False

    class Items(object):
        def __init__(self, name, val, weight, NoOwned, ID):
            self.name = name
            self.val = val
            self.weight = weight
            self.NoOwned = NoOwned
            self.ID = ID
        def AddItem(self):
            MaxWeight = 50
    
            if CurrentWeight + self.weight > MaxWeight:
                return
            else:
                self.NoOwned += 1
        @property
        def CurrentWeight(self):
            CurrentW = 0
            for q in Inventory:
                CurrentWeight += (q.weight * q.NoOwned)
            return CurrentW

    EVENTS = []
    Inventory = []
    t = 0

    while t < 50:
        EVENTS.append(Event(0, 0, 0, "", False))
        Inventory.append(Items("none", 0, 0, 0, t))
        t += 1
