def CheckAge(Age):
    bFlag = False

    if (Age >= 18):
        bFlag = True

    return bFlag

def main():
    bFlag = False
    iAge = 0

    iAge = int(input("Enter Age: "))

    if (iAge <= 0):
        print("Invalid Age!")
        return
    
    bFlag = CheckAge(iAge)

    if (bFlag == True):
        print("Valid Age for Voting!")

    else:
        print("Invalid Age for Voting!")

if __name__ == "__main__":
    main()