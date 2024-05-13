#i added this while later to continuesly do calculations
while True:
  numb1 = int(input("Enter numb1 = "))
  numb2 = int(input("Enter numb2 = "))
  operator = input("Enter the operator (add, subtract, multiply, divide): ")

  def calculate(numb1, numb2, operator): #function taking three arguments which user will entered above now based on operatior it will do only that calculation
    if operator == "add":
      print(numb1 + numb2)
    elif operator == "subtract":
      print(numb1 - numb2)
    elif operator == "multiply":
      print(numb1 * numb2)
    elif operator == "divide":
      if numb2 == 0:
        print("Error: Division by zero")
      else:
        print(numb1 / numb2)
    else:
      print("Invalid Operator")

  calculate(numb1, numb2, operator)    #this tells program to solve as operations are already defined (basically a function call)
#this part is for to run program again simple while loop
  choice = input("Do you want to perform another calculation? (y/n): ").lower()
  if choice not in ("y", "yes"):
    break
#this will be printed user leaves
print("good by")