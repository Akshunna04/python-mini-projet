a=input("Enter starting date in format dd/mm/yyyy: ") 
b=input("Enter ending date in format dd/mm/yyyy: ")
x=a[6:10]
y=b[6:10]
x=int(x)
y=int(y)
ly=[]
nly=[]
for i in range(x,y+1):
    if(i%400==0 and i%100==0):
        ly.append(i)
    elif(i%4==0 and i%100!=0):
        ly.append(i)
    else:
        nly.append(i)
print("Leap Years are: ",ly)
print("Non leap years are: ",nly) 
