
while True:

  print("Welcome to the Budget Calculator! ")

  income = int(input("What is your monthly income?"))

  rent = int(input("What is your monthly rent?"))

  credit_card = int(input("What is your monthly credit card payments?"))

  gas = int(input("How much do you spend on gas a month?"))

  internet = int(input("How much is your monthly internet?"))


  if income <= rent + credit_card + gas + internet:
    print("You are over budget")

  elif income > rent + credit_card + gas + internet:
    print("You are under budget")
  else:
    print("I need to try that again..")

  go_again = input("Do you want to try again?")

  if go_again == "no" or "No":
    print("See you later!")
    break
  else:
    print("Great!")
#def invalid_answer():



print(income, rent, credit_card, gas, internet)











  #def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
   # if (budget < food_bill + electricity_bill + internet_bill + rent):
    #  return True
    #else:
     # return False
  #print(over_budget(100, 20, 30, 10, 40))
  # should print False
  #print(over_budget(80, 20, 30, 10, 30))
  # should print True
  #if youre over budget prints true




  # Needs fixed
  #def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
   #   if (budget < food_bill + electricity_bill + internet_bill + rent):
     #     if over_budget == True:
       #       print("On Budget!")
      #return Truelse:
       #   return False



  #print(over_budget(100, 20, 30, 10, 40))