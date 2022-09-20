x=int(input("Enter the number:"))
b=''
while x!=0:
    b=str(x%2)+b
    x=x//2
print(int(b))    
