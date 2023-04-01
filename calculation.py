import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
import art

print(art.logo)
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  if n2 == 0:
    return "Invalid input! Nothing can divided by 0"
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculation():
  num1 = float(input("What's the first number?: "))
  
  for key in operations:
    print(key)
  
  while True:
    operation_key = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
  
    if (operation_key != "+" and operation_key != "-") and (operation_key != "*" and operation_key != "/"):
      print("Invalid input!")
      continue
    elif operation_key == "/" and num2 == 0:
      print("Invalid input!")
      continue
    else:
      calculation_function = operations[operation_key]
      answer = calculation_function(num1,num2)
      print(f"{num1} {operation_key} {num2} = {answer}")
      flag = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ").lower()
      if flag != "y" and flag != "n":
        print("Invalid input!")
        break
      elif flag == "n":
        clear()  
        calculation()
    num1 = answer
calculation()