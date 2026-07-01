ChkEven = lambda No : No % 2 == 0

Incremnet = lambda No : No + 1

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is : ",Data)

    FData = list(filter(ChkEven,Data))

    print("Data after filter : ",FData)

    MData = list(map(Incremnet,FData))
    
    print("Data after map : ",MData)

if __name__ == "__main__":
    main()