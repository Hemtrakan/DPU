def area_trapezium(a, b, h):
    area = 0.5 * (a + b) * h
    print(f"Area of a Trapezium is {area}")


def main():
    a = int(input("Enter number a : "))
    b = int(input("Enter number b : "))
    h = int(input("Enter number h : "))
    area_trapezium(a, b, h)

if __name__ == "__main__":
    main()
