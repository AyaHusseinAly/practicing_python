vowels=['a','e','o','i','u','A','E','O','I','U']

inStr = input("Enter your string: ")
outStr=inStr

for elem in inStr:
    if elem in vowels:
        outStr=outStr.replace(elem,'')


print(outStr)
