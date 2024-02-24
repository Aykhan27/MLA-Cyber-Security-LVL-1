import math
from sympy import gcd  # Sympy library is used for calculating the gcd

def pollards_p_minus_1(n, B=10000000000000000000000000000000000000000000000000000000):
    a = 2
    for j in range(20000000000000000, B):
        a = pow(a, j, n)
        d = gcd(a - 1, n)
        if 1 < d < n:
            return d
    return None  # No factor found

# Convert hexadecimal values to decimal
n_hex = "a09d5bbe7b77137e4a923e89057edaac71a600b229ad43bd20e56b5aa2e2ddd4a1171322d4af4fa8f48437a7663917f726b225964df20a37df79210694a081f5f28199e35997f52dfcaa5c7b9971b00b02acf2fc2fead62ed0bbc6fd5c275fb5d72ead7fe5b82b9818717acf77d6108fef8a56c5a2307866f8779d336a8f44d0cb8699f4c2db98564fed93e863f48778f802cc9d32b7185cd76a47fec3b056e804a26b4d1b254f055e73ffc08a547ad4bede1d297876140665ae93f04cacb6f88665797d6e48a9ba3d1500f16067adfb5624199e73ccd806c283a399e25b8cc223575112353b3ed24939f98dc33e0ac5298b690995ffcc5ce66d7e9ef976a801"
n = int(n_hex, 16)

# Attempt to find a nontrivial factor of n
factor = pollards_p_minus_1(n)

if factor:
    print(f"Found factor: {factor}")
else:
    print("No factor found with Pollard's p-1 within the given bound.")
