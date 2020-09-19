## Just some function implementations of simple String logic
## just for my practice
# no main block present
# I actually use Jupyter Notebook


def fizzbuzz():
    '''
    prints fizz if number is divisible by 3
    prints buzz if number is divisible by 3
    prints fizzbuzz if number is divisible by both 3 and 5

    '''
    for i in range(1,101):
        # checking for range upto 100 numbers
        if i%3 == 0 and i%5 ==0:
            print('FizzBuzz')

        elif i%3 == 0:
            print('Fizz')

        elif i%5 == 0:
            print('Buzz')

        else:
            print(i)



def reverse_string(text):
    '''
    Reverse a string

    '''
    return text[::-1]

def palindrome(text):
    '''
    palindrome or not

    '''
    text= text.replace(' ','')
    return text == text[::-1]


def pig_latin(test):
    '''
    pig latin formatting of text
    '''
    if test[0] in 'aeiou':
            return test+'yay'

    for i in test:
        if i in 'aeiou':
            return test[test.index(i):]+test[:test.index(i)]+'ay'


def vowel(test):
    '''
    counting number of vowels
    '''
    count=0
    l=[]
    for i in test:
        if i in 'aeiou':
            count+=1
            l.append(i)

    return l


from collections import defaultdict

def counter(string=None,file=None):
    '''
    returning number of count of each word in a string/file
    '''
    d= defaultdict(lambda : 0)

    if string:
        new=string.split()
        print(new)
        for i in new:
            d[i]=d[i]+1

    if file:
        with open(file,'r') as f:
            new= f.read()
            new = new.split()

            for i in new:
                d[i]= d[i]+1

    return d


def file(name,mode):
    '''
    performing various user defined actions on files
    '''
    myfile=open(name,mode)
    if mode=='r':
        content=myfile.read()
        print(content)
    else:
        myfile.write(input('add text:'))
    myfile.close()
    print('Success')
