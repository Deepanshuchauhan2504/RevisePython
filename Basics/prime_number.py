import math


def prime_number(n):
    if n < 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False

    return True

def main():
    n = int(input("Enter a number: "))
    if prime_number(n):
        print("Prime number")
    else:
        print("Not a prime number")


if __name__ == "__main__":
    main()
