ChkEven = lambda No:(No % 2 == 0)
    
def main():
    Value = int(input("Enter number : "))
    Ret = ChkEven(Value)

    if (Ret == True):
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()