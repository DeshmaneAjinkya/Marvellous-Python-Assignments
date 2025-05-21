from functools import reduce

def Prime(Data):
    No1 = int(Data / 2)
    Cntr = True
    Final = []

    while (No1 > 1):
        if (Data % No1 == 0):
            Cntr = False
        
        No1 = No1 - 1

    if (Cntr == True):
        Final.append(Data)

    return Final

Mult = lambda Data : Data * 2

def Max(No1, No2):
    iMax = No1

    if (No2 > No1):
        iMax = No2

    return iMax

def main():
    Data = []
    Size = 0

    Size = int(input("Enter number of elements you want to add: "))

    for i in range (Size):
        print("Enter element number ",i+1,":")
        iNo = int(input())

        Data.append(iNo)
    
    FData = list(filter(Prime, Data))
    print("List After Filter:")
    print(FData)

    MData = list(map(Mult, FData))
    print("List After Map:")
    print(MData)

    RData = reduce(Max, MData)
    print("Sum of FMR is: ",RData)

if __name__ == "__main__":
    main()