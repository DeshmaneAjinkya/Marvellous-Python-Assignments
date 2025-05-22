Sum = lambda iNo1, iNo2 : (iNo1 + iNo2)

Diff = lambda iNo1, iNo2 : (iNo1 - iNo2)

Mult = lambda iNo1, iNo2 : (iNo1 * iNo2)

Div = lambda No1, No2 : (No1 / No2)

def main():
    iNo1 = 0
    iNo2 = 0

    iNo1 = int(input("Enter Number 1: "))

    iNo2 = int(input("Enter Number 2: "))

    Ret = Sum(iNo1,iNo2)
    print("Sum: ",Ret)

    Ret = Diff(iNo1, iNo2)
    print("Difference: ",Ret)

    Ret = Mult(iNo1, iNo2)
    print("Product: ",Ret)

    Ret = Div(iNo1, iNo2)
    print("Division: ",Ret)

if __name__ == "__main__":
    main()