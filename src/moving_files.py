import os

def main():

    print("-------------")

    old_path = r"C:\Users\shane\Desktop\old"
    new_path = r"C:\Users\shane\Desktop\new"

    # 1) make new folder "new" if needed
    # backslashes (\) in Windows paths are interpreted as escape characters in Python strings.
    # Solution: Use raw strings by prefixing the string with r, or use forward slashes /
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    # 2) list files in the "old" folder
    entries = os.scandir(old_path)

    # loop thru files and move each one to new folder
    for entry in os.scandir(old_path):
        location_orig = os.path.join(old_path, entry.name)
        location_new = os.path.join(new_path, entry.name)

        if os.path.isfile(location_orig):
            os.rename(location_orig, location_new)


        # if os.path.isfile(entry):
        #     print("File found:", entry.name)
        #     print(entry.path)

        #     # 3) move each file to the "new" folder

        # elif os.path.isdir(entry):
        #     print("Directory found:", entry.name)


main()
