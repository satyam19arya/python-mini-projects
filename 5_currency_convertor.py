with open('currency_data.txt') as f:
    lines=f.readlines()

try:
 currencyDict={}
 for line in lines:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]



 amount=int(input("Enter the amount: \n"))
 print("Enter the name of the currenct you want to convert this amount? Available Options: \n")
 [print(item) for item in currencyDict.keys()]
 currency=input("Please Enter one of these values: \n")
 print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")

except Exception as e:
    print("Error! Please check the input")