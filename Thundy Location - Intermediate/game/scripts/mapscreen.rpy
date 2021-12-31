screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.jpeg"
        button:
            xpos 750
            ypos 500
            text "Home"
            action Return("Home")

        button:
            xpos 486
            ypos 315
            text "Aunt's House"
            action Return("Aunt's House")

        button:
            xpos 508
            ypos 751
            text "Shop"
            action Return("Shop")

        button:
            xpos 470
            ypos 600
            text "School"
            action Return("School")
