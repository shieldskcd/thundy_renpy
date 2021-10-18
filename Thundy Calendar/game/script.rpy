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
        "click"
        $ calendar.AddTime(4)
        if EventOne.DateCheck(calendar):
            call expression EventOne.Block

    return



label variables:
    $ calendar = Calendar(0, 0, 0, 0, ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 0, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    $ EventOne = Event(12, 2, 0, "EvOne", True)
    return

label EvOne:
    "this is Event One's Block"
    $ EventOne.SetInactive()
    return
