def main():
    import csv
    items_list = []
    file_open = open('items.csv')
    with file_open as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            items_list += [row]
    file_open.close()
    choice = ""

    while choice.upper() != "Q":
        print(
            "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark an item as completed\nQ - Quit")

        choice = input(">>> ")

        if choice.upper() == "A":
            name = input("Item name: ")
            price = float(input("Price: $"))
            priority = int(input("Priority (1 - 3, 1 being high): "))

            items_list += [[name, price, priority, 'r']]
            print("{}, ${:.2f} (priority {}) added to shopping list".format(name, price, priority))

        else:
            print("Invalid menu choice")

    file_save = open('items.csv', 'w', newline='')
    with file_save as csvfile:
        for i in items_list:
            write = csv.writer(file_save)
            write.writerow(i)
    file_open.close()
    print("{} items saved to items.csv".format(len(items_list)))
    print("Have a nice day :)")

main()