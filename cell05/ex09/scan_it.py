import sys

def main():
    """
    Scans a string for a keyword and prints the count, or 'none' if invalid input or not found.
    """
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    search_string = sys.argv[2]

    count = search_string.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()