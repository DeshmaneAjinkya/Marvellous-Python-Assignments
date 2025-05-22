Area = lambda No1, No2 : float(No1 * No2)

Peri = lambda No1, No2 : float((No1 + No2) * 2)

def main():
    fLength = 0.0
    fWidth = 0.0
    fAns = 0.0

    fLength = float(input("Enter Length: "))

    fWidth = float(input("Enter Width: "))

    fAns = Area(fLength,fWidth)
    print("Area is: ",fAns)

    fAns = Peri(fLength,fWidth)
    print("Perimeter is: ",fAns)

if __name__ == "__main__":
    main()