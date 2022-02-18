# week 2 Advanced Coding Challenge

# 1. Hailstone

def hailstone(n):
    """
    Your Code Here
    """
    steps=1
    ns=[n]
    while n > 1:
        if n%2:
            n=n*3+1
            ns.append(int(n))
        else:
            n=n/2
            ns.append(int(n))
        steps+=1
    ns.append(steps)
    return ns

def main():
    n = int(input())
    a = hailstone(n)
    for i in a:
        print(i)

main()

# 2. Largest Factor

def largest_factor(n):
    """
    Return the largest factor of n that is smaller than n.
    Your code here.
    """
    fs=[]
    for f in range(1,n):
        if n%f==0:
            fs.append(f)  
    return fs

def main():
    n = int(input())
    print(largest_factor(n))

main()

# week 3 Advanced Coding Challenge

# 1. Digital Currency

def cal_price(prices):
    """
    Your Code Here
    """
    c = 0
    h = False
    for i,p in enumerate(prices):
        if h==True and i<=len(prices)-2:
            if prices[i]<prices[i+1]:
                continue
            elif prices[i]>=prices[i+1]:
                c+=p
                h=False
        elif h==True and i==len(prices)-1:
            c+=p
            h=False
        elif h==False and i!=len(prices)-1:
            c-=p
            h=True
            if prices[i]>=prices[i+1]:
                c+=p
                h=False
    return c

# def cal_price(prices):
    # def cal_price(prices):
    # num_prev=0
    # profit=0
    # the_first_time=True
    # for i in prices:
    #     if not the_first_time:
    #         if num_prev<i:
    #             profit+=i-num_prev
    #     num_prev=i
    #     the_first_time=False
    # return profit   

def main():

    prices = input().split()
    prices = list(map(int, prices))
    print(cal_price(prices))

main()

# 2. Roman Numerals.

def roman_translate(num):

    """
    Your Code Here
    """
    s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    v = 0
    for i,n in enumerate(num):
        if s[num[i-1]]<s[n] and i>0:
            v += (s[n]-2*s[num[i-1]])
        else:
            v += s[n]
    return v

    # sum = s[num[len(num)-1]]
    # for i in range(len(num)-1,0,-1):
    #     if(s[num[i]]<=s[num[i-1]]):
    #         sum += s[num[i-1]]
    #     else:
    #         sum -= s[num[i-1]]
    # return sum

def main():

    num = input()
    print(roman_translate(num))

main()

# week 4 Advanced Coding Challenge

# 1. Permutation

"""
You may define your own functions
"""
import itertools
import math
 
def perm(nums):
    if len(nums)<=1:
        return [nums]
    output=[]
    for i in range(len(nums)):
        first = nums[i] # take one element
        rest = nums[:i] + nums[i+1:] # rest  of the list
        for p in perm(rest):
            output.append([first]+p) # append list ot output (another list)
    return output

def main():

    nums = input().split()
    """
    Your Code Here
    """
    output = perm(nums)
    # output.sort()
    for l in output: print(l)
    # print(output)

    # p=itertools.permutations(nums)
    # for i in p:
    #     print(list(i))

    # n=tuple(nums)
    # l=len(n)
    # ind=list(range(l))
    # c=list(range(l, 0, -1))

    # print(list(n[i] for i in ind[:l]))

    # for t in range(math.prod(range(1,l+1))):
        
    #     for i in reversed(range(l)):

    #         c[i] -= 1
    #         if c[i] == 0:
    #             print(ind[i:],ind[i+1:],ind[i:i+1])
    #             ind[i:] = ind[i+1:] + ind[i:i+1]
    #             c[i] = l - i

    #         else:
    #             j = c[i]
    #             ind[i], ind[-j] = ind[-j], ind[i]
    #             print(list(n[i] for i in ind[:l]))
    #             break
main()

# week 5 Advanced Coding Challenge

# 1. Tic-tac-toe

"""
Your Code Here
No Scaffold Provided
"""

b=['| 1 || 2 || 3 |','| 4 || 5 || 6 |','| 7 || 8 || 9 |']

t=1
i1,i2=[0,1,2],[2,7,12]
d={1:(0,2),2:(0,7),3:(0,12),4:(1,2),5:(1,7),6:(1,12),7:(2,2),8:(2,7),9:(2,12)}
w=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
w1=list(w).copy()
# print(w1)
def p(n):
    n=int(n)
    a=d[n][0]
    b=d[n][1]
    return a, b
def s(n):
    n=int(n)
    return b[p(n)[0]][p(n)[1]]

play=1
while play:    
    
    if t: 
        b=list(map(''.join,b))
        print('\n'.join(b))
        x=input('X: ')
        b=list(map(list,b))
        # print(c)
        if x.isnumeric()==True and int(x)>0 and int(x)<10:
            if (int(x)>0 and int(x)<10) and b[p(x)[0]][p(x)[1]]=='X' or b[d[int(x)][0]][d[int(x)][1]]=='O':
                print('Error: N/A position')
                continue
            elif int(x)>0 and int(x)<10:
                x=int(x)
                b[d[x][0]][d[x][1]]='X'
            else:pass
        elif x==' ':
            print('Error: invalid input')
            continue
        else:
            print('Error: invalid input')
            continue

        b=list(map(''.join,b))
        # print(b)
        t-=1

    elif not t: 
        b=list(map(''.join,b))
        print('\n'.join(b))
        o=input('O: ')
        b=list(map(list,b))
        # print(c)
        # print(b[d[o][0]][d[o][1]])
        # print(b[d[o][0]][d[o][1]])
       
        if o.isnumeric()==True and (int(o)>0 and int(o)<10):
            # print(b)
            
            if b[p(o)[0]][p(o)[1]]=='X' or b[p(o)[0]][p(o)[1]]=='O':
                print('Error: N/A position')
                continue
            elif int(o)>0 and int(o)<10:
                o=int(o)
                b[d[int(o)][0]][d[int(o)][1]]='O'
            else:pass
        elif x==' ':
            print('Error: invalid input')
            continue
        else:
            print('Error: invalid input')
            continue

        b=list(map(''.join,b))
        t+=1

    for i,n in enumerate(w):
        w1[i]=list(map(lambda x: s(x),n))
        if list(map(lambda x: s(x),n))==['X','X','X']:
            print('\n'.join(b))
            print('Player X wins')
            play=0
        elif list(map(lambda x: s(x),n))==['O','O','O']:
            print('\n'.join(b))
            print('Player O wins') 
            play=0
        else:pass

    if play != 0 and all(j.isalpha() for i in w1 for j in i):
        print('\n'.join(b))
        print('Tie')
        play=0
    # print(w1)

# week 6 Advanced Coding Challenge

# 1. Simple Web Crawling

from bs4 import BeautifulSoup

'''
You Code Here
'''
# from bs4 import BeautifulSoup as bs

#with open('AcademicStaff.html') as f:
    #for line in f:
        #print(line)
# h=open('AcademicStaff.html')
#print(type(h))

with open('AcademicStaff.html') as fp:
    soup = BeautifulSoup(fp,'html.parser')

# s = BeautifulSoup(open('AcademicStaff.html'), 'html.parser')
# ns=s.select("strong")
# for n in ns[:-2]:
#     print(n.string)

rows = soup.select('tbody tr strong')
for i in rows:
    print(i.string)

# 2. Card Deck

import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# random.shuffle(deck)
# print(deck[:50])

l = random.choices(deck,k=50)
print(l)

# week 7 Advanced Coding Challenge

# 1. Supermarket (Optional)

def readData(products):
    command=input().split()
    while (command[0]!="END"):
        products[int(command[0])]=[command[1],float(command[2])]
        command=input().split()

def showMenu(products):
    print("-Menu-")
    for k in products:
        v=products[k]
        print(k, ':', v[0], '$', v[1])
    print("------")


def purchase(products):
    showMenu(products)

    product_code = int(input("Product code:"))
    quantity = int(input("Quantity:"))

    product_data=products[product_code][1]
    price=product_data*quantity

    print("Added $", price)
    return price

def checkout(total):
    print('Purchase $', total)
    print('Tax $', total * 0.05)
    print('Total $', total * 1.05)
    print("Thank you!")
    return

def main():
    products={}
    readData(products)
    
    print("****************************************")
    print("*  Welcome to ENGG1330's supermarket!  *")
    print("****************************************")
    
    choice = 0
    total = 0
    while( choice != 3 ):
        print("------------------------")
        print("\t 1: Purchase. ")
        print("\t 2: Checkout. ")
        print("\t 3: Exit. ")
        print("------------------------")
           
        choice=int(input("Please select:"))

        if ( choice == 1 ):
            total += purchase(products)
            print("Current amount $",total)
        elif( choice == 2 ):
            checkout(total)
            break
        elif ( choice == 3 ):
            return

main()

# 2. Phonebook

def addNumbers(phonebook, name, phones):
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].extend(phones)

def showNumber(phonebook,name):
    if name in phonebook: 
        phonebook[name].sort()
        # for i in range(len(phonebook[name])//2):
        #     phonebook[name][i],phonebook[name][len(phonebook[name]) - 1 -i] = phonebook[name][len(phonebook[name]) - 1 -i], phone
        print(phonebook[name][::-1])
    else:
        print(name,'not found')


def findNumber(phonebook,number):
    for name in phonebook:
        if number in phonebook[name]:
            print(name)
            return
    print(number, 'not found')

def main(): 
    phonebook = {} 
    command = input().split() 
    while (command[0] != 'END'): 
        #More to be added here
        def addNumbers(phonebook, name, phones):
            if name not in phonebook:
                phonebook[name] = []
                phonebook[name].extend(phones)
            else: phonebook[name].extend(phones)
            # return phonebook

        def showN(phonebook,name):
            if name in phonebook: o=phonebook[name]
            else: o=f'{name} not found'
            return print(o) 

        def findN(phonebook,phones):
            nl=list(phonebook.values())
            
            if [phones] in nl: o=phonebook[name]
            else: o=f'{name} not found'
            return print(o) 

        if command[0] == 'ADD':
            addNumbers(phonebook, command[1], command[2:])
        # if command[0] == 'SHOW':
        #     showN(command[1])
        elif command[0]=='SHOW':
            showNumber(phonebook,command[1])

        elif command[0]=='FIND':
            findNumber(phonebook,command[1])

        # print(phonebook)
        # showN()
        
        command = input().split() 

main()

# week 8 Advanced Coding Challenge

# 1. Wise Choice

def dominate(hotels,A,B):
    for i in range(len(hotels[A])):
        if (hotels[A][i] > hotels[B][i]):
            return False
    for i in range(len(hotels[A])):
        if (hotels[A][i] < hotels[B][i]):
            return True
        # else: 
    return False

def wiseChoice(hotels):
    #To be implemented by you
    result=[]
    for i in hotels:
        d=False
        for j in hotels: 
            # Do something here to check if j dominates i
            if(i!=j and dominate(hotels,j,i)):
                d=True
                break
        if  not d:
            result.append(i)

    return result

def readInput(hotels):
    #To be implemented by you  
    command=input().split()
    while ( command[0]!="END" ):
        name = command[0] 
        hotels[name]=[] 
        for i in command[1:]:
            hotels[name].append(float(i))            
        command=input().split()
        
    return hotels

def main():
    hotels={}
    readInput(hotels)
    print(wiseChoice(hotels))
main()

# week 9 Advanced Coding Challenge

# 1. Fibonacci number
def fib(n):
    if n == 0 or n == 1:
        return n
        
    fn = fib(n-1) + fib(n-2)
    return fn

print(fib(int(input())))

# 2. Fibonacci number illustration
def fib(n):
    print(f'calculate f {n}')
    if n == 0 or n == 1:
        print(f'return {n}')
        return n

    print(f'f {n} = f {n-1} + f {n-2}')
    fn = fib(n-1) + fib(n-2)
   
    print(f'f {n} = {fn}')
    print(f'return {fn}')
    return fn


print(fib(int(input())))
# fib()

# 3. Factorial
def f(i):
    if i==1 or i==0:return 1
    return i*f(i-1)
print(f(int(input())))

# 4. Ackermann function
def a(m,n):
    if m==0:return n+1
    elif m>0 and n==0:return a(m-1,1)
    return a(m-1,a(m,n-1))

m=int(input())
n=int(input())
print(a(m,n))

# 5. Combinations
n=int(input())
k=int(input())
def c(n,k):
    if k==0 or n==k:
        print(f'{n}C{k} = 1')
        return 1
    else:
        print(f'{n}C{k} = {n-1}C{k-1} + {n-1}C{k}')
        ans=c(n-1,k-1) + c(n-1,k)
        print(f'{n}C{k} = {ans}')
        return ans

c(n,k)

# week 10 Advanced Coding Challenge

# 1. Safety map
def check1(i,j):
    for r in range(-1,2):
        for c in range(-1,2):
            if (i + r) >= 0 and (i+r) <= len(map) - 1 and (j + c) >= 0 and (j+c) <= len(map) - 1:
                if map[i+r][c+j] == 1:
                    return False
    return True
def check2(i,j):
    for r in range(-2,3):
        for c in range(-2,3):
            if (i + r) >= 0 and (i+r) <= len(map) - 1 and (j + c) >= 0 and (j+c) <= len(map) - 1:
                if map[i+r][c+j] == 1:
                    return False
    return True

def main():
    global map
    map = []
    s = input()
    map.append(list(s))

    for i in range(len(s) - 1):
        map.append(list(input()))
    for i in range(len(map)):
        for j in range(len(map)):
            map[i][j] = int(map[i][j])

    smap = [[-1 for i in range(len(map))] for j in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 1:
                smap[i][j] = '#'
            else:
                if check2(i,j):
                    smap[i][j] = 2
                elif check1(i,j):
                    smap[i][j] = 1
                else:
                    smap[i][j] = 0
    for i in range(len(smap)):
        for j in range(len(smap)):
            print(smap[i][j], end = '')
        print()
main()
