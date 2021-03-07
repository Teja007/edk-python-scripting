def print_alphabets_and_digits(s: str):
    alphabets = 0
    digits = 0
    for c in s:
        if c.isalpha():
            alphabets += 1
            continue
        if c.isdigit():
            digits += 1
    print(f"LETTERS: {alphabets}")
    print(f"DIGITS: {digits}")


if __name__ == "__main__":
    st = input("Enter an sentence: ")
    print_alphabets_and_digits(st)
