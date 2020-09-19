"""
Enter two numbers a and b to return its power
"""

def pow(a, b):
    """
    Return a to the power of b
    """
    if(b == 0):
        return 1
    else:
        return a**b

if __name__ == '__main__':
    a = float(input('Enter number'))
    b = float(input('Enter its power'))
    print(pow(a, b))
