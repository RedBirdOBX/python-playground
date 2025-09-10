"""
Module providing a common calculator functions.
importing folder_name and then file_name.
"""
# import utilities.calculators
# import utilities.formatters
# import demos.casting
# import demos.conditionals
# import demos.loops
# import demos.strings
# import demos.numbers
# import demos.lists
# import demos.primitive_types
# import demos.operators
# import demos.logical_operators
# import demos.functions
# import demos.inheritance
# import demos.files
# import demos.input
# import demos.print
# import demos.random_numbers
# import demos.rounding
# import demos.space_api
# import demos.try_catch
# import demos.weather_api
# import demos.version
# import demos.variables
import demos.using_global_variables

# import games.rolldice
# import games.lottery
# import games.rock_paper_scissors
# import mini_apps.loan_calculator
# import mini_apps.movie_schedule
# import dictionaries.dictionaries

import config

def main():
    """Main entry point for the application."""
    print("This is the main entry point for the application.")
    print(f"App Name: {config.APP_NAME}\n\n")

    # Utilities
    # utilities.calculators.age_calculator()
    # utilities.calculators.expenses_calculator()

    # utilities.formatters.format_number()
    # utilities.formatters.format_string()

    # Demos
    # demos.casting.demo()
    # demos.conditionals.demo()
    # demos.loops.demo()
    # demos.strings.demo()
    # demos.lists.demo()
    # demos.primitive_types.demo()
    # demos.operators.demo()
    # demos.logical_operators.demo()
    # demos.numbers.demo()
    # demos.functions.demo()
    # demos.inheritance.demo()
    # demos.files.demo()
    # demos.input.demo()
    # demos.print.demo()
    # demos.random_numbers.demo()
    # demos.rounding.demo()
    # demos.space_api.demo()
    # demos.try_catch.demo()
    # demos.weather_api.demo()
    # demos.version.demo()
    # demos.variables.demo()
    demos.using_global_variables.demo()

    # Games
    # games.rolldice.game()
    # games.lottery.play_lottery()
    # games.rock_paper_scissors.play_game()

    # Dictionaries
    # dictionaries.dictionaries.demo()

    #Mini Apps
    # mini_apps.loan_calculator.demo()
    # mini_apps.movie_schedule.demo()

if __name__ == "__main__":
    main()
