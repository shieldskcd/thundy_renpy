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
        menu:
            "Add apple":
                $ Inventory[0].AddItem()
            "Display weight":
                $ wt = Inventory[0].CurrentWeight
                "The Current Weight is [wt]"

    return



label variables:
    $ Inventory[0] = Items("apple", 1, 1, 0, 0)
    return
