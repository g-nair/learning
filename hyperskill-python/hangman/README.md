### Hangman

The hangman project is described by the platform as follows:

> ##### About
> Games can help you kill time when you’re bored. But before smartphones, people played games the classic way – with paper and pencil. Let’s recreate one such game and improve your programming skills in the process. In this project, you will code Hangman, a game where the player has to guess a word, letter by letter, in a limited number of attempts. Make a program that plays Hangman with you – and good luck with the guessing!

> ##### Learning outcomes
> Best project for Python Basics: uses functions, loops, lists, and other variables. The Random module is a cherry on top. Don’t be intimidated by the number of stages – they ensure that your immersion in Python is smooth and safe.

#### My thoughts:
This was a great refresher project! I enjoyed scratching my head figuring out some of the specific asks the platform had, such as the feedback when you input a character that you have before. The course nudges you in the direction of using a set to accomplish this task, as inserting duplicates does not affect the length of the set, and it maintains a faster search than a list would as the game goes on. I have taken a few intro-level python courses before this one, and enjoyed how immersive this project was.

#### Possible improvements:
The first change I would make to improve the experience of the game is to allow the full word to be guessed instead of letter by letter. This could be inserted where the code checks for the length of the guess - if it is not a single letter, it could check if the input is equal to the answer, and print the winning message and break.
Second, the instructions were to tell the user if the letter was not an ASCII lowercase letter. While this helps filter our non-alphabet guesses, the input could be cleaned up by applying .lower(). And lastly! I would include some sort of indicator of how many guesses the player has left. I'd imagine some command line stick figure art would be most entertaining.

On to the next one!
