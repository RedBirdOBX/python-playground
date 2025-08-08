"""Strings demo."""
def demo():

    """Demo of string operations."""
    fname = "john"
    lname = "doe"
    fullname = f"{fname} {lname}"
    fullname_upper = fullname.upper()
    fullname_lower = fullname.lower()
    fullname_title = fullname.title()

    print(fname)
    print(lname)
    print(fullname)
    print(fullname_upper)
    print(fullname_lower)
    print(fullname_title)
    print(fullname.swapcase())

    message = "Hello, World!   "
    print(message[0])
    print(message[1])

    # find - like IndexOf
    print(message.find("World"))

    # strip
    print(message.strip())

    # casing
    print(message.upper())
    print(message.lower())
    print(message.title())

    # len
    print(len(message))

    # replace
    message2 = "Hello, Python!"
    print(message2.replace("Python", "New World"))

    # escaping
    print("Hello \"World\"")
    print('Hello \'World\'')

    # slicing [start index start BEFORE position: end index - end BEFORE position]
    # formula: [first char : last char + 1]
    print(message[0:13])

    print(message[:5])  # Hello
    print(message[7:])  # World

    # calculate half-way point with integer division
    half = len(message) // 2
    print(message[:half])  # Hello
    print(message[half:])  # World!

    # pig latin
    word = "Python"
    first = word[0]
    rest = word[1:]
    result = rest + "-" + first + "y"
    print(result)

    # long string
    long_message = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque congue tempor nibh.
    Maecenas viverra volutpat odio, eget tincidunt velit vehicula a. Nullam lacinia
    pharetra diam, sit amet sagittis felis pretium eget. Interdum et malesuada fames
    ac ante ipsum primis in faucibus. Aenean pellentesque, metus nec ultricies molestie,
    diam orci luctus risus, commodo aliquet lorem mauris gravida elit. Nulla facilisi.
    Nulla et tellus sed orci cursus vehicula. Aliquam ut purus tempus magna tempus auctor
    quis in odio.

    Integer scelerisque eu neque eget sollicitudin. In iaculis a sem ut tempus.
    Sed interdum lobortis quam ac volutpat. Etiam id commodo orci. Pellentesque
    tincidunt scelerisque vulputate. Aliquam vulputate et quam a facilisis.
    Donec vestibulum congue nulla, at dapibus mi pellentesque in. Proin tristique nunc
    molestie, rhoncus nulla a, faucibus velit. Sed facilisis tellus nunc,
    vel dapibus mauris iaculis in. Nunc id mattis leo. Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. In porttitor sed metus quis posuere.
    In suscipit et felis ut malesuada. Duis mi enim, dapibus quis pellentesque at,
    placerat sed dui. Integer posuere sem lorem, ac venenatis tellus laoreet sit amet.
    Sed ut nibh non risus mollis auctor.
    """
    print(long_message)


    # looking for substrings
    print("Hello" in long_message)
    print("rhoncus" in long_message)
    print("foobar" not in long_message)
