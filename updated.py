import sys
import time


from playsound import playsound
audio1 = r'C:\Users\GethinGrice(WHS-Year\Documents\audio_readout_help_python.mp3'
#playsound (audio1)

audio2 = r'C:\Users\GethinGrice(WHS-Year\Documents\closing_program_audio.mp3'


money_earnt = 0

logged_in = False
logged_in_username = False
log_in_username = False



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
    #return value outside of function
    global money_earnt
    print()
    print()
    print("===================================================")
    print("What food is the student purchasing?")
    print("===================================================")
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
         print()
         print("Exiting admin..")


    if purchasing.lower() == "chicken wrap":
        if (chicken_wrap["amount"]) > 0:
         chicken_wrap["amount"] = (chicken_wrap["amount"] -+ 1)
         money_earnt = money_earnt + chicken_wrap["price"]
         print()
         print("Chicken wrap purchased")
         print()
         print("Money earnt: {:.2f}".format(money_earnt))
         print()
         print("Exiting admin..")


    if purchasing.lower() == "pizza":
        if (pizza["amount"]) > 0:
         pizza["amount"] = (pizza["amount"] -+ 1)
         money_earnt = money_earnt + pizza["price"]
         print()
         print("Pizza purchased")
         print()
         print("Money earnt: {:.2f}".format(money_earnt))
         print()
         print("Exiting admin..")


    if purchasing.lower() == "pasta":
     if (pasta["amount"]) > 0:
         pasta["amount"] = (pasta["amount"] -+ 1)
         money_earnt = money_earnt + pasta["price"]
         print()
         print("Pasta purchased")
         print()
         print("Money earnt: {:.2f}".format(money_earnt))
         print()
         print("Exiting admin..")




    if purchasing.lower() == "admin":
        print()
        print("-------------------------------------------------------------")
        username_input = input("Enter USERNAME:   ")
        password_input = input("Enter PASSWORD:   ")
        if username_input.lower == ("gethin") and password_input == ("password123"):
            print()
            print("-------------------------------------------------------------")
            print("Hello Gethin. What do you want to do?")
            admin_prompt = str(input("Money earnt       Price       Amount       Food"))
            print("-------------------------------------------------------------")
        if username_input.lower != ("gethin") and password_input != ("password123"):
            print("-----------------------------------------------------------")
            print("Wrong username or password")
            print("-----------------------------------------------------------")
            print()
            quit()
        


            
                



            


            if admin_prompt.lower() == "money earnt":
                print()
                print ("Money earnt: {:.2f}".format(money_earnt))
                print()
                print("Exiting admin..")



            if admin_prompt.lower() == "price":
                print()
                price_prompt = str(input("Which food do want the price of?"))
                if price_prompt == "curry":
                    print()
                    print("-------------------------------------------------------------")
                    print("Curry price ---> " + str((curry["price"])))
                    print("-------------------------------------------------------------")
                    print()
                    print("Exiting admin..")

                        
                        
                if price_prompt == "chicken wrap":
                    print()
                    print("-------------------------------------------------------------")
                    print("Chicken wrap price ---> " + str((chicken_wrap["price"])))
                    print("-------------------------------------------------------------")
                    print()
                    print("Exiting admin..")
                        
                        
                if price_prompt == "pizza":
                    print()
                    print("-------------------------------------------------------------")
                    print("Pizza price ---> " + str((pizza["price"])))
                    print("-------------------------------------------------------------")
                    print()
                    print("Exiting admin..")

                        
                if price_prompt == "pasta":
                    print()
                    print("-------------------------------------------------------------")
                    print("Pasta price ---> " + str((pasta["price"])))
                    print("-------------------------------------------------------------")
                    print()
                    print("Exiting admin..")
                        


                
                if admin_prompt.lower() == "amount":
                    print()
                    amount_prompt = str(input("Which food do want to retrieve the amount of?"))
                    if amount_prompt == "curry":
                        print()
                        print("-------------------------------------------------------------")
                        print("Curry amount ---> " + str((curry["amount"])))
                        print("-------------------------------------------------------------")
                     
                if admin_prompt.lower() == "money earnt":
                    print()
                    print ("Money earnt: {:.2f}".format(money_earnt))
                    print()
                    print("Exiting admin..")



                if admin_prompt.lower() == "price":
                    print()
                    price_prompt = str(input("Which food do want the price of?"))
                    if price_prompt == "curry":
                        print()
                        print("-------------------------------------------------------------")
                        print("Curry price ---> " + str((curry["price"])))
                        print("-------------------------------------------------------------")
                        print()
                        print("Exiting admin..")

                        
                        
                    if price_prompt == "chicken wrap":
                        print()
                        print()
                        print("Exiting admin..")
                        
                        
                    if amount_prompt == "chicken wrap":
                        print()
                        print("-------------------------------------------------------------")
                        print("Chicken wrap amount ---> " + str((chicken_wrap["amount"])))
                        print("-------------------------------------------------------------")
                        print()
                        print("Exiting admin..")
            
                        
                        
                    if amount_prompt == "pizza":
                        print()
                        print("-------------------------------------------------------------")
                        print("Pizza amount ---> " + str((pizza["amount"])))
                        print("-------------------------------------------------------------")
                        print()
                        print("Exiting admin..")

                    
                    if amount_prompt == "pasta":
                        print()
                        print("-------------------------------------------------------------")
                        print("Pasta amount ---> " + str((pasta["amount"])))
                        print("-------------------------------------------------------------")
                        print()
                        print("Exiting admin..")
            


                if admin_prompt.lower() == "food":
                    print()
                    print("-----------------------------------------------------------")
                    print("Food -->      CURRY     CHICKEN WRAP     PASTA      PIZZA")
                    print("-----------------------------------------------------------")
                    print()
                    print("Exiting admin..")
                            



                #added so quit and exit works while in admin mode
                if admin_prompt.lower() == "quit" or admin_prompt.lower() == "exit":
                    print("\n")
                    print("Closing program.")

                    time.sleep(1)
            
                    for x in range(50):
                        print()
                    print()
                    print("Closing program..")

                    time.sleep(1)

                    for x in range(50):
                        print()
                    print()
                    print("Closing program...")

                    time.sleep(1)
                    quit()



    #quit and exit clears page and types closing animation then prompts sys.close
    if purchasing.lower() == "quit" or purchasing.lower() == "exit":
        print("\n")
        print("Closing program.")
        playsound (audio2)

        time.sleep(1)

        for x in range(50):
            print()
        print()
        print("Closing program..")

        
        playsound(audio2)
        time.sleep(1)

        for x in range(50):
            print()
        print()
        print("Closing program...")

        
        playsound (audio2)
        time.sleep(1)
        quit()

        



    if purchasing.lower() == "help" or purchasing.lower() == "tut" or purchasing.lower() == "tutorial":
        print("========================================================")
        print("User selects student purchase")
        print("Food purchased is printed + total money earnt")
        print()
        print('User can enter "admin" to go into admin mode')
        print('Can enter "money earnt", "price", "amount" and "food"')
        print()
        print('If user enters "price" or "amount", they get prompted to enter the food')
        print()
        print('If user enters "exit" or "close" in any input, the closing sequence is iniated')
        print("And the user is prompted to exit the program")
        print("========================================================")
        playsound (audio1)

         


        #==================need to do======================#
        #stop main purchasing from happening when in admin - done (left)
        #keyword to go back to purchasing? - don't need


                
        #add each variable price to print - done
                                   
       
                                 


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
