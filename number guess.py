import random
def guess(x):
    random_guess=random.randint(1,x)
    guess=0
    while guess != random_number:
         guess=int(input(f'Guess a number betwee 1 and{x}:'))
    if guess < random_number:
        print('sorry')
    elif guess > random_number:
            print('sorry')

            print('çongrats')

def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c':
         guess = random.randint(low,high)
         feedback = input(f'{guess} is high(H),is low(L),is correct(C)')
         if feedback == 'h':
             high = guess - 1 
        elif feedback == 'l':
             low = guess + 1 
             
        print(f 'guess correctly number, {guess},')
        
computer_guess(10)
            
