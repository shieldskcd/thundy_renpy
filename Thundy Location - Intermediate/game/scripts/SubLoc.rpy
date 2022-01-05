screen SubLocHUD():
    frame:
        xpos 1500
        ypos 200

        vbox:
            for q in Sublocations:
                if q.parent == LocationID:
                    text q.name
