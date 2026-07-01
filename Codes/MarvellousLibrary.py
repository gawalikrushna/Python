
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
