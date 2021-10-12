define e = Character("Eileen", color = "#FF0044")
define d = Character("Dave", color = "#0033FF")


label start:

    scene bg room

    show eileen happy

    "You are walking through your college campus and see a familiar face,
    you think it is your friend Eileen from school."

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
    e "I am glad you had a good day!"

label GoodDayB:
    e "Part 2 of the Good Day block"

    return

label BadDay:
    e "I am sorry you had a bad day"

    return
