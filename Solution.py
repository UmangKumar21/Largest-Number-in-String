def em(s):
    N,R=0,0
    for i in range(len(s)):
        if s[i]>="0" and s[i]<="9":
            N=N*10 + int(int(s[i])-0)
        else:
            R=max(R,N)
            N=0
    return max(R,N)
s = (input())
print(em(s))
