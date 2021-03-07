if __name__ == "__main__":
    n = str(input("Enter a number to find palindrome: "))
    r = ''.join(list(reversed(n)))
    if int(n) == int(r):
        print("Palindrome")
    else:
        print("Not a Palindrome")
