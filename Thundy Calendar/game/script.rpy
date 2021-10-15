define e = Character("Eileen", color = "#FF0044")
define d = Character("Dave", color = "#0033FF")
image main_bg = im.Scale("bg01.jpeg", 1920, 1080)
image red01 = "1.png"
image red02 = "2.png"
image red03 = "3.png"


label start:

    call variables
    show main_bg
    $ GameRunning = True
    while GameRunning:
        $ Output = WeekDays[Day] + " " + Months[Month] + " " + str(Days + 1) + " " +str(Hours) + ":" + str(Minutes)
        "[Output]"
        $ Minutes += 30
        if Minutes > 30:
            $ Minutes = 0
            $ Hours += 1
        if Hours > 23:
            $ Hours = 0
            $ Day += 1
            $ Days += 1
        if Day > 6:
            $ Day = 0
        if Days > MonthDays[Month]:
            $ Month += 1
            $ Days = 0
        if Month > 11:
            $ Month = 0

    return



label variables:
    $ WeekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    $ Months = ["January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"]
    $ MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    $ Minutes = 0
    $ Hours = 12
    $ Month = 0
    $ Day = 0
    $ Days = 0

    return
