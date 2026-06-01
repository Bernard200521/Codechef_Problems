!Pallindrome(string), Factorial, Largest no., Armstrong No., Anagram, Maximum no., Length(abs), Pallindrome(Number), Celsius to Fahrenheit, Fahrenheit to celsius, Fibonicci Series, Swap no., Average

n=input()
s=n[::-1]
if(s==n):
  print("Pallindrome")
else:
  print("Not Pallindrome")

n=int(input())
fact=1
i=1
for i in range(1,n+1):
  fact = fact * i
print(fact)

a=int(input())
b=int(input())
c=int(input())
if (a>b and a>c):
  print("Largest:",a)
elif (b>a and b>c):
  print("Largest:",b)
else:
  print("Largest:",c)

n=int(input())
digits = len(str(n))
sum=0
temp=n
while temp > 0:
  rem = temp % 10
  sum += rem**digits
  temp //= 10
if (sum == n):
  print("Armstrong")
else:
  print("Not armstrong")

a = input()
b = input()
if(sorted(a) == sorted(b)):
  print("Anagram")
else:
  print("Not Anagram")

a=int(input())
b=int(input())
c=int(input())
print(max(a,b,c))

n = int(input())
out = len(str(abs(n)))
print(out)

for num in range(2, 51):
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)

n = int(input())
temp = n
rev = 0
while temp > 0:
  rem = temp%10
  rev = rev*10 + rem
  temp //= 10
if(rev == n):
  print("Pallindrome")
else:
  print("Not Pallindrome")

F = float(input())
C = (F-32)*5/9
print(C)

C = float(input())
F = (C*9/5)+32
print(F)

a = int(input())
b = int(input())
a,b = b,a
print(a,b)

n = int(input())
a = 0
b = 1
while n>0:
  c=a+b
  a=b
  b=c
  n-=1
  print(c)

a = int(input())
b = int(input())
c = int(input())
print((a+b+c)/3)

from functools import reduce
a=[1,2,3,4]
l=len(a)
s=reduce(lambda x,y:x+y,a)
print(s/l)

n = int(input())
for i in range(n):
  for j in range(i+1):
    print("*", end=' ')
  print()

n = int(input())
for i in range(n):
  for j in range(n-i):
    print("*", end=' ')
  print()

n = input()
l = ['a','e','i','o','u']
count = 0
for ch in n:
  if ch.upper() in l or ch.lower() in l:
    count += 1
    print(ch)
print("Vowels : ",count)

a = int(input())
b = int(input())

x=a
y=b

while y!=0 :
  x,y = y,x%y
gcd = x

lcm = (a*b)//gcd
print("GCD : ",gcd)
print("LCM : ",lcm)

l = [3,17,29,7,65,92]
print("largest : ",max(l))
print("Smallest : ",min(l))

a = int(input())
b = int(input())
choice = input()
if choice == '+':
  print(a+b)
elif choice == '-':
  print(a-b)
elif choice == '*':
  print(a*b)
elif choice == '/':
  print(a/b)
else:
  print("invalid")



n = int(input())
if n>0 :
  print("Positive")
elif n<0 :
  print("Negative")
elif n==0 :
  print("Zero")

n = int(input())
if (n%400 == 0 or (n%4 == 0 and n%100 != 0)):
  print("Leap year")
else:
  print("Not a leap year")

n = int(input())
if n%2 == 0:
  print("Even")
else:
  print("Odd")

n = int(input())
for i in range(n):
  for j in range(i+1):
    print(j+1, end=' ')
  print()

n = int(input())
for i in range(n):
  for s in range(i):
    print(" ",end=' ')
  for j in range(n-i):
    print("*", end=' ')
  print()

n = 3
for i in range(1,n+1):
  print(" "*(n-i) + "* "*i)
for i in range(n-1,0,-1):
  print(" "*(n-i) + "* "*i)

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")

    print()

n = [80,70,90,20,50]
n.sort(reverse=True)
print("Largest : ",n[:3])

a = "listen"
b = "silent"

if len(a) != len(b):
    print("Not Anagram")
else:
    count = 0

    for i in a:
        for j in b:
            if i == j:
                count += 1
                break

    if count == len(a):
        print("Anagram")
    else:
        print("Not Anagram")

a=int(input())
b=int(input())
if (pow(2,a) == b):
  print("Power of 2")
else:
  print("Not Power of 2")

a = input()
b = input()
if(a==b , b==a):
  print("Anagram")
else:
  print("Not Anagram")

s = input()
rev = s[3:13:1]
print(rev)

s1 = input()
s2 = input()

count = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        count += 1
if count == 1:
    print("Yes")

s = input()
l = ['a','e','i''o','u']
v_list = []
r = 0
for i in s:
  if i in l:
    v_list.append()

s = input()
curr = " "
for i in range(len(s)):
  curr = " "
  for j in range(i,len(s)):
    if s[j] not in curr:
      curr += s[j]
    else:
      break
print(len(curr))

n = int(input())
x = list(map(int,input().split()))
for i in range(1,n+1):
  d = x[i]
  if x[i] == 0:
    d = x[i-1] + 1
    print(d)
    break

class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def display(self):
    print("Name:",self.name)
    print("Age:",self.age)
obj = Student("HEMS",3)
obj.display()

class Father:
  def bike(self):
    print("Father has bike")
class Son(Father):
  def cycle(self):
    print("Son has cycle")
obj = Son()
obj.bike()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())5
rev = int(str(n)[::-1])
if is_prime(n) and is_prime(rev):
    print("Both are prime")
else:
    print("Not a prime")

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print(-i, end=" ")
    else:
        print(i, end=" ")

n = int(input())

sq = n * n

rev = int(str(n)[::-1])

rev_sq = rev * rev

if str(sq)[::-1] == str(rev_sq):
    print("Adam Number")
else:
    print("Not Adam Number")

n = input()

if '0' in n and n[0] != '0':
    print("Duck Number")
else:
    print("Not Duck Number")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = input()
flag = True

for i in range(len(n)):
    rotation = n[i:] + n[:i]
    if not is_prime(int(rotation)):
        flag = False
        break
if flag:
    print("Circular Prime")
else:
    print("Not Circular Prime")
