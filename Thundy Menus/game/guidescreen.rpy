screen GameGuide(GuideMessage):
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        vbox:
            text GuideMessage
            text ""
            button:
                text "Close"
                action Return()
                
