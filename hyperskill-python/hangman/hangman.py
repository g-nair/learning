import random
import string

print('H A N G M A N')

# Menu loop that breaks if the input is not 'play'
while input('Type "play" to play the game, "exit" to quit: ') == 'play':
    
    # Small selection of words, an answer is randomly selcted
    words = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(words)
    
    # Hiding the answer w/ hypens in a list for each letter
    out = ['-'] * len(answer)
    
    # Creating empty set to hold guessed letters, set count for wrong attempts
    gset = set()
    gcount = 0
    
    # 8 allowed *wrong* attempts
    while gcount < 8:
        print('')
        # Display progress by joining list, ask for input
        print(''.join(out))
        guess = input('Input a letter: ')

        # Check for single letter input
        if len(guess) != 1:
            print('You should input a single letter')
            continue

        # Check for lowercase ASCII (could sanitize the input with .lower() instead)
        elif guess not in string.ascii_lowercase:
            print('It is not an ASCII lowercase letter ')
            continue

        # Check if guess submitted previously
        elif guess in gset:
            print('You already typed this letter')
            continue

        # If the guess is in answer, add to the set
        elif guess in answer:
            gset.add(guess)
            
            # Fill out the output list with the guess where appropriate
            for i in range(len(answer)):
                if answer[i] == guess:
                    out[i] = guess
            
            # If doing so creates right answer, success! And break.
            if ''.join(out) == answer:
                print('')
                print(''.join(out))
                print('You guessed the word!')
                print('You survived!')
                break

        # If guess is valid entry, but not in answer, add to set, increment attempt
        else:
            gset.add(guess)
            print('No such letter in the word')
            gcount += 1
    
    # if while loop terminates without the break, game over
    else:
        print('You are hanged!')
