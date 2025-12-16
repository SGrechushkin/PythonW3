from os.path import commonpath
# add default lists


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

union_a, union_b = union_by_index(list1, list2)
print("Union A:", union_a)
print("Union B:", union_b)
'''
def unique_elements(list1, list2):
    #Converting lists to sets
    set1 = set(list1)
    set2 = set(list2)
    # Select all unique elements from 2 sets
    unique = set1 ^ set2
    # Return as a list
    return list(unique)

def sort_lists_asc(list1, list2):
    #Sorting two lists
    asc_list1 = sorted(list1)
    asc_list2 = sorted(list2)
    # Return 2 new lists
    return asc_list1, asc_list2

def sort_lists_des(list1, list2):
    # Sorting two lists in reverse
    des_list1 = sorted(list1, reverse=True)
    des_list2 = sorted(list2, reverse=True)
    # Return 2 new lists
    return des_list1, des_list2

def elements_less_than_30(list1, list2):
    #Select elements lover then 30 from lists
    less_list1 = [x for x in list1 if x < 30]
    less_list2 = [x for x in list2 if x < 30]
    #Connecting elements lover then 30 in one list
    less_than_30 = less_list1 + less_list2
    #Return list
    return less_than_30

def continue_actions():
    #Function to continue the operations
    while True:
        #Check the ansver
        print ("do you want to continue enter 'yes' or 'no':")
        ansver=input().strip().lower()

        if ansver == "yes":
            return True
        elif ansver == "no":
            print ("The operation is over")
            return False
        else:
            print("Incorrect input. Please enter 'yes' or 'no'.")


#main function
def main():
    list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
    list2 = [99, 7, 3, 101, 12, 22, 67, 55, 11, 2]

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

        if action in ["a", "b", "c", "d", "e", "f", "g"]:
            return action
        #Rerun function if selected wrong letter, because no return in function
        else:
            print("Incorrect item selected. Please re-enter:")

            if action == "a":
                print(common_elements(list1, list2))
            elif action == "b":
                print(unique_elements(list1, list2))
            elif action == "c":
                asc_list1, asc_list2 = sort_lists_asc(list1, list2)
                #Print new lists from new line
                print(asc_list1)
                print(asc_list2)
            elif action == "d":
                des_list1, des_list2 = sort_lists_des(list1, list2)
                print(des_list1)
                print(des_list2)
            elif action == "e":
                print(elements_less_than_30(list1, list2))
            #Chek the ansver from continue_actions() function and break if False
            if not continue_actions():
                break
# Call the main function
main()
'''