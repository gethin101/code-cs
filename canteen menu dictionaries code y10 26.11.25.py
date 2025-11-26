
money_earnt = 0


curry = {
  "food" : "curry",
  "price" : 2.40,
  "amount" : 100
}


chicken_wrap = {
  "food" : "chicken_wrap",
  "price" : 2.20,
  "amount" : 50
}


pizza = {
  "food" : "pizza",
  "price" : 2.60,
  "amount" : 110
}


pasta = {
  "food" : "pasta",
  "price" : 2.00,
  "amount" : 67
}


daily_menu = {
  "curry" : curry,
  "chicken_wrap" : chicken_wrap,
  "pizza" : pizza,
  "pasta" : pasta
}


#gets amount from curry nested in daily menu
#print (daily_menu["curry"]["amount"])



def buying():
    global money_earnt
    print()
    print()
    print("===================================================")
    print("What food is the student purchasing?")
    purchasing = str(input("Curry     Chicken Wrap     Pizza     Pasta    "))
    print("===================================================")
    print()


    if purchasing.lower() == "curry":
        if (curry["amount"]) > 0:
         curry["amount"] = (curry["amount"] -+ 1)
         money_earnt = money_earnt + curry["price"]
         print()
         print("Curry purchased")
         print()
         print("Money earnt: {:.2f}".format(money_earnt))


    if purchasing.lower() == "chicken wrap":
        if (chicken_wrap["amount"]) > 0:
         chicken_wrap["amount"] = (chicken_wrap["amount"] -+ 1)
         money_earnt = money_earnt + chicken_wrap["price"]
         print()
         print("Chicken wrap purchased")
         print()
         print("Money earnt: {:.2f}".format(money_earnt))


    if purchasing.lower() == "pizza":
        if (pizza["amount"]) > 0:
         pizza["amount"] = (pizza["amount"] -+ 1)
         money_earnt = money_earnt + pizza["price"]
         print()
         print("Pizza purchased")
         print()
         print("Money earnt: {:.2f}".format(money_earnt))


    if purchasing.lower() == "pasta":
     if (pasta["amount"]) > 0:
         pasta["amount"] = (pasta["amount"] -+ 1)
         money_earnt = money_earnt + pasta["price"]
         print()
         print("Pasta purchased")
         print()
         print("Money earnt: {:.2f}".format(money_earnt))




    if purchasing.lower() == "admin":
        print()
        print("-------------------------------------------------------------")
        print("Admin. What do you want to do?")
        admin_prompt = str(input("Money earnt       Price       Amount       Food"))
        print("-------------------------------------------------------------")

        if admin_prompt.lower() == "money earnt":
            print()
            print("Money earnt --> " + str(money_earnt))

        if admin_prompt.lower() == "price":
            print()
            price_prompt = str(input("Which food do want the price of?"))
            if price_prompt == "curry":
                print("Curry price ---> " + (curry["price"]))
            if price_prompt == "chicken wrap":
                print("Chicken wrap price ---> " + (chicken_wrap["price"]))
            if price_prompt == "pizza":
                print("Pizza price ---> " + (pizza["price"]))
            if price_prompt == "pasta":
                print("Pasta price ---> " + (pasta["price"]))


        #stop main purchasing from happening when in admin
        #keyword to go back to purchasing?
        #add each variable price to print
                                   
       
                                 


while True:
        buying()
    






#The school canteen wants a simple, digital system to manage their daily menu and track how many servings of each meal are left.

#The system needs to:

#Store the daily menu, including the Meal Name, Price, and Initial Stock (number of servings available).

#Display the menu to the canteen staff.

#Allow staff to select a meal when a student buys it.

#Update the stock by reducing the count for the purchased meal.

#Stop sales for any meal whose stock reaches zero.

#Calculate the total earnings for the day based on the total meals sold.

#Run continuously until the canteen staff decide to close the system for the day.
