x=int(input("Enter the number:"))
o=''
while x!=0:
    o=str(x%8)+o
    x=x//8
print(int(o))    
    
