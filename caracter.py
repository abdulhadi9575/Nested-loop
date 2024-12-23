a=str(input("enter a word"))
b=str(input("enter a caracter"))
i=0
count=0
while(i < len(a)) :
    if a[i]==0 :
        count=count+1
    i=i+1
print(count)
