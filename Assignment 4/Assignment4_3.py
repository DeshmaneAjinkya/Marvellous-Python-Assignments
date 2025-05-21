from functools import reduce

def RemoveF(Data):
    Final = []

    if ((Data >= 70) and (Data <= 90)):
        Final.append(Data)
    
    return Final

Add = lambda Data : Data + 10

Prod = lambda No1, No2 : No1 * No2

def main():
    Data = []
    Size = 0

    Size = int(input("Enter number of elements you want to add: "))

    for i in range (Size):
        print("Enter element number ",i+1,":")
        iNo = int(input())

        Data.append(iNo)
    
    FData = list(filter(RemoveF, Data))
    print("List After Filter:")
    print(FData)

    MData = list(map(Add, FData))
    print("List After Map:")
    print(MData)

    RData = reduce(Prod, MData)
    print("Product of FMR is: ",RData)

if __name__ == "__main__":
    main()