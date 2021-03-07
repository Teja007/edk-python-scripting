def get_factors(n: int) -> list:
    factors = list()
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


if __name__ == "__main__":
    x = int(input("Enter a number to find factors: "))
    f = get_factors(x)
    print(f"Factors: {f}")
    if len(f) % 2 == 0:
        print("Even Factors")
    else:
        print("Odd Factors")
