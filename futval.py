#futval.py
#A program to compute the value of an investiment
#carried 10 years into the future

def main():
    print("This program calculates the future value of a 10-year investiment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual intrest rate: "))

    for i in range(10):
        principal = principal * (1 + apr )

    print("The valaue in 10 years is: ", principal)

main()
    
