def circle_area(radius):
    c_area = 3.14 * (radius ** 2)
    print("Circle area is ", c_area)
    return c_area

def triangle_area(lenght_a, height):
    t_area = 0.5 * lenght_a * height
    print("Triangle area is", t_area)
    return t_area

def rectangle_area(lenght_a, lenght_b):
    r_area = lenght_a * lenght_b
    print("Rectangle area is", r_area)
    return r_area

def trapeze_area(lenght_a, lenght_b, height):
    trap_area = 0.5 * (lenght_a + lenght_b) * height
    print("Trapeze area is", trap_area)
    return trap_area