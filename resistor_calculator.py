# Resistor Combination Calculator
# Calculates total resistance in series and in parallel.
# EXTRA FEATURE: optional voltage input -> total current in each circuit.


def get_positive_number(prompt, as_int=False):
    """Keep asking until the user types a valid number greater than 0.
    Returns the number (int if as_int=True, otherwise float)."""
    while True:
        text = input(prompt)
        try:
            # Convert the text to int or float
            value = int(text) if as_int else float(text)
        except ValueError:
            print("Invalid input. Please type a number (e.g. 10 or 4.7).")
            continue
        if value <= 0:
            print("The value must be greater than 0.")
        else:
            return value


def series_resistance(resistors):
    """Return total resistance in series: R1 + R2 + ... + Rn."""
    total = 0
    for r in resistors:
        total += r
    return total


def parallel_resistance(resistors):
    """Return total resistance in parallel: 1 / (1/R1 + 1/R2 + ... + 1/Rn)."""
    inverse_sum = 0
    for r in resistors:
        inverse_sum += 1 / r
    return 1 / inverse_sum


def main():
    print("=== Resistor Combination Calculator ===")

    # Ask how many resistors there are
    count = get_positive_number("How many resistors do you have? ", as_int=True)

    # List to store each resistor value (in ohms)
    resistors = []

    # Loop to read each resistor value
    for i in range(1, count + 1):
        value = get_positive_number(f"Enter resistor {i} value (ohms): ")
        resistors.append(value)

    # Calculate both totals using the functions
    total_series = series_resistance(resistors)
    total_parallel = parallel_resistance(resistors)

    # Print results
    print("\n--- Results ---")
    print("Resistors (ohms):", resistors)
    print(f"Total resistance in series:   {total_series:.2f} ohms")
    print(f"Total resistance in parallel: {total_parallel:.2f} ohms")

    # EXTRA FEATURE: current calculation using Ohm's law (I = V / R)
    choice = input("\nCalculate current for a supply voltage? (y/n): ").strip().lower()
    if choice == "y":
        voltage = get_positive_number("Enter supply voltage (volts): ")
        print(f"Series current:   {voltage / total_series:.3f} A")
        print(f"Parallel current: {voltage / total_parallel:.3f} A")
    elif choice == "n":
        print("Okay, skipping current calculation.")
    else:
        print("Not a valid choice, so the current calculation was skipped.")


# Run the program
main()
