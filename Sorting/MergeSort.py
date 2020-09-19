def merge(Arr):
    '''
    sorting a list using merging
    '''
    if len(Arr)> 1:
        # dividing a list into two halves
        mid = len(Arr)//2
        new_A = Arr[:mid]
        new_B = Arr[mid:]
        
        merge(new_A) # merging first half
        merge(new_B) # merging second half
        
        i=j=k=0 #initialize
        
        #performing sorting for each recursive loop
        while i< len(new_A) and j< len(new_B):
            if new_A[i] > new_B[j]:
                Arr[k] = new_B[j]
                j+=1
                
            else:
                Arr[k] = new_A[i]
                i+=1
                
            k+=1 
        
        # when two half lists are of different length
        # leftover elements are shifting back to list
        while i<len(new_A):
            Arr[k] = new_A[i]
            k+=1
            i+=1
            
        while j< len(new_B):
            Arr[k] = new_B[j]
            j+=1
            k+=1


if __name__ == '__main__':
    elements = input('Enter elements to sort with space:').split()
    elements=[int(i) for i in elements]

    merge(elements)
    print(elements)