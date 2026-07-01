ChkEven = lambda No: No % 2 == 0

Incremnet = lambda No : No + 1

Addition = lambda No1, No2 : No1 + No2

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no) # ChkEven(no)

        if Ret == True:
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no) #Increment(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Elemets):
    Sum = 0

    for no in Elemets:
        Sum = Task(Sum, no)  # Addition(no)

    return Sum

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