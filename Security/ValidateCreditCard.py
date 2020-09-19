from functools import reduce
def card_validate():
    '''
    Validates a card
    implemeted using Checksum Principle
    
    '''
    card_list=[]
    new=[]
    while True:
        num =input('please enter 16 digit card number:')
        num=num.replace(' ','')
        if len(num)!= 16:
            continue
        else:
            break
        
        
    for e in num:
        card_list.append(int(e))
            
    check_digit= card_list.pop()
    for i,j in enumerate(card_list):
        if i%2==0:
            m= j*2
            m=int(m/10)+(m%10)
            new.append(m)
        else:
            new.append(j)
            
    result= reduce(lambda x,y: x+y,new)
    if (result+check_digit)%10 == 0:
        return True
    else:
        return False



if __name__ == '__main__':
    Result = card_validate()
    print(Result)