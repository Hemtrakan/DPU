import math

def circle(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area , circumference

def square(h):
    area = h**2
    circumference = h * 4
    return area , circumference 

def main():
    radius = int(input("Enter Radius : "))
    area_of_circle, circum_of_circle = circle(radius)
    print(f"area_of_circle : {area_of_circle}")
    print(f"circum_of_circle : {circum_of_circle}")
    
    h = int(input("Enter Side : "))
    area_of_square, circum_of_square = square(h)
    print(f"area_of_square : {area_of_square}")
    print(f"circum_of_square : {circum_of_square}")
    
if __name__ == "__main__":
    main()


# def func_add(a, b):
#     print(f"ผลบวก  {a} + {b} = {a + b}")

# def func_mul(a, b):
#     print(f"ผลคูณ   {a} x {b} = {a * b}")

# def func_minus(a,b):
#     print(f"ผลลบ   {a} - {b} = {a - b}")
    
# def func_divide(a,b):
#     print(f"ผลหาร  {a} / {b} = {a / b}")

# a = 2
# b = 4
# func_add(a, b)
# func_mul(a, b)
# func_minus(a, b)
# func_divide(a, b)
