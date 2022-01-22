# 100 Days Of Code - Log


### Day 5: January 22, 2022

Went though Chapter 17 of the [Python Crash Course](https://nostarch.com/pythoncrashcourse2e) book today, titled "Working With APIs"<br>
The source code for the chapter can be found - [here](https://github.com/ehmatthes/pcc_2e/tree/master/chapter_17)

**Progress**:
- Accessed the GitHub API via [requests](https://docs.python-requests.org/en/latest/) (one of my first times doing any API call ... I think?)
- Queried for the top Python repos - and found a lot of interesting repos in the process!
- Took the query output and displayed it in an offline Plotly bar chart (Also a first for me)

The chapter also had a section on retriving articles and associated data from [Hacker News](https://news.ycombinator.com/), which I had only recently heard about.

Great exposure project! It led to some project ideas that would combine the use of the Wikipedia API and the Spotify API!

<br>

---

<br>

### Day 3-4: January 12-20, 2022

Whew! Life happened. No reason to give excuses, but I simply didn't make the time to sit down for a full hour because ... reasons!
Instead I sat down for 20-30 minutes at a time and learned the following, which I'm going to consider 2 hours == 2 days.

**Progress**:
- Watched the [Intro to Object-Oriented Programming (OOP) in Python](https://realpython.com/courses/intro-object-oriented-programming-oop-python/) course from RealPython
  - Reading about OOP in textbooks was never that inspiring, but with this course and making my own example class for fun, I think I have a better grasp on classes.
- Did a good deal of foundational Pandas learning
  - Found myself with a small excel dataset to play with and decided to work with it in Python instead of Excel itself. Essentially figured out how to do the basics that I could do in SQL in Pandas, which included `pd.read_excel()`,`pd.merge()` to perform joins, using Select-equivalent syntax to get columns from the dataframe, and using `pd.assign()` to create/add my own calculated field to the dataframe. This was exciting as learning pandas/having a good reason to learn has been on my agenda for years. More to come for sure.
- Got a detailed review of Entity Relationship Diagrams (ERD) from a [couple YouTube videos](https://youtu.be/QpdhBUYk7Kk)
  - I have been using these diagrams at work for a while now, but got the spark to look into them further. I previously understood the one to one-to-many type of relationship but became aware of all the other cardinality notations. Definitely a good thing to have in the toolkit.

**Link to work:**
- Might as well share the [example class](https://github.com/g-nair/learning/blob/master/100-days-of-code/code/RealPython-OOP-Example.py) I created for the OOP course. I had some fun modelling a class around the water bottle that was sitting in front of me.

<br>

---

<br>

### Day 2: January 11, 2022

**Today's Progress**: Another few chapters of [Python Crash Course](https://nostarch.com/pythoncrashcourse2e) this morning! Topics covered were
- User Input
- while Loops
- Functions

Specifics I was happy to have refreshed:
- the use of while loops to iterate until a list is emptied or no longer contains a specified element through pop/remove
- how to use positional, keyword, and default arguments as appropriate
- dealing with optional arguments, as well as arbitrary (\*args) and arbitrary keyword (\*\*kwargs) arguments
- and lastly, a reminder on how to save files to import modules into main code files

I then decided I would give the [PyBites Intro Code Challenges](https://codechalleng.es/bites/intro) a try.

I made it through the first four challenges and found myself *very* confused by the [fifth challenge](https://codechalleng.es/bites/105/) because of how bizzare the syntax of the function definiton looked: `def slice_and_dice(text: str = TEXT) -> list:`

I had never seen anything like it! I ended up spending way too much time trying to figure out what was happening.  
Thankfully the Python Docs had my back - letting me know to relax... It was just a [Function Annotation](https://docs.python.org/3/tutorial/controlflow.html#function-annotations).

Now I know! I did like the platform a lot, I will have to restart from the 5th intro challenge onward.

<br>

---

<br>

### Day 1: January 10, 2022

**Today's Progress**: Read through the first six chapters of [Python Crash Course](https://nostarch.com/pythoncrashcourse2e) refresing on basics such as
- Variables
- Data Types
- Lists
- for Loops
- if Statements
- and Dictionaries

Some bits and bobs that I hadn't remembered since I did this last were things like
- The difference between `pop()`, `del`, and `remove()` when working with lists
- How beautiful list comprehensions can bring a tear to one's eye
- Using `get()` when working with dictionaries allows you to set a default output if the key you tried to access isn't there
- Sets being an easy way to remove duplicates from a list

I also browsed through the first three chapters of [How to Automate the Boring Things](https://nostarch.com/automatestuff2) which covered similar topics!

**Thoughts:**  

If you're fortunate enough to have both of these books, the difference in presentation of the material and the various specifics each author decides to include in their basics sections really does provide a comprehensive refresher on Python syntax/what's possible with core Python.
