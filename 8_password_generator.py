import string
import random

if __name__=='__main__':
    s1=string.ascii_lowercase
    print(s1)
    s2=string.ascii_uppercase
    print(s2)
    s3=string.digits
    print(s3)
    s4=string.punctuation
    print(s4)
    
    print("\n")
    plent = int(input("Enter password length: \n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)

    random.shuffle(s)
    #print(s)
    print("".join(s[0:plent]))
    

'''
    a=[1,2,3,4,5,6]
    b=[5,7]
    a.append(b)
    [1,2,3,4,5,6,[5,7]]


    a=[1,2,3,4,5,6]
    b=[5,7]
    a.extend(b)
    [1,2,3,4,5,6,5,7]


    s1='abcdefghijklmnop'
    list(s1)
    ['a','b','c','d','e','f','g','h','i']

'''