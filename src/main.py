# import functionalities from your source file.
# note that you are importing the file by folder structure (demos) and the file name (calculators)
import utilities.calculators
import utilities.formatters

def main():
    print("This is the main entry point for the application.\n\n")

    utilities.calculators.age_calculator()
    # utilities.calculators.expenses_calculator()

    # utilities.formatters.format_number()
    # utilities.formatters.format_string()


if __name__ == "__main__":
    main()
