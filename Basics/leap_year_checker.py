def leap_year(year):
    if(year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    year = int(input("Enter a year: "))
    if(leap_year(year)):
        print("Leap Year")
    else:
        print("Not a Leap Year")


if __name__ == "__main__":
    main()