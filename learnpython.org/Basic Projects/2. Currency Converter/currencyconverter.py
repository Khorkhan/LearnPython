def main():
    exchange_rates = {
        "USD": 0.028,
        "JPY": 4.20,
        "KRW": 37.50
    }

    print("=== Currency Converter (Bath) ===")

    try:
        thb_amount = float(input("input bath: "))

        print("\n Select currency: ")
        print("1. USD")
        print("2. JPY")
        print("3. KRW")

        choice = input("Select (1/2/3): ")

        if choice == "1":
            result = thb_amount * exchange_rates["USD"]
            print(f"{thb_amount} bath to dollar: {result:.2f} USD.")
        elif choice == "2":
            result = thb_amount * exchange_rates["JPY"]
            print(f"{thb_amount} bath to yen: {result:.2f} JPY.")
        elif choice == "3":
            result = thb_amount * exchange_rates["KRW"]
            print(f"{thb_amount} bath to won: {result:.2f} KRW.")
        else:
            print("Wrong menu")

    except ValueError:
        print("Please enter numbers only.")

if __name__ == "__main__":
    main()