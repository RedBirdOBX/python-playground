def main():

    rudiment = input("Enter a rudiment name: ").strip().lower()

    # MODES:
    # a append
    # r (read)
    # w (write)
    # x (exclusive creation)
    # b (binary)
    # t (text, default)
    

    # basic version
    # file = open(file_name, "r")
    # try:
    #     # do stuff
    #     pass
    # finally:
    #     file.close()

    # This must be run in the src folder.
    # A better way to locate the file would be:
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # file_name = os.path.join(script_dir, "rudiments.txt")

    # C:\Data\Projects\GitHubRepos\python-playground\python-playground\src\rudiments.txt
    # better version - will dispose of file properly
    file_name = "rudiments.txt"

    # print("file.read")
    # with open(file_name) as file:

    #     result1 = file.read()
    #     print(result1)

    # print("file.readline")
    # with open(file_name) as file:

    #     result2 = file.readline()
    #     print(result2.strip())

    # print("file.readlines")
    with open(file_name) as file:

        result3 = file.readlines()
        match_found = False

        for line in result3:
            # print(line.strip())
            if rudiment in line.strip().lower():
                print(f"Found: {line.strip()}")
                match_found = True
                break

    if not match_found:
        print("Rudiment not found.")
        rudiment = input("Enter a new rudiment name: ").strip().lower()
        definition = input("Enter the rudiment definition: ").strip()

        with open(file_name, "a") as file:
            file.write(f"{rudiment.capitalize()} - {definition}\n")

main()