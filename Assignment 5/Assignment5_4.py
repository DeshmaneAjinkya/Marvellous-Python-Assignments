def Largest(iNo1, iNo2, iNo3):
    iRet = iNo1

    if(iRet <= iNo2):
        iRet = iNo2
        if (iRet <= iNo3):
            iRet = iNo3
    if(iRet <= iNo3):
        iRet = iNo3

    return iRet

def main():
    iNo1 = 0
    iNo2 = 0
    iNo3 = 0
    iAns = 0

    iNo1 = int(input("Enter Number 1: "))

    iNo2 = int(input("Enter Number 2: "))

    iNo3 = int(input("Enter Number 3: "))

    iAns = Largest(iNo1,iNo2,iNo3)

    print("Largest Number is: ",iAns)

if __name__ == "__main__":
    main()