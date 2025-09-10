import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config


def demo():

    # reading a global variable from config
    print("using_global_variables.py demo")
    print(f"App Name: {config.APP_NAME}\n\n")
