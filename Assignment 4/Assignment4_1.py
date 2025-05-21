Power = lambda No1 : (2**No1)

def main():
    No1 = 0
    Ret = 0

    No1 = int(input("Enter Number: "))

    Ret = Power(No1)

    print("2 To The Power ",No1," Is ",Ret)


if __name__ == "__main__":
    main()