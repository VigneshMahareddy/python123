#Write a program to find whether an inputted number is perfect or not.
n=int(input("ENTER ANY NUMBER : "))
s=0
for i in range (1,n):
    if(n % i==0):
        s=s+i
if (s==n):
    print(n,"IS A PERFECT NUMBER.")
else:
    print(n,"IS NOT A  PERTECT NUMBER.")
