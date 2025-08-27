def demo():

    # Python can have 60+ error messages.

    try:
        # Code that may raise an exception
        result = 10 / 0  # This will raise a ZeroDivisionError
        print("Result:", result)
    except ZeroDivisionError as e:
        # Handle the specific exception
        print("Error: Cannot divide by zero.")
        print("Exception message:", e)

        # Raise the exception
        raise e

    except Exception as e:
        # Handle any other exceptions
        print("An unexpected error occurred:", e)

        raise Exception("A new exception was raised.") from e

    else:
        # Code to run if no exceptions were raised
        print("Operation completed successfully.")
    finally:
        # Code that will run no matter what
        print("Execution of the try-except block is complete.")
