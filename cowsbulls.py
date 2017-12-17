import random, os
os.system ('clear')

def compare_bullscows (usernum, targetnum, Bulls, Cows):
    if usernum == targetnum:
        return True
    testnum = list (usernum)
    targetnum = list(targetnum)

    #for i in range (4):
    for j in range (4):
        if testnum[j] == targetnum[j]:
            Bulls += 1
            targetnum[j] = 'a'
            testnum[j] = 'b'
            continue
        elif Bulls == 4:
            return True
    for j in range (4):
        for i in range (4):
            if testnum[i] == targetnum[j]:
                Cows += 1
                targetnum[j] = 'a'
                testnum[i] = 'b'
    print ("Bulls " + str(Bulls) + ", Cows " + str(Cows) + ' \n\n')
    Bulls = 0
    Cows = 0
    return False




# generate a number
targetnum = str(random.randint(0, 9999)).zfill(4)
print (targetnum + ''' A four number digit was generated
Can you guess what it is? Everytime you guess a digit
in its right place it is counted as a Bull. Every time you guess
a digit in a wrong spot it counts as a Cow. Goodluck CowBoyGirl \n\n''')

# ask a number and send it to compare_bullscows
Bulls = 0
Cows = 0
guess = 0
while True:
    usernum = input('What is your guess?:> ')
    if usernum == targetnum:
        print ('Yu wun focker in: WHOLE IN ONE!!!')
        break
    else:
        result = compare_bullscows(usernum, targetnum, Bulls, Cows)
        guess += 1
        while result == False:
            usernum = input ('Next guess:> ')
            result = compare_bullscows(usernum, targetnum, Bulls, Cows)
            guess += 1

        print ('Yu wun FACCKKAAAAAAHHHHH in ' + str(guess) + ' guesses!!! CHEAT')
        break

print ('END')
