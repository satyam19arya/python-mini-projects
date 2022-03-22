secure=(('s','$'),('and','&'),('a','@'),('o','0'),('i','1'),('l','!'),('c','('),('v','^'))

def securePassword(password):
    for a,b in secure:
        password = password.replace(a,b)
    return password

if __name__=="__main__":
    password = input("Enter your password:\n")
    password = securePassword(password)
    print(f"Your secure Password is {password}")