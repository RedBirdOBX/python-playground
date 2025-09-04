import sys

def demo():
    """Demo function to print the current Python version."""

    print("Current Python version:")
    print(sys.version)
    print("Version info:")
    print(sys.version_info)
    print(f"Major: {sys.version_info.major}")
    print(f"Minor: {sys.version_info.minor}")
    print(f"Micro: {sys.version_info.micro}")
    print(f"Release level: {sys.version_info.releaselevel}")
    print(f"Serial: {sys.version_info.serial}")
    print()
    