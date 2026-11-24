def check_input(user_input):
    try:
        int(user_input)
        return "Integer"
    except ValueError:
        try:
            float(user_input)
            return "Decimal (Float)"
        except ValueError:
            return "String (Not a number)"


def main():
    first = input("Enter first value: ")
    second = input("Enter second value: ")

    print(f"First input is: {check_input(first)}")
    print(f"Second input is: {check_input(second)}")


if __name__ == "__main__":
    main()