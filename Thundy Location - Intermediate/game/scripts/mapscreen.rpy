screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "map.jpeg"
        for q in Places:
            if q.IsActive:
                hbox:
                    xpos q.x
                    ypos q.y
                    imagebutton:
                        yalign 0.5
                        hover q.avatar
                        idle q.avatar
                        action SetVariable("LocationID", q.ID), Return(q.name)
                    button:
                        yalign 0.5
                        text q.name size 18
                        action SetVariable("LocationID", q.ID), Return(q.name)
