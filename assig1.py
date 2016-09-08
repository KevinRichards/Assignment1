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
    choice = get_user_choice()
    while choice.upper() != "Q":

        if choice.upper() == "A":
            name = get_item_name()
            price = get_item_price()
            priority = get_item_priority()
            items_list.append([name, str(price), str(priority), 'r'])  # puts item details into array then add to list
            print("{}, ${:.2f} (priority {}) added to shopping list".format(name, price, priority))

        elif choice.upper() == "C":
            print("Completed items:")
            display_items(items_list, 'c')  # function to sort array for completed items

        elif choice.upper() == "R":
            print("Required items:")
            display_items(items_list, 'r')  # function to sort array for required items

            """
            Pseudocode for setting item as complete
            if menu_choice = M
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
            items_list = display_items(items_list, 'r')  # function to sort array for required items
            print(items_list)
            if items_list[-1] != 0:  # checks if any required items in items list
                complete_item = get_item_to_complete(items_list)
                items_list[int(complete_item)][3] = 'c'  # sets item to completed
                items_list = items_list[
                             0:-1]  # resizes items list to remove last item which stores number of required items within the list
                print("{} marked as completed".format(items_list[int(complete_item)][0]))
        else:
            print("Invalid menu choice")
        choice = get_user_choice()

    file_save(items_list)
    print("Have a nice day :)")


# gets and error checks item name from user
def get_item_name():
    name = input("Item name: ")
    while name == "":  # check if name has been entered
        print("Input can not be blank")
        name = input("Item name: ")
    return name


# gets and error checks index of item to set as complete from user
def get_item_to_complete(items_list):
    print("Enter the number of an item to mark as completed")
    finished = False
    while not finished:
        try:
            item_index_to_complete = int(input(">>> "))
            0 <= item_index_to_complete < items_list[
                -1]  # evaluates if user enter is within required items range of list
            finished = True
        except ValueError:
            print("Invalid input; enter a number")
        except:
            print("Invalid item number")
    return item_index_to_complete


# gets and error checks item priority from user
def get_item_priority():
    finished = False
    while not finished:
        try:
            priority = int(input("Priority (1 - 3, 1 being high): "))
            1 <= priority <= 3  # evaluates if user entered priority is within 1 and 3
            priority != ""
            finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
        except:
            print("Priority must be 1, 2 or 3")
    return priority


# gets and error checks item price from user
def get_item_price():
    finished = False
    while not finished:
        try:
            price = float(input("Price: $"))
            price >= 0  # evaluates if price is $0 or more
            price != ""
            finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
        except:
            print("Price must be >=$0")
    return price


# sorts items in list by required or completed, then displays the required or completed items and their combined price
def display_items(items_list, display_items_r_or_c):
    from operator import itemgetter
    items_list.sort(key=itemgetter(2))  # function to sort array in terms of priority of each item
    displayed_items = []
    rest_items = []
    expected_price = []
    display_items_count = 0  # number of display items in list
    format_name_length = longest_string_in_array(items_list, 0)  # function to find spacing required in formatting
    format_cost_length = longest_string_in_array(items_list, 1) + 1  # +1 to accommodate for displaying 2 decimals
    for i in range(len(items_list)):
        if items_list[i][-1] == display_items_r_or_c:  # checks if item is required or completed
            print(
                "{}. {:{}}    $ {:{}.2f} ({})".format(display_items_count, items_list[i][0], int(format_name_length),
                                                      float(items_list[i][1]), int(format_cost_length),
                                                      items_list[i][2]))  # prints each item as added to items list
            displayed_items += [items_list[i]]
            expected_price.append(float(items_list[i][1]))
            display_items_count += 1
        else:
            rest_items.append([items_list[i]])
    if not displayed_items:
        if display_items_r_or_c == 'r':
            print("No required items")
        else:
            print("No completed items")
    else:
        print("Total expected price for {} items: ${:.2f}".format(display_items_count, sum(expected_price)))
    return displayed_items + rest_items + [
        display_items_count]  # returns list with all display items(required or completed items)
    # at the top then the rest items (vice versa), then the number of display items as an index reference outside the function


# Finds length of longest string in array for print formatting
def longest_string_in_array(array, index):
    strings = []
    for i in range(len(array)):
        strings.append(len(array[i][int(index)]))
    return max(strings)


# Loads items list file and puts into list array
def file_load():
    """
      #Pseudocode for loading items
    open “items.csv” as file for reading
      read items data from file
      for each row of file
        add to items list
      display len(items list)
      close file
      """

    import csv
    items_list = []
    file_open = open('items.csv')
    file_read = csv.reader(file_open)  # delimiter stops reader from adding blank
    # array between each item read in list (was researched)
    for row in file_read:
        items_list.append(row)
    file_open.close()
    print("{} items loaded from items.csv".format(len(items_list)))
    return items_list


# Writes items from list to file
def file_save(items_list):
    import csv
    file_save = open('items.csv', 'w', newline='')
    for item in items_list:
        write = csv.writer(file_save)
        write.writerow(item)
    file_save.close()
    print("{} items saved to items.csv".format(len(items_list)))


# display menu options and get user choice
def get_user_choice():
    print(
        "Menu:\nR - List required items\nC - List completed items\nA - "
        "Add new item\nM - Mark an item as completed\nQ - Quit")
    return input(">>> ")


main()
