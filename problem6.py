inStr = input("Enter a String: ")
inChar = input("Enter a Character: ")
s=set()
start=0

while True:
    i=inStr.find(inChar,start)
    if i!=-1:
        s.add(i)
    if start==len(inStr)-1: break
    else:
        start+=1


print(list(s))
