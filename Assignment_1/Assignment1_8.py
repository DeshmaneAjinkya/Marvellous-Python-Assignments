def stars(no1):
    for no1 in range(no1):
        print("* ",end="")


def main():
    i = int(input("Enter Number Of Stars You Want To Enter: "))
    stars(i)

if __name__ == "__main__":
    main()