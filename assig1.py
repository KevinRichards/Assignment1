"""
Kevin Richards
9/9/16
Python program to emulate a shopping list in which the
name, price, priority of items is taken and stored in a file
The program can add new items, display items which are required
or which have already been completed, check off items as completed

https://github.com/KevinRichards/Assignment1
"""


def main():
    print("Shopping List 1.0 - by Kevin Richards")
    items_list = file_load()
    print(items_list)
    choice = get_user_choice()
    while choice.upper() != "Q":

        if choice.upper() == "A":
            name = input("Item name: ")
            while name == "":
                print("Input can not be blank")
                name = input("Item name: ")
            finished = False
            while finished == False:
                try:
                    price = float(input("Price: $"))
                    price >= 0
                    price != ""
                    finished = True
                except ValueError:
                    print("Invalid input; enter a valid number")
                except:
                    print("Price must be >=$0")
            finished = False
            while finished == False:
                try:
                    priority = int(input("Priority (1 - 3, 1 being high): "))
                    1 <= priority <= 3
                    priority != ""
                    finished = True
                except ValueError:
                    print("Invalid input; enter a valid number")
                except:
                    print("Priority must be 1, 2 or 3")
            items_list += [[name, str(price), str(priority), 'r']]
            print("{}, ${:.2f} (priority {}) added to shopping list".format(name, price, priority))

        elif choice.upper() == "C":
            print("Completed items:")
            complete_required(items_list, 'c')

        elif choice.upper() == "R":
            print("Required items:")
            complete_required(items_list, 'r')

            """if menu_choice = M
                sort items list by item priority
                for each item in items list
                    if item is required
                        display item details
                        add item to required items list
                        add item price to expected price
                    otherwise
                        add item to completed items list
                if nothing in required items list
                    display "No required items"
                otherwise
                    display expected price for required items
                get item to set as completed as index given by display
                set indexed item in required items list to complete
                item list = required items list + completed items list
                display item is completed"""

        elif choice.upper() == "M":
            items_list = complete_required(items_list, 'r')
            if items_list[-1] != 0:
                print("Enter the number of an item to mark as completed")
                finished = False
                while finished == False:
                    try:
                        complete_off = input(">>> ")
                        0 <= complete_off < items_list[-1]
                        finished = True
                    except ValueError:
                        print("Invalid input; enter a number")
                    except:
                        print("Invalid item number")
                items_list[int(complete_off)][3] = 'c'
                items_list = items_list[0:-1]
                print("{} marked as completed".format(items_list[int(complete_off)][0]))
        else:
            print("Invalid menu choice")
        choice = get_user_choice()

    file_save(items_list)
    print("Have a nice day :)")


def complete_required(array, r_c):
    from operator import itemgetter
    array.sort(key=itemgetter(2))
    r_c_items = []
    rest_items = []
    expected_price = []
    x = 0
    longest_word_length = max_char_length(array,0)
    max_cost_length = max_char_length(array,1) + 1
    for i in range(len(array)):
        if array[i][-1] == r_c:
            print("{}. {:{}}       $ {:{}.2f} ({})".format(x, array[i][0], int(longest_word_length), float(array[i][1]),
                                                           int(max_cost_length), array[i][2]))
            r_c_items += [array[i]]
            expected_price += [float(array[i][1])]
            x += 1
        else:
            rest_items += [array[i]]
    if not r_c_items:
        if r_c == 'r':
            print("No required items")
        else:
            print("No completed items")
    else:
        print("Total expected price for {} items: ${:.2f}".format(x, sum(expected_price)))
    return r_c_items + rest_items + [x]


def max_char_length(array,index):
    strings = []
    for i in range(len(array)):
        strings += [len(array[i][int(index)])]
    return max(strings)

def file_load():
    """
      #Pseudocode for loading items
     open “items.csv” as fileIn for reading
      get items data from fileIn
      put items data into list
      close fileIn
      """

    import csv
    items_list = []
    file_open = open('items.csv')
    file_read = csv.reader(file_open, delimiter=',')
    for row in file_read:
        items_list += [row]
    file_open.close()
    print("{} items loaded from items.csv".format(len(items_list)))
    return items_list

def file_save(array):
    import csv
    file_save = open('items.csv', 'w')
    for item in array:
        write = csv.writer(file_save)
        write.writerow(item)
    file_save.close()
    print("{} items saved to items.csv".format(len(array)))
def get_user_choice():
    print(
        "Menu:\nR - List required items\nC - List completed items\nA - "
        "Add new item\nM - Mark an item as completed\nQ - Quit")
    return input(">>> ")
main()
