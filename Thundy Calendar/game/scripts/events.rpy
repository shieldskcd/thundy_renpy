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
            return self.WeekDays[self.Day] + " " + self.Months[self.Month] + " " + str(self.Days+1) + " " + str(self.Hours).zfill(2)
