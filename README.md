This is the Thundy Games tutorial for Development with Ren'Py. As this game gets more complicated, we will make a number of changes to keep up with the tutorial. However, if you want to start the series, you can find it here: https://youtube.com/playlist?list=PLKdE0Vv4UA5-dqJLpDkPt5CLQzc6hJ-uh

## So far, this is what we have done:
1. Created the initial game environment in Ren'Py
2. Connected the Ren'Py language package to the Atom.io Text Editor
3. Created a new character for use in the dialogue
4. Changed the text coloration for the speaker so that we can see the color to identify the speaker without reading their name
5. Created our first choice menu to allow the game to branch between a Good Day and a Bad Day.
6. Created a third menu choice to continue the Good Day using the jump and call commands
7. Added an image for the character Eileen
8. Change the picture of Eileen based on whether you have had a good or bad day
9. Worked with Scenes to make the images of Eileen disappear (this did not seem to work but the command is still there)
10. Experimented with an image click command to change the picture of Eileen when someone clicks the mouse (now commented out as it was for illustrative purposes and nothing more)
11. Created variables to store the Player's Score and the Player's name
12. Used variable changes to modify the name of the character (now commented out as it was for illustrative purposes)
13. Included text that shows the values of Player Name and Score
14. Used variable changes to increase or decrease the score of the player based on whether they had a good or bad day.
15. Created a new screen at the top of the main window to house the calendar.
16. Created a new file for events and create a class for the clock that can be called across the game system
17. Finally got the Calendar to work, it appears as though I had removed some of the needed code in the script.rpy file that was modifying calendar.
18. Adjusted the AddTime to add 4 hours instead of 1 per click.
19. Notified Reddit and Lemma Soft forums that issue was resolved.
20. Created a new class for Event Checks using a function
21. Wrote code instructions to check for the event trigger on the 3rd day at 12PM.
22. Created a new inventory system that tracks the items and weight
23. Added the ability to add an apple and a sword
24. Added a core display for the weight in the top center of the menu screen
25. Added limitation so that weight cannot be greater than 50.
26. Added buttons to allow display of invdividual items and weights
27. We just experimented with moving the quick menu from the bottom to the left or right and changing the xpos/ypos.
28. We modified the screens.rpy file to change the location and formatting of the choice menu button.
29. We modified the gui.rpy file to change the position of the menu items to be mid-left aligned
30. We changed the default font to use a different font (I used HelveticaNueue).
31. We changed the default color of the text to be slightly pink when not clicked.
32. Modified the main menu formatting to remove the History, Help, and About buttons
33. Experimented with changing the location of the main title screen
34. Changed the formatting and location of the Main Menu depending on startup location.
35. Uploaded a video to images/video and made it play in a loop on main menu.
36. Added a bullet to the icon menu in the game.
37. Adjusted icon size and opacity.
38. Created a new screen called "Game Guide" that will be used for pop ups.
39. Added two new dialogue lines
40. Called the Pop Up to display a new message screen.
41. Added four locations: Home, Shops, Aunt's House, and School.
42. Created a screen message to let us know which location we are currently in.
43. Added 4 distinct background images that change based on location specified.
44. Used Location.lower to make sure that the picture name does not have to be capitalized (i.e. Go Home = home.jpg, Shop = shop.jpg, etc.)
45. Used a pre-built fantasy map to create a map with coordinates for each location.
46. Confirmed that user can navigate from one location to another either with menu or with the map.
47. Changed icons on map to be an object with changeable properties instead of individual items.
48. Update events to auto generate locations using values in the item property for Places.

## We are now on lesson 24.
