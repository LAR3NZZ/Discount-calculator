def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number."

    if not isinstance(discount, (int, float)):
        return "The discount should be a number."

    if price <= 0:
        return "The price should be greater than 0."

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."

    final_price = price * (1 - discount / 100)
    return round(final_price, 2)


def format_currency(value):
    return f"KSh {value:,.2f}"


def print_banner():
    print("\n" + "=" * 52)
    print("   KENYAN SHILLINGS DISCOUNT CALCULATOR".center(52))
    print("=" * 52)
    print(" Price after discount\n")


def main():
    while True:
        print_banner()

        try:
            price = float(input("Original price (KSh): "))
            discount = float(input("Discount percentage: "))
        except ValueError:
            print("\nPlease enter valid numeric values. Try again.\n")
            continue

        result = apply_discount(price, discount)

        if isinstance(result, str):
            print(f"\n⚠️  {result}\n")
        else:
            savings = price - result
            print("\n" + "-" * 52)
            print(f"Original price:   {format_currency(price)}")
            print(f"Discount:         {discount:.0f}%")
            print(f"You save:         {format_currency(savings)}")
            print(f"Final price:      {format_currency(result)}")
            print("-" * 52)

        again = input("\nCalculate another price? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThanks for using the discount calculator.\n")
            break


if __name__ == "__main__":
    main()