def collatz_conjecture(num):
    '''
    finding number
    '''
    steps=1
    while num !=1:
        if num%2 ==0:
            num= num/2
            steps+=1
            
        else:
            num= (num*3)+1
            steps+=1
            
    return steps


def euclid(num1,num2):
    '''
    finding GCD of two numbers using Euclids Algoritm
    '''
    num1,num2=max(num1,num2),min(num1,num2)
    
    while num2 != 0:
        temp = num2
        num2 = num1%num2
        num1 = temp
        
    return num1


def seive(n):
    '''
    finding prime numbers using seive of erasthothenes technique
    '''
    l = [i for i in range(2,n+1)]
    
    for i in l:
        for j in l:
            if j%i ==0 and j >= i**2:
                l.pop(l.index(j))
                
    for i in l:
        print(i)



def closest(*args):
    '''
    takes n input points and returns the closest distance between two points
    '''
    dist = []
    
    for i in range(len(args)):
        for j in range(i % len(args)):
            x1,y1 = args[i]
            x2,y2 = args[j]
            
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            dist.append(distance)
        
        dist.sort()
    return dist[0]



