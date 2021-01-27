#take num resverse it and add is it ever going to be a palindrome
from matplotlib import pyplot as plt
def reverse(num):
    rev=0
    while(num>0):
        rev=rev*10+num%10
        num=int(num/10)
    return rev

def isPal(x):
    if reverse(x)==x :
        return 1
    else: return 0

def diff(l):
    retl=[]
    for i in range(1,10000):
        if(i not in l):
            retl.append(i)
    return retl  
lpal=[1,2,3,4]


for i in range(10,10000):
    t=i
    for j in range(100):
        if(isPal(t) and j>0):
            lpal.append(i)
            break
        else:
            t=t+reverse(t)
ldif=diff(lpal)
print(ldif)

for i in range(10,500):
    if i in ldif:
        plt.plot([i],[1],'ro')
plt.xlabel("Truth Values 1=> True")
plt.title("NOT PALINDROME IN 500")
plt.savefig("Pal500.png")
for i in range(10,1000):
    if i in ldif:
        plt.plot([i],[1],'ro')
        
plt.xlabel("Truth Values 1=> True")
plt.title("NOT PALINDROME IN 1000")
plt.savefig("Pal1000.png")
for i in range(10,10000):
    if i in ldif:
        plt.plot([i],[1],'ro')
plt.xlabel("Truth Values 1=> True")
plt.title("NOT PALINDROME IN 10000")
plt.savefig("Pal10000.png")