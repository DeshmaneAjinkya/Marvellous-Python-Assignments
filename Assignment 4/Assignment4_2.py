Mult = lambda No1, No2 : (No1 * No2)

def main():
    No1 = 0
    No2 = 0
    Ret = 0

    No1 = int(input("Enter Number 1: "))

    No2 = int(input("Enter Number 2: "))

    Ret = Mult(No1, No2)

    print("Multiplication of ",No1," and ",No2," is ",Ret)

if __name__ == "__main__":
    main()