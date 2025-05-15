import Assignment2_Module1

def main():
    no1 = int(input("Enter Number 1: "))
    no2 = int(input("Enter Number 2: "))

    ans = 0

    ans = Assignment2_Module1.Add(no1,no2)
    print("Addition of two numbers is: ",ans)

    ans = Assignment2_Module1.Sub(no1,no2)
    print("Subtraction of two numbers is: ",ans)

    ans = Assignment2_Module1.Mult(no1,no2)
    print("Multiplication of two numbers is: ",ans)

    ans = Assignment2_Module1.Div(no1,no2)
    print("Division of two numbers is: ",ans)
    
if __name__ == "__main__":
    main()