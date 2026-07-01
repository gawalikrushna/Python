from MarvellousLibrary import *

ChkEven = lambda No: No % 2 == 0

Incremnet = lambda No : No + 1

Addition = lambda No1, No2 : No1 + No2

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is : ",Data)

    FData = list(filterX(ChkEven,Data))

    print("Data after filter : ",FData)

    MData = list(mapX(Incremnet,FData))
    
    print("Data after map : ",MData)

    RData = reduceX(Addition,MData)

    print("Data after reduce : ",RData)

if __name__ == "__main__":
    main()