s = input()
myList = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in myList:
    s = s.replace(i,'*')
print(len(s))