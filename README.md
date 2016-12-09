# MoodTracker

MoodTracker is a Domain-Specific Language that helps users track their moods easily through writing journal entries in which they rate their mood. They have the option of seeing the trend of their moods in a graph or checking out their previous journal entries in a list mode.

To use the DSL, follow the instructions below. It is assumed that your computer already has Python 2 installed. 

1. Download the folder MoodTracker to your computer.

2. Open Terminal or other command line interpreter available on your computer. 

3. Enter "cd {path to the directory where you saved the MoodTracker folder/MoodTracker}"

4. Enter "python main.py", once you're in the MoodTracker folder.

5. You'll be prompted with a text menu and be able to enter a number to choose one of the options.

The text menu should look as the following.


1. Write a journal entry

2. Graph to see the trend of your moods from previous entries

3. List to see your previous entries

4. Exit


* When you are to write a journal entry, it has to follow the syntax of the DSL. See below.

`On {date}, I felt {what}, because {reason}, rated {number for rating}, color {characters},`

* Date can be written in any of the formats below to say Dec 12th 2014.

  12 04 14, 12-04-14, 12/04/14, 12 04 2014, 12-04-2014, 12/04/2014, 2014 12 04, 2014-12-04, 2014/12/04, December 12 2014, Dec 12 2014, 14 12 04, 14-12-04, 14/12/04, Dec 12 14, December 12 14

  If you don't specify the year, it will be automatically set to the current year.

  Date can also be written as one of the following:

  today, yesterday, previous day, a day ago
  
  Lastly, you also have the option of, in the place of date, saying n days ago, where n is an integer between 1 and 30.

* Please note that in the place of {number for rating}, you must enter a number between 0 and 10, 0 being extremely bad and 10 being perfect. It can be an integer or a decimal.

* Please also note that each component ends with a comma, including the last one where you specify a color of a bar in the bar graph.

  In the place of {characters}, you have to enter one of the following to specify a color for a bar.

  b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, nc = default

  The default color is set to be Magic mint (#AAF0D1).


* On the graph that shows the trend of your moods, you'll see an icon on the bottom left which you can click to save the graph on your computer.


Author: Woky(Won Kyoung) Park



