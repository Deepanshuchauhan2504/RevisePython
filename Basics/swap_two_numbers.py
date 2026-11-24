def swap( a, b):
    a = a^b
    b = b^a
    a = a^b
    return [a, b]

def main():
    a = 15
    b = 5
    print(swap(a, b))


if __name__ == "__main__":
    main()