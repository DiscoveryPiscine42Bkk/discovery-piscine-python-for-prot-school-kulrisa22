# append_it.py

def append_to_list(existing_list, item):
    """Appends an item to the provided list."""
    existing_list.append(item)
    return existing_list

def display_list(arr):
    """Displays the contents of the list."""
    print("Current list:", arr)

def main():
    my_list = []

    while True:
        print("\n--- Append It! ---")
        print("1. Append an item")
        print("2. Display the list")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            item = input("Enter an item to append: ")
            my_list = append_to_list(my_list, item)
            print(f"Item '{item}' added to the list.")
        elif choice == "2":
            display_list(my_list)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose between 1-3.")

if __name__ == "__main__":
    main()