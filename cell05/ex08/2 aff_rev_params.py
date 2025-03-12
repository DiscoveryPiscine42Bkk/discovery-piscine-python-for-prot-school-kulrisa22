import sys

def main():
    """
    Displays the command-line arguments in reverse order, or 'none' if there are fewer than two.
    """
    args = sys.argv[1:]  # Exclude the script name itself

    if len(args) < 2:
        print("none")
    else:
        for arg in reversed(args):
            print(arg)

if __name__ == "__main__":
    main()