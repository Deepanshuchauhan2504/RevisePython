def reverse_a_number(n):
    ans = 0
    while n>0:
        ans = ans*10 + n%10
        n //= 10

    return ans
def main():
    print(reverse_a_number(105))

if __name__ == "__main__":
    main()
