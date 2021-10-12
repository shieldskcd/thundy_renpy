define e = Character("Eileen", color = "#FF0044")
define d = Character("Dave", color = "#0033FF")
image main_bg = im.Scale("bg01.jpeg", 1920, 1080)
image red01 = "red01.png"
image red02 = "red02.png"
image red03 = "red03.png"

label start:

    show main_bg

    "You are walking through your college campus and see a familiar face,
    you think it is your friend Eileen from school."

    show red01

    d "Hi, Eileen!"

    e "Hello, Dave, How was your day?"

    menu:
        "My Day Was Great! Thanks Eileen":
            call GoodDay

        "My Day Was Not too Great.":
            jump BadDay

        "My Day Was Good but go to part B":
            call GoodDayB

    "This code ends the Start Block"

    return

label GoodDay:
    show red02
    e "I am glad you had a good day!"

label GoodDayB:
    e "Part 2 of the Good Day block"

    return

label BadDay:
    show red03
    e "I am sorry you had a bad day"

    return
