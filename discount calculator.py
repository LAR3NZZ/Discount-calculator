def calculate_discount(price, discount_percent):
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a number.")

    if not isinstance(discount_percent, (int, float)):
        raise ValueError("Discount must be a number.")

    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100.")

    final_price = price * (1 - discount_percent / 100)
    return round(final_price, 2)


def main():
    while True:
        try:
            price = float(input("Original price: "))
            discount_percent = float(input("Discount percentage: "))
            final_price = calculate_discount(price, discount_percent)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        savings = price - final_price
        print(f"Original price: {price:.2f}")
        print(f"Discount: {discount_percent:.0f}%")
        print(f"You save: {savings:.2f}")
        print(f"Final price: {final_price:.2f}")

        again = input("Calculate another price? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye.")
            break


if __name__ == "__main__":
    main() 