"""
a simple loan calculator that computes interest over time given an APR,
monthly payment, and duration.
"""
def demo():
    """A simple loan calculator that computes interest."""
    # input
    # money_owed = float(input("How much money do you owe? "))
    # apr = float(input("What is the annual percentage rate (APR) in %? "))
    # payment = float(input("What is your monthly payment? "))
    # months = int(input("How many months do you want to calculate for? "))

    money_owed = 20000
    apr = float(4)
    payment = float(500)
    months = int(48)
    total_interest_paid = 0
    total_paid = 0

    # calculations
    monthly_apr = apr/100/12
    print("Annual APR: ", apr)
    print("Monthly APR: ", monthly_apr)

    print("--------------------------------------------------")
    print("----------- Month Breakdown ----------------------")
    print("--------------------------------------------------")


    for i in range(months):
        print("Month: ", i + 1)

        interest_paid = money_owed * monthly_apr
        print("     Interest paid this month: ", interest_paid)

        total_interest_paid += interest_paid
        total_paid += payment

        if (money_owed - payment < 0):
            print("The last payment is $", money_owed, sep="")
            print("You have paid off the loan in ", i + 1, " months.", sep="")
            print("----------------------------------------------")
            break

        # add in interest
        money_owed = money_owed + interest_paid

        # make payment
        money_owed = money_owed - payment
        print("     Money owed after payment: ", money_owed)
        print("Paid $", payment, " of which $", interest_paid, " was interest.", sep="", end=" ")
        print("You still owe $", money_owed, ".", sep="")
        print("----------------------------------------------")

    print("Total interest paid: $", total_interest_paid, sep="")
    print("Total paid: $", total_paid, sep="")
    print("")
    print("")
    print("")