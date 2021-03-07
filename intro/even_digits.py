def are_digits_even(n: int) -> bool:
    tmp = str(n)
    for c in tmp:
        if int(c) % 2 != 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(1000, 3001):
        if are_digits_even(i):
            print(i, end=",")
