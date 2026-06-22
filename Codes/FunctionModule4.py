from Marvellous import Addition, Substraction

def main():
    print("Enter first number: ")
    Value1 = int(input())

    print("Enter second number: ")
    Value2 = int(input())

    ret = Addition(Value1, Value2) 

    print("Addition is : ",ret)

    ret = Substraction(Value1, Value2) # Error

    print("Substraction is : ",ret)

if __name__ == "__main__":
    main()

