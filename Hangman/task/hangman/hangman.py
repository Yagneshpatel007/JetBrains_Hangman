# Write your code here
import random
from string import ascii_lowercase
words = ('python', 'java', 'kotlin', 'javascript')

b = random.choice(words)
print("H A N G M A N\n")
ddd = list(b)
dj = set(ddd)
comp = '-' * len(b)
complete = list(comp)
improve = []
for r in range(8):
    if '-' not in complete:
        break
    ffd = True
    while ffd:
        if '-' not in complete:
            print(f"You guessed the word {comp}!")
            print("You survived!")
            break
        else:

            print(comp)
            latter = input('Input a letter:')
            if latter in improve and r != 7:
                print("You've already guessed this letter\n")
                break
            elif len(latter) != 1 and r != 7:
                print('You should input a single letter\n')
                break
            elif latter not in ascii_lowercase and r != 7:
                print('Please enter a lowercase English letter\n')
                break
            if latter in dj:
                improve.append(latter)
                dj.remove(latter)
                for j in range(len(b)):
                    if latter == ddd[j]:
                        complete[j] = latter
                        for c in range(len(b)):
                            comp = ''.join(complete)
                print()
            elif r == 7:
                if latter not in ascii_lowercase:
                    print('Please enter a lowercase English letter')
                elif latter not in dj:
                    print("That letter doesn't appear in the word")
                elif latter in improve:
                    print("You've already guessed this letter")

                elif len(latter) != 1:
                    print('You should input a single letter')
                print("You lost!")
                ffd = False
                break
            else:
                improve.append(latter)
                print("That letter doesn't appear in the word\n")
                ffd = False