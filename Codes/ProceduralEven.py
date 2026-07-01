def ChkEven(No):
    if No % 2 == 0:
        print("Even number")

    else:
        print("Odd number")

def main():
    Value = int(input("Enter number : "))
    ChkEven(Value)

if __name__ == "__main__":
    main()