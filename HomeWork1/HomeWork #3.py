
#Logical functions
list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
list2 = [99, 7, 3, 101, 12, 22, 67, 55, 11, 2]
def union_by_index(list1, list2):
    union_a = []
    union_b = []

    for i in range(len(list1)):
        if i % 2 == 0:
            union_a.append(list1[i])
    for i in range(len(list2)):
        if i % 2 == 1:
            union_a.append(list2[i])
    for i in range(len(list1)):
        if i % 2 == 1:
            union_b.append(list1[i])
    for i in range(len(list2)):
        if i % 2 == 0:
            union_b.append(list2[i])
    return union_a, union_b

def sort_asc(data):
    return sorted(data)

def sort_des(data):
    return sorted(data, reverse=True)

#main function
def main():
    list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
    list2 = [99, 7, 3, 101, 12, 22, 67, 55, 11, 2]

    union_a, union_b = union_by_index(list1, list2)

    while True:
        print("Select an action (enter a letter):")
        print("Enter 'a' a list that consists of all the even index elements (let's think that 0 is even) of the first list and the odd index ones from the second.")
        print("Enter 'b' to Display a list that consists of all the even index elements of the second list and the odd index ones from the first.")
        print("Enter 'c' to Display a list from the task item a, but sorted in ascending order.")
        print("Enter 'd' to Display a list from the task item a, but sorted in descending order.")
        print("Enter 'e' to Display a list from the task item b, but sorted in ascending order.")
        print("Enter 'f' to Display a list from the task item b, but sorted in descending order.")
        print("Enter 'g' to Finish.")

        action = input().strip().lower()

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
        else:
            print("Incorrect item selected. Please re-enter.")
# Call the main function
main()
