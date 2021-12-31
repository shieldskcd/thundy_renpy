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
            ypos 125
            text "Aunt's"
            action Return("Aunt's House")

        button:
            xpos 330
            ypos 380
            text "Shop"
            action Return("Shop")

        button:
            xpos 410
            ypos 580
            text "School"
            action Return("School")
