def evenodd(no1):
    flag = False
    if((no1 % 2) == 0):
        flag = True
    
    return flag

def main():
    i = int(input("Enter Number That You Want To Check If It Is Even Or Odd:"))
    flag = evenodd(i)

    if flag == True:
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()