def calculate(t,c):
    if(c=='+'):
        return True if (t[0]+t[1]==t[2]) else False
    elif(c=='-'):
        return True if (t[0]-t[1]==t[2]) else False
    elif(c=='*'):
        return True if (t[0]*t[1]==t[2]) else False
    elif(c=='I'):
        if(t[0]+t[1]==t[2] or t[0]-t[1]==t[2] or t[0]*t[1]==t[2]):
            return False
        else:
            return True

while True:
    try:
        n=int(input())
        hisab=[]
        names=[]
        loses=[]
        temp=[]
        pr=''
        for x in range(n):
            a,b=input().split()
            b,c=b.split('=')
            temp.append(int(a))
            temp.append(int(b))
            temp.append(int(c))
            hisab.append(temp)
            temp=[]
        for x in range(n):
            a,b,c=input().split()
            names.append(a)
            b=int(b)
            #print(a, b, hisab[b-1], c, calculate(hisab[b-1],c))
            if(calculate(hisab[b-1],c)==False):
                loses.append(x)
        Nlose=[]
        for x in loses:
            Nlose.append(names[x])
        Nlose.sort()
        if(len(loses)==n):
            print('None Shall Pass!')
        elif(len(loses)==0):
            print('You Shall All Pass!')
        else:
            pr=''
            for x in range(len(Nlose)):
                pr+=(Nlose[x]+' ')
            print(pr[:-1])
            
    except EOFError:
        break
