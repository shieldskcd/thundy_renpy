define e = Character("Eileen", color = "#FF0044")
define d = Character("Dave", color = "#0033FF")
image main_bg = im.Scale("bg01.jpeg", 1920, 1080)
image red01 = "1.png"
image red02 = "2.png"
image red03 = "3.png"


label start:

    call variables

    show main_bg

    "You are walking through your college campus and see a familiar face,
    you think it is your friend Eileen from school."

    #$ t = 1
    #while t < 3:
    #    show expression("[t].png")
    #    "click"
    #    $ t += 1


    d "Hi, Eileen!"

    show red01

    e "Hello, [PlayerName], How was your day?"

    menu:
        "My Day Was Great! Thanks Eileen":
            call GoodDay

        "My Day Was Not too Great.":
            jump BadDay

        "My Day Was Good but go to part B":
            call GoodDayB

    scene
    return

label GoodDay:
    hide red01
    show red02
    $ PlayerScore += 10
    e "I am glad you had a good day! Your score is [PlayerScore]"
    $ PlayerName += "\nNimrod"
    e "I will start calling you [PlayerName]"

label GoodDayB:
    e "Part 2 of the Good Day block"

    return

label BadDay:
    hide red01
    show red03
    $ PlayerScore -= 1
    e "I am sorry you had a bad day, Your score is [PlayerScore]"
    return

label variables:
    $ PlayerScore = 0
    $ PlayerName = "Dave"

    return
