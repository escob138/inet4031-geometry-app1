import math

def volume(radius):
    return (4/3) * math.pi * (radius ** 3)

def main():
    print("Geometry Calculator - Sphere")
    print("----------------------------")
    rad = float(input("Enter the radius: "))
    vol = volume(rad)
    print(f"The volume of a sphere with radius {rad} is: {vol}")

if __name__ == "__main__":
    main()
