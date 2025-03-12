number = input("Give me a number: ")

if"." in number:
    try:
        float(number)
        print("This number is a decimal.")
    except ValueError :
        print("Invalid input.")
else:
        try:
            int(number)
            print("This number is an integer.")
        except ValueError:
            print("Invalid input.")