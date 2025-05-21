from functools import reduce

def Even(Data):
    Final = []

    if Data % 2 == 0:
        Final.append(Data)
    
    return Final

Square = lambda Data : Data * Data

def Sum(No1, No2):

    return No1 + No2

def main():
    Data = []
    Size = 0

    Size = int(input("Enter number of elements you want to add: "))

    for i in range (Size):
        print("Enter element number ",i+1,":")
        iNo = int(input())

        Data.append(iNo)
    
    FData = list(filter(Even, Data))
    print("List After Filter:")
    print(FData)

    MData = list(map(Square, FData))
    print("List After Map:")
    print(MData)

    RData = reduce(Sum, MData)
    print("Sum of FMR is: ",RData)

if __name__ == "__main__":
    main()