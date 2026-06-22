def Area(Radius, PI):
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(10.5, 3.14)
    print("Area of circle is : ",Ret)

    Ret2 = Area(13.6, 7.12)
    print("Area of circle is : ",Ret2)

if __name__ == "__main__":
    main()