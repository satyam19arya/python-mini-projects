sum=0
while True:
  try:
    userInput=input("Enter the item price or press quit to exit: ")
    if userInput!='quit':
        sum=sum+int(userInput)
        print(f"Your current bill is {sum}")
    else:
        print(f"Your total bill is {sum}. Thanks for shopping with us:)")
        break

  except Exception as e:
      print(f"Your input is an error {e}")