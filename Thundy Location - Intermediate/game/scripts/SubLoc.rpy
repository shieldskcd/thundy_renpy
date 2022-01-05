screen SubLocHUD():
    frame:
        xpos 1500
        ypos 200

        vbox:
            for q in Sublocations:
                if q.parent == LocationID:
                    button:
                        text q.name
                        action Return(q.name)

            button:
                text "\n\nExit"
                action Return(Location)
