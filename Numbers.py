## Just some function implementations of simple Number logic
## just for my practice
# no main block present
# I actually use Jupyter Notebook


import math

def Pi_upto_n_decimals(n):
    '''
    Calculates value of pi upto n decimal points
    '''
    return '{0:5.{1}f}'.format(math.pi,n)



def e_upto_n_decimals(n):
    '''
    Calculates value of e upto n decimal points
    '''
    return '{0:5.{1}f}'.format(math.e,n)



def fib(n):
    '''
    calculate fibonacci series upto n digits
    '''
    first= 0
    second = 1
    for i in range(n):
        yield first
        first, second = second, first + second



def find_primes(n):
    '''
    find prime numbers upto the value of n
    '''
    primes = [2]
    start =3
    if n < 2:
        return 0
    while start <= n:
        for prime in primes:
            if start % prime == 0:
                start += 2
                break

        else:
            primes.append(start)
            start += 2
    return primes




#from os import system
from IPython.display import clear_output

while True:
    # Asks untill user want to quit
    ask_user = input('enter your number or exit to end:')
    if ask_user[0].lower() == 'e':
        break

    else:
        #system('cls')
        clear_output()
        prime_nums= find_primes(int(ask_user))
        for num in prime_nums:
            print(num)



def total_cost_of_tile(tile_cost,width,height):
    total_area= width * height
    return total_area*tile_cost

## Just some code to run a timer for fixed number of seconds which ends with a beep sound in the end

def sound():
    import winsound
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

import time
import re
# define the countdown func.
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print('Time Out!')
    sound()


# input time in seconds
t = input("Enter the time as (2 mins or 20 secs) :")

# function call
countdown(int(t))



def fib(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b



def change(amount, cost):
    '''
    gives back the exact change to be provided in quarters, dimmes, nickels, pennies
    '''
    change = amount - cost
    str_change = str(change).split('.')
    left = int(str_change[1])

    quarter = int(left/25)
    left = left%25

    dimme = int(left/10)
    left = left%10

    nickel = int(left /5)
    pennie = left%5

    return (change,quarter,dimme,nickel,pennie)



def factorial(n):
    fact= 1
    for i in range(1,n+1):
        fact= fact*i
    return fact


def rec_factorial(n):
    fact = n
    if n==1:
        return 1
    else:
        return fact*rec_factorial(n-1)


import random

def coin_flip():
    '''
    checking number of heads/tails of n flips of a coin
    '''
    flip= random.randint(0,1)
    if flip == 1:
        flip='H'
    else:
        flip='T'
    return flip



def Binary(num):
    l=[]
    while num > 0:
        r=num%2
        num=int(num/2)
        l.append(r)

    l.reverse()
    for i in l:
        print(i)



def Dec(num):
    n=0
    dec=0
    while num >0:
        r=num%10
        dec=dec+(r*(2**n))
        num=num//10
        n+=1
    return dec
