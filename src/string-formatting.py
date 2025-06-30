def main():
    number = 12345.6789
    print(f"Formatted number: {number:.2f}")  # Format to 2 decimal places
    print(f"Formatted number: {number:.3f}")  # Format to 3 decimal places
    print(f"Currency: ${number:,.2f}")  # Format as currency with commas and 2 decimal places

main()