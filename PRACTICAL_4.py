#Write a Program to find factorial of the entered number.
a=int(input("ENTER NUMBER :"))
s=1
i=1
while i < a+1 :
    s=s*i
    i+=1
    if i == a+1:
        break
print("THE FACTORIAL OF THE ENTERED NUMBER IS : ", s)
