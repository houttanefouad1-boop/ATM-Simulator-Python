################################### ATM Simulator #########################################
#__________________________________$$__neveu1__$$_________________________________________#
password = "0000"
username = "admin"
balance = 5000
password = input("password: ")
username = input("username: ").lower()

    
if password == "0000" and username == "admin":
    while True:
        ################# THE CHOSE ###############

        print("1: Account statement")
        print("2: Pull the amount")
        print("3: Deposit the amount")
        print("4: Exit")
        number = float(input("CHOSE: "))

        ##### chose 1 : #################
        #####################################3

        if number == 1:
            print(f"you the amount is : {balance} DH")
            #### if blance < 0 ###############
            if balance <= 0 :
                print(balance)
        ######### chose 2: ##############
        ################################################################

        elif number == 2 :
            print("how much want pull?")
            pull = float(input("Pull:"))
            if pull > balance : # if this number > balance : ############
                print("Your balance is not enough") #########################################
            else:
                balance -= pull 
            print(f"it has been withdrawn: {pull} DH")
            
        ###### chose 3 :    #################################

        elif number == 3 :
            deposit = float(input("Deposit: "))
            balance += deposit
            print(f"you add {deposit}")
        #### chose 4 : ####################################################    
        ###########################################444444444444444444444444444

        elif number == 4:
            exit()
        else:
            print("error pleas enter this choses")

##############################@@@@@@ PAWOERD OR USERNAME @@@@@#################### 
           
else: ##### if the password or username not correct
    print("password or usernam is not corecte")
             ############                                                                     ##############
                          ###########                                               ##########
                                    ###########                             ########
                                                #THIS IS MY FIRST PROJECT#
                                    ###########                             #######
                        ############                                                ##########
            ###########                                                                       ###############
            

