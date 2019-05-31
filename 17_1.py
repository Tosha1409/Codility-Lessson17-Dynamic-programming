def solution(A):
    turns=6
    l=len(A)
    if (min(A)<9): abs_min=min(A)*(l)
    else: abs_min=-1
    A2=([A[0]]*(turns+1))+([abs_min]*(l-1)) 
    for x in range(turns+1, l+turns):
        m=abs_min
        for y in range (1, turns+1):  m=max(m, A2[x-y])
        A2[x] = A[x-turns]+m        
    return (A2[-1])