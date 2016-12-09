# MoodTracker

MoodTracker is a Domain-Specific Language that helps users track their moods easily through writing journal entries in which they rate their mood. They have the option of seeing the trend of their moods in a graph or checking out their previous journal entries in a list mode.

To use the DSL, follow the instructions below. It is assumed that your computer already has Python 2 installed. 
1. Download the folder MoodTracker to your computer.
2. Open Terminal or other command line interpreter available on your computer. 
3. Enter "cd {path to the directory where you saved the MoodTracker folder/MoodTracker}"
4. Enter "python main.py", once you're in the MoodTracker folder.
5. You'll be prompted with a text menu and be able to enter a number to choose one of the options.

The text menu should look as the following:
------------------------------ MENU ------------------------------
1. Write a journal entry
2. Graph to see the trend of your moods from previous entries
3. List to see your previous entries
4. Exit
-------------------------------------------------------------------

When you are to write a journal entry, it has to be in the syntax of the DSL.
`On {date}, I felt {what}, because {reason}, rated {number for rating}, color {character},`
