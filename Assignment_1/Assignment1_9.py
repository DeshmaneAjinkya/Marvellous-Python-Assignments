def teneven():
    no1 = 1
    no2 = 1
    while (no1 <= 10):
        if ((no2 % 2) == 0):
            print(no2," ",end="")
            no1 = no1 + 1
        
        no2 = no2 + 1


def main():
    teneven()

if __name__ == "__main__":
    main()