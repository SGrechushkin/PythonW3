
#Logical functions
def union_by_index(list1, list2):
    # This function creates two new lists based on index positions
    union_a = []
    union_b = []

    # Add elements with even indexes from the first list to union_a
    for i in range(len(list1)):
        if i % 2 == 0:
            union_a.append(list1[i])
    # Add elements with odd indexes from the second list to union_a
    for i in range(len(list2)):
        if i % 2 == 1:
            union_a.append(list2[i])
    # Add elements with odd indexes from the first list to union_b
    for i in range(len(list1)):
        if i % 2 == 1:
            union_b.append(list1[i])
    # Add elements with even indexes from the second list to union_b
    for i in range(len(list2)):
        if i % 2 == 0:
            union_b.append(list2[i])
    # Return both generated lists
    return union_a, union_b

def sort_asc(data):
    # This function returns a new list sorted in ascending order
    return sorted(data)

def sort_des(data):
    # This function returns a new list sorted in descending order
    return sorted(data, reverse=True)

#main function
def main():
    # Initialize default lists
    list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
    list2 = [99, 7, 3, 101, 12, 22, 67, 55, 11, 2]

    union_a, union_b = union_by_index(list1, list2)
    #Menu
    while True:
        print("Select an action (enter a letter):")
        print("Enter 'a' a list that consists of all the even index elements (let's think that 0 is even) of the first list and the odd index ones from the second.")
        print("Enter 'b' to Display a list that consists of all the even index elements of the second list and the odd index ones from the first.")
        print("Enter 'c' to Display a list from the task item a, but sorted in ascending order.")
        print("Enter 'd' to Display a list from the task item a, but sorted in descending order.")
        print("Enter 'e' to Display a list from the task item b, but sorted in ascending order.")
        print("Enter 'f' to Display a list from the task item b, but sorted in descending order.")
        print("Enter 'g' to Finish.")

        # Read user input and normalize it
        action = input().strip().lower()

        # Execute selected action
        if action == "a":
            print(union_a)
        elif action == "b":
            print(union_b)
        elif action == "c":
                print(sort_asc(union_a))
        elif action == "d":
                print(sort_des(union_a))
        elif action == "e":
                print(sort_asc(union_b))
        elif action == "f":
                print(sort_des(union_b))
        elif action == "g":
                print("Finish")
                break
        # Handle incorrect input
        else:
            print("Incorrect item selected. Please re-enter.")

# Call the main function
main()
