def bubble_sort(container):
    '''
    sorting elements using bubble sort
    '''
    for j in range(len(container)-1):
        for i in range(len(container)-1):
            if container[i] > container[i+1]:
                
                swap= container[i+1]
                container[i+1]= container[i]
                container[i]= swap



if __name__ == '__main__':
    elements = input('Enter elements to sort with space:').split()
    elements=[int(i) for i in elements]

    bubble_sort(elements)
    print(elements)