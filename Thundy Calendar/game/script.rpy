define e = Character("Eileen", color = "#FF0044")
define d = Character("Dave", color = "#0033FF")
image main_bg = im.Scale("bg01.jpeg", 1920, 1080)
image red01 = "1.png"
image red02 = "2.png"
image red03 = "3.png"


label start:

    call variables

    show main_bg

    while GameRunning:
        "[Hours]:[Minutes]:[Seconds]"
        $ Seconds += 1
        if Seconds == 60:
            $ Seconds = 0
            $ Minutes += 1
        if Minutes == 60:
            $ Hours += 1
            $ Minutes = 0
        if Hours == 24:
            $ Hours = 0
            


    return



label variables:
    $ GameRunning = True
    $ Hours = 0
    $ Minutes = 0
    $ Seconds = 0

    return
