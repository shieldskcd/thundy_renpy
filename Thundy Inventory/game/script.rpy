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
            "Add Sword":
                $ Inventory[1].AddItem()
            "Display number of apples":
                $tmp = Inventory[0].NoOwned
                "You have [tmp] Apples"
            "Display number of Swords":
                $tmp = Inventory[1].NoOwned
                "You have [tmp] Swords"
            "Display weight":
                $ wt = Inventory[0].CurrentWeight
                "The Current Weight is [wt]"

    return



label variables:
    $ Inventory[0] = Items("apple", 1, 2, 0, 0)
    $ Inventory[1] = Items("Sword", 100, 20, 0, 1)
    return
