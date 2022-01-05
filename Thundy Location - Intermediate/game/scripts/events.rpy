init python:
    import math
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

            if self.CurrentWeight + self.weight > MaxWeight:
                return
            else:
                self.NoOwned += 1

        @property
        def CurrentWeight(self):
            CurrentW = 0
            for q in Inventory:
                CurrentW += (q.weight * q.NoOwned)
            return CurrentW

    class Place(object):
        def __init__(self, ID, x, y, name, IsActive):
            self.ID = ID
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive

        @property
        def avatar(self):
            icon = "icons/" + self.name.lower() + "_icon.png"
            return(icon)

        @property
        def rooms(self):
            outlist = []
            for q in Sublocations:
                if q.parent == self.ID:
                    outlist.append(q.ID)
            return outlist

    class SubPlace(object):
        def __init__(self, ID, parent, name, IsActive):
            self.ID = ID
            self.parent = parent
            self.name = name
            self.IsActive = IsActive


    Places = []
    Sublocations = []
    EVENTS = []
    Inventory = []
    t = 0

    while t < 50:
        EVENTS.append(Event(0, 0, 0, "", False))
        Inventory.append(Items("none", 0, 0, 0, t))
        Places.append(Place(t, 0,0,"", False))
        Sublocations.append(SubPlace(t, -1,"", False))
        t += 1

    Places[0] = Place(0, 750,500,"Home", True)
    Places[1] = Place(1, 380,380, "Shop", True)
    Places[2] = Place(2, 486,125, "Aunt's House", True)
    Places[3] = Place(3, 430,590, "School", True)

    Sublocations[0] = SubPlace(0, 0, "Bathroom", True)
    Sublocations[1] = SubPlace(1, 0, "Bedroom", True)
    Sublocations[2] = SubPlace(2, 0, "Kitchen", True)
    Sublocations[3] = SubPlace(3, 0, "Game Room", True)
