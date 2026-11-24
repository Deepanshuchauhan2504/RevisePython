def celcius_to_fahrenheit(c):
    fahrenheit = (c * 9 / 5) + 32
    return fahrenheit


def main():
    c = float(input("Please enter a temperature in Celcius: "))
    f = celcius_to_fahrenheit(c)

    print(f"The temperature in Fahrenheit is {f}")


if __name__ == "__main__":
    main()
