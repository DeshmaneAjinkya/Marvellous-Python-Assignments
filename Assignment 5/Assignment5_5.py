CheckEven = lambda iNo : int(iNo % 2)

def main():
    iNo = 0
    iAns = 0

    iNo = int(input("Enter Number: "))

    iAns = CheckEven(iNo)

    if (iAns == 0):
        print("Number is even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()