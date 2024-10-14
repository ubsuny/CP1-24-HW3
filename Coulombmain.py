import Coulumb

coulomb_to_microcoulomb = 10**-6

def main():

    q1 = float(input("Enter charge q1 (in microcoulombs): "))

    q2 = float(input("Enter charge q2 (in microcoulombs): "))

    q1, q2 = map(lambda q: q * coulomb_to_microcoulomb, [q1, q2])

    r = float(input("Enter distance r (in centimeters): "))

    result = Coulumb.calculate_electric_force(q1, q2, r)

    print(f"q1 in microcoulombs: {q1} µC")
    print(f"q2 in microcoulombs: {q2} µC")

    print("The electric force between q1 and q2 is ", result, "N")

if __name__ == "__main__":
    main()