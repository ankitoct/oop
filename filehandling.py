f=open("data.txt",'r')
print(f.readline(),end='')
print(f.readline(),end='')
x=f.read()
print(x)
f1=open("abc.txt",'w')
f1.write(x)
f1.close()
f2=open("T.jpg",'rb')
photo=f2.read()
f3=open("A.jpg",'wb')
f3.write(photo)
f3.close()