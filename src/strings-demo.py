def main():

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

    message = "Hello, World!"
    print(message[0])
    print(message[1])

    #len
    print(len(message))

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

main()

