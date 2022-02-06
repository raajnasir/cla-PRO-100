class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_Balance(self):
        print("Your Balnce is 50,000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount" +str(amount) +"Your remaining balance is "+str(new_amount))        


def main():
    Card_number = input("Insert your card number :-")
    pin_number = input("Enter your pin number :-")

    new_user = Atm(Card_number, pin_number)

    print("Choose your activity ")
    print("1. balance Enquriy  2.withdrawl")
    activity = int(input("Enter activity number:-"))

    if(activity == 1):
        new_user.check_Balance()

    elif(activity == 2):
        amount = int(input("Enter the Amount to be withdrawed"))
        new_user.withdrawl(amount)

    else:
        print("enter a valid number")


main()        
