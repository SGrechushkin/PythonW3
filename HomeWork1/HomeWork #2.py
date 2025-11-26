from os.path import commonpath
# add default lists
default_list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5]
default_list2 = [99, 7, 3, 101, 12, 22, 67]

#Function for choosing the lists
def choose_data():
   #Endless cycle
    while True:
        print ("Choose the test data: input 'a' for Default test data or 'b' to Enter your own test data")
        #Input in lower cases without spaces
        choice = input().strip().lower()

        if choice  == 'a':
            # Return values to function
            return default_list1, default_list2

        elif choice  == 'b':
                print  ("Enter the first list of numbers separated by spaces. For example, '1 2 3 4'")
                #Create a list from the input. Split - separate the input by spaces
                raw1 = input().split()
                #Convert values to a list
                custom_list1 = [int(x) for x in raw1]

                print("Enter the second list of numbers separated by spaces. For example, '1 2 3 4'")
                raw2 = input().split()
                custom_list2 = [int(x) for x in raw2]
                return custom_list1, custom_list2
        else:
            print ("Incorrect item selected")


def choose_action():
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
        #Rerun function if selected wrong letter, because no return in function
        else:
            print("Incorrect item selected. Please re-enter.")

#Logical functions
def common_elements(list1, list2):
    #Converting lists to sets
    set1 = set(list1)
    set2 = set(list2)
    #Select all common elements from 2 sets
    common = set1 & set2
    return list(common)


def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    unique = set1 ^ set2
    return list(unique)

def sort_lists_asc(list1, list2):
    asc_list1 = sorted(list1)
    asc_list2 = sorted(list2)

    return asc_list1, asc_list2

def sort_lists_des(list1, list2):
    des_list1 = sorted(list1, reverse=True)
    des_list2 = sorted(list2, reverse=True)

    return des_list1, des_list2

def elements_less_than_30(list1, list2):
    less_list1 = [x for x in list1 if x < 30]
    less_list2 = [x for x in list2 if x < 30]

    less_than_30 = less_list1 + less_list2
    return less_than_30

def continue_actions():
    while True:
        print ("do you want to continue enter 'yes' or 'no':")
        ansver=input().strip().lower()

        if ansver == "yes":
            return True
        elif ansver == "no":
            print ("The operation is over")
            return False
        else:
            print("Incorrect input. Please enter 'yes' or 'no'.")



def main():
    list1, list2 = choose_data()
   # action = choose_action()
    common = common_elements(list1, list2)
    unique = unique_elements(list1, list2)
    asc_list1, asc_list2 = sort_lists_asc(list1, list2)
    des_list1, des_list2 = sort_lists_des(list1, list2)
    less_than_30 = elements_less_than_30(list1, list2)

    while True:
        action = choose_action()

        if action == "a":
            print(common_elements(list1, list2))
        elif action == "b":
            print(unique_elements(list1, list2))
        elif action == "c":
            asc_list1, asc_list2 = sort_lists_asc(list1, list2)
            print(asc_list1)
            print(asc_list2)
        elif action == "d":
            des_list1, des_list2 = sort_lists_des(list1, list2)
            print(des_list1)
            print(des_list2)
        elif action == "e":
            print(elements_less_than_30(list1, list2))

        if not continue_actions():
            break

main()