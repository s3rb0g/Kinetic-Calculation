def compute(mass, velocity):
    kinetic = 0.5 * mass * (velocity ** 2)
    
    return kinetic

kg = float(input("\nEnter mass in kilometers: "))
ms = float(input("Enter velocity in meters per second: "))

ke = compute(kg, ms)
ke = round(ke, 2)

print("\nThe object's kinetic energy is:", ke , "J.\n")