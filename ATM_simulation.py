name = input("please enter your name:-")
print(f"hello {name} !")

print("how may i help you.","\n")         

message = """Please select any of them option,
Type 1 >>>>>> CHECK BALANCE,
Type 2 >>>>>> DEPOSIT,
Type 3 >>>>>> WITHDRAWL."""
print(message,"\n")
task=  int(input("enter your option:-"))

available_amount= 5000

if (task >= 1) & (task<=3):
    if task ==1:
        #task 1 program for check balance
        balance_message =  f"THANKS FOR VISITING ! YOUR AVAILABLE BALANCE IS:- INR{available_amount}"
        print(balance_message)

    elif task==2:
        # task 2 program for deposit
        deposit_amount = int(input("enetr your deposit amont:-"))
        if deposit_amount>0:
            available_amount += deposit_amount
            deposit_message = f"you have successfully deposited your money {deposit_amount}"
            balance_message = f"THANKS FOR VISITING ! YOUR AVAILABLE BALANCE IS:- INR{available_amount}"

            print(deposit_message)
            print('\n')
            print(balance_message)
        
        else:
            print("please enter a valid amount ")

    else:
        #task 3  program withdrawl amount
        withdrawl_amount = int(input("enter amount:-"))
        if withdrawl_amount<=available_amount:
  #withdrawl process starts
            if withdrawl_amount >0:
                available_amount -= withdrawl_amount
                withdrawl_amount_message = f"you have successfully withdrawl amount {withdrawl_amount}"
                balance_message = f"THANKS FOR VISITING ! YOUR AVAILABLE BALANCE IS:- INR{available_amount}"
                print(withdrawl_amount_message)
                print(balance_message)
            else:
                print(f"please enter a valid number")
        else:
            withdrawl_message_warning = "you have insufficient balance"
            balance_message = f"THANKS FOR VISITING ! YOUR AVAILABLE BALANCE IS:- INR{available_amount}"
            print(withdrawl_message_warning)
            print(balance_message)
else:
    print("please type correct input!😁")

