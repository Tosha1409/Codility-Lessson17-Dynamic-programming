#finding all possible summs of elements. amount - amounts of elements
#and x is value of elements.
def get_sums(amount,x):
    a=[]
    for y in range (-amount, amount+1):
        if (amount%2==abs(y%2)): a.append(x*y)
    return (a)

def solution(A):
    #returning results if A have 0 or 1 elements, finding biggest value of array
    #and creatng array for counting repeated elements (m and -m counted as m)
    if len(A)==1: return (A[0])
    if len(A)==0: return (0)
    n=max(max(A),abs(min(A)))
    numbers=[0]*(n+1)
    
    #counting amount of repeats
    for x in A: 
        if x!=0: numbers[abs(x)] +=1

    #removing last elements that can be divided by 2 and reducing numbers of repeats
    #cause those are not really nessesary for calculation and only increase amount 
    #of calculations.
    for x in range(n,0,-1):
        #removing elemnts
        if (numbers[x]%2!=1) and (x==len(numbers)-1): numbers.pop()
        #decreasing amount of repeats
        elif numbers[x]>3:
             max_value=n//x
             if numbers[x]%2!=max_value%2: max_value +=1
             else: max_value +=2
             if numbers[x]>max_value: numbers[x]=max_value
    
    #returnng results if them are obvious after previous operations.
    n=len(numbers)-1
    if (sum(numbers)==0): return(0)
    if (sum(numbers)==1): return(len(numbers)-1)

    #counting all possible summs for current elements and removing duplicated values
    results=[]
    for x in range (1,n+1):
        if numbers[x]!=0: 
            sums = get_sums (numbers[x],x)
            #counting every next sum
            if results!=[]:
                tmp = []
                for n1 in results: 
                    for n2 in sums: tmp.append(n1+n2)
                results= list(set(tmp)) 
            #if it is first calculation then cutting half of it, 
            #because 2nd half is basicly inverted first part
            else:
                results= sums[:(len(sums))//2]
    
    #returning result
    return (abs(min(results, key=abs)))