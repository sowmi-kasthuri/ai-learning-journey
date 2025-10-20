# implement a program in Python that prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer. 
# Assume that the user will input an integer.

# 𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy (measured in Joules), 
# 𝑚 represents mass (measured in kilograms), 
# and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al.

def main():
    mass = int(input("Enter mass in kg: ") or "0")
    c = 300000000
    energy = mass * c**2
    print(f"Equivalent energy in Joules: {energy:,}")

main()
