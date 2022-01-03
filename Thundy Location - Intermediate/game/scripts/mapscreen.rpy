screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.jpeg"
        for q in Places:
            if q.IsActive:
                button:
                    xpos q.x
                    ypos q.y
                    text q.name
                    action Return(q.name)
