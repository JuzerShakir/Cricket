""" Lets Play Cricket """

# asking user for its name
user_name = input('What would you like me to call you, your name? : ')

print("\nHi", user_name, "! Let's play!", end="\n\n")

# for pauses in between running the program
import time
# pause
time.sleep(2)


####         TOSS           ####

# for generating random numbers
import random

# output randomly any single number from 1 to 1000 inclusive
computer_toss = random.randint(1, 1000)

user_toss = int(input("Computer has chosen a number, you need to guess it if the number is odd or even.\nPress '1' for odd or '0' if even...\n\n"))

print('Number generated by computer is', computer_toss)

# pause
time.sleep(2.5)

# computing if 'computer_toss' int is odd or even
if computer_toss % 2 == 0:
    toss = 0
else:
    toss = 1

# Flag value for toss decision
user_won_toss = False

# Who won the toss??
if toss == user_toss:
    user_won_toss = True
    print('\nCongratulations', user_name,'! You have won the toss!', end='\n\n')
else:
    print('\nSorry', user_name,'! You have lost the toss!', end='\n\n')

# pause
time.sleep(2.5)

# flag value if user bats or not in first inning
user_bat = False
# flag value if computer bats or not in first inning
computer_bat = False
# flag value if user bats or not in second inning
user_bat_sec_ing = False
# flag value if computer bats or not in second inning
computer_bat_sec_ing = False

# Bat or Bowl Decision
if user_won_toss:
    user_dec = int(input("\nWould you like to Bat or Bowl?\nPress '0' for bat or '1' for bowl..."))

    # if user chooses to bat
    if user_dec == 0:
        user_bat = True
        print('\n', user_name,'You have chosen to bat first.', end='\n\n')
        # pause
        time.sleep(2.5)
        print("Here you go!\nPress any number between 1 and 6.\nIf your number and computer's number match, then you will be out!\n")
    
    # if user choose to bowls
    else:
        computer_bat = True
        print('\n', user_name,'You have choosen to bowl first.')
        # pause
        time.sleep(2.5)
        print('Here you go!\nPress any number between 1 and 6.\nIf your number and computers number match, then I will be out!\n')

# if computer won toss
else:
    rand_num = random.randint(1, 1000)
    # if odd then it will choose bowl, or bat first
    if rand_num % 2 == 0:
        computer_bat = True
        print(user_name,'I choose to bat first!')
        # pause
        time.sleep(2.5)
        print('\nHere you go!\nPress any number between 1 and 6.\nIf your number and computers number match, then I will be out!\n')
    
    # computer chooses to bowl
    else:
        user_bat = True
        print(user_name,'I choose to bowl first!')
        # pause
        time.sleep(2.5)
        print('\nHere you go!\nPress any number between 1 and 6.\nIf your number and computers number match, then you will be out!\n')




#####       Play Function         #####

# funcion for first and second inning calculations, first param is boolean and second is integer
def game(chase, first_ing):
    # for total computation
    total = 0
    # flag for batting
    not_out = True

    # continue to bat until the player is not out
    while not_out:
        # asks user for score
        user_num = int(input(''))
        # generates random number
        compt_num = random.randint(1, 6)

        # Out or Not Out, if out break quit function, gives total
        if user_num == compt_num:
            # loop false
            not_out = False
            # prints total
            print('Howwzzaaatt...! Score is', total, end='\n\n')
            # breaks loop
            break

        # if user bats first or second inning
        if user_bat or user_bat_sec_ing:
            # computes total
            total = user_num + total
            print('Your batting at', total, '....')
            # if chasing, then matches the first inning score to second, if second inning is greater then break loop
            if chase and first_ing < total:
                break

        # if computer bats first or second inning
        else:
            total = compt_num + total
            print('Computer batting at', total, '....')
            if chase and first_ing < total:
                break

    return(total)


####         Lets play           ####

# flag for chasing score, useful in second inning
chase = False

# user bats first inning
if user_bat:
    # calls the function for computation by giving param values
    first_ing = game(chase, first_ing = 0)

    # outputs after first inning is over
    print(user_name,'You have scored', first_ing, '. Very good!\nNow its my turn to bat and beat your score.', end='\n\n')
    # pause
    time.sleep(2.5)
    print('I need to score', first_ing + 1, 'to win.', end='\n\n')

    # switching flag values, useful in game() function and for final results
    user_bat = False
    user_bat_sec_ing = False
    computer_bat_sec_ing = True

# if computer bats first
else:
    first_ing = game(chase, first_ing = 0)

    print(user_name,'I have scored', first_ing, '. Very good!\nNow its your turn to bat and beat my score.', end='\n\n')
    # pause
    time.sleep(2.5)
    print('You need to score', first_ing + 1, 'to win.', end='\n\n')

    computer_bat = False
    user_bat_sec_ing = True
    computer_bat_sec_ing = False


# second innings begins...
chase = True
# passing first inning score to break loop once chasing score is more than first innings
second_ing = game(chase, first_ing)

# pause
time.sleep(2.5)

# if computer batted second innings
if computer_bat_sec_ing:
    # WIN
    if first_ing > second_ing:
        print("\nCongratulations", user_name,"! You have beaten me! I loose! :)")
    # TIE
    elif first_ing == second_ing:
        print('\n', user_name,',our scores are similar. Match is a TIE!  :(')
    # LOOSE
    else:
        print("\nUnfortunately", user_name,", you lost the match! I win!  ;)")

# if user batted second innings
elif user_bat_sec_ing:
    # LOOSE
    if first_ing > second_ing:
        print("\nUnfortunately", user_name,", you lost the match! I win!  ;)")
    # TIE
    elif first_ing == second_ing:
        print('\n', user_name,',our scores are similar. Match is a TIE!  :(')
    # WIN
    else:
        print("\nCongratulations", user_name,"! You have beaten me! I loose! :)")


### THE END ###