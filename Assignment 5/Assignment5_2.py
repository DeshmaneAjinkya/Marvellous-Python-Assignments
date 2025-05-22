def CheckVovel(DemoChar):
    bFlag = False

    if ((DemoChar == 'a') or (DemoChar == 'e') or (DemoChar == 'i') or (DemoChar == 'o') or (DemoChar == 'u') or (DemoChar == 'A') or (DemoChar == 'E') or (DemoChar == 'I') or (DemoChar == 'O') or (DemoChar == 'U')):
        bFlag = True

    return bFlag

def main():
    bFlag = False
    
    Char = input("Enter Character: ")

    bFlag = CheckVovel(Char)

    if (bFlag == True):
        print(Char," is a vovel")
    else:
        print(Char," is not a vovel")

if __name__ == "__main__":
    main()