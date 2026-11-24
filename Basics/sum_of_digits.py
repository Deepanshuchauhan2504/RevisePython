def main():
    Number = int(input("Enter a number: "))
    n = digits(Number)
    print(f"Sum of digits is given number {Number} are {n}")

def digits(Number):
    ans = 0
    while(Number > 0):
        ans += Number % 10
        Number = Number // 10

    return ans




if __name__ == "__main__":
    main()