default_list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
default_list2 = [99, 7, 3, 101, 12, 22, 67]

def choose_data():
    while True:
        print ("Choose the test data: input 'a' for Default test data or 'b' to Enter your own test data")
        choice = input().strip().lower()

        if choice  == 'a':
            return default_list1, default_list2

        elif choice  == 'b':
                print  ("Enter the first list of numbers separated by spaces. For example, '1 2 3 4'")
                raw1 = input().split()
                custom_list1 = [int(x) for x in raw1]

                print("Enter the second list of numbers separated by spaces. For example, '1 2 3 4'")
                raw2 = input().split()
                custom_list2 = [int(x) for x in raw2]
                return custom_list1, custom_list2
        else:
            print ("Incorrect item selected")




def show_menu():
    while True:
        print("Select an action (enter a letter):")
        print("Enter 'a' to Display a list of elements which exist in both lists.")
        print("Enter 'b' to Display a list of elements (from both lists) which exist only in one list. ")
        print("Enter 'c' to Display both lists sorted in ascending order.")
        print("Enter 'd' to Display both lists sorted in descending order.")
        print("Enter 'e' to Print a list of all elements of two lists that are less than 30.")


        action = input().strip().lower()

        if action in ["a", "b", "c", "d", "e"]:
            return action
        else:
            print("Incorrect item selected. Please re-enter.")

list1, list2 = choose_data()
action = show_menu()

print("\nYou selected:", action)
print("List1:", list1)
print("List2:", list2)