ConvertTemp = lambda Degree : ((Degree * 9/5) + 32)

def main():
    Degree = 0.0
    Fahrenheit = 0.0

    Degree = float(input("Enter Temprature in Degree Celsius: "))

    Fahrenheit = ConvertTemp(Degree)

    print(Degree," in Fahrenheit is ",Fahrenheit,"°F")

if __name__ == "__main__":
    main()