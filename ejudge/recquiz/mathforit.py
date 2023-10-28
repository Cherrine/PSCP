"""math for it"""
import math
def calculate(ray):
    """calculate"""
    area = math.pi*(ray**2)
    cir = 2*math.pi*ray
    print("Area: " + "%.3f" %area)
    print("Circumference: " + "%.3f" %cir)
calculate(float(input()))
