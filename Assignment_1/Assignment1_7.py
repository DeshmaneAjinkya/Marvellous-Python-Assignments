def div5(no1):
    flag = False
    if((no1 % 5) == 0):
        flag = True
    
    return flag

def main():
    i = int(input("Enter Number That You Want To Check If It Is Divisible By 5:"))
    flag = div5(i)

    if flag == True:
        print(flag)
    else:
        print(flag)

if __name__ == "__main__":
    main()