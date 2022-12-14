# 11/11/2022 -> 11/12/2022
name = []
contact_Number = []
address = []
date_of_Entry = []


def fileNaming(data, type):
    if type == "Input":
        y = " "
        for i in y:
            # means to remove the character -> youtube lol
            data = data.replace(i, "-")
            return data
    elif type == "File":
        y = "-"
        for i in y:
            # means to remove the character -> youtube lol
            data = data.replace(i, " ")
            return data


def delete(data, type):
    # Accessing the global variables and manipulate its data
    global name, contact_Number, address, date_of_Entry
    if type == "Name":
        position = name.index(data)  # Locate the data to delete
        # Deleting data
        name.remove(name[position])
        contact_Number.remove(contact_Number[position])
        address.remove(address[position])
        date_of_Entry.remove(date_of_Entry[position])
    elif type == "Date":
        for i in range(date_of_Entry.count(data)):  # counts how many data to delete
            position = date_of_Entry.index(data)  # locate the data to delete
            # deleting data
            name.remove(name[position])
            contact_Number.remove(contact_Number[position])
            address.remove(address[position])
            date_of_Entry.remove(date_of_Entry[position])


def deleteByDate():
    if showEntries():
        print("")
        data = input("Enter a Date to delete: ")
        # calling a function to delete with two parameters as 'data' and 'type' respectively
        if name.count(data) != 0:
            delete(data, "Date")
            print("Data successfully deleted!")
        else:
            print("")
            print("----Date not found----")


def displayMenu():
    print("WELCOME TO CONTACT TRACING APP!")
    print("[1] Add Entry")
    print("[2] Delete Entry")
    print("[3] Delete Entry by Date")
    print("[4] Find Entry")
    print("[5] Find Entries by Date")
    print("[6] Show Entry")
    print("[0] EXIT")


def addEntry():
    print("")
    strContainer = ""
    # Accessing the global variables and manipulate its data
    global name, contact_Number, address, date_of_Entry, fileName

    strContainer = str(input("Enter name: "))
    name.append(strContainer)  # Putting the data to a list variable

    strContainer = str(input("Enter contact number: "))
    contact_Number.append(strContainer)  # Putting the data to a list variable

    strContainer = str(input("Enter address: "))
    address.append(strContainer)  # Putting the data to a list variable

    strContainer = str(input("Enter date of entry(MM/DD/YYYY): "))
    date_of_Entry.append(strContainer)  # Putting the data to a list variable
    print("Data Successfully Added!")


def deleteEntry():
    if showEntries():
        data = input("Enter a name to delete: ")
        if name.count(data) != 0:
            delete(data, "Name")
            print("Data successfully deleted!")
        else:
            print("")
            print("----Name not found----")


def showEntries():
    print("")
    if name == []:
        print("----The list is empty----")
        checker = False
    else:
        checker = True
        for i in range(len(name)):
            print(
                f"{date_of_Entry[i]}, {name[i]} from {address[i]}, contact at {contact_Number[i]} ")

        print("")
    return checker


def findEntry():
    print("")
    if name == []:
        print("----The list is empty----")
    else:
        username = str(input("Enter a name to access its record: "))
        x = name.count(username)
        if x != 0:
            y = name.index(username)
            print(
                f"\n{date_of_Entry[y]}, {name[y]} from {address[y]}, contact at {contact_Number[y]}")
        else:
            print("")
            print("----Name not found----")


def findEntriesByDate():
    print("")
    if date_of_Entry != []:
        date = str(input("Enter date of entry: "))
        if date_of_Entry.count(date) != 0:
            print("")
            for i in range(len(date_of_Entry)):  # counts how many data to delete
                if date_of_Entry[i] == date:
                    print(
                        f"{date_of_Entry[i]}, {name[i]} from {address[i]}, contact at {contact_Number[i]} ")
        else:
            print("")
            print("----Date not found----")
    else:
        print("----The list is empty----")


def loadFile():
    x = []
    file = (open("database.txt", "r"))
    for data in file:
        line_strip = data.strip()
        line_split = line_strip.split()
        x.append(line_split)
    for i in range(len(x)):
        j = 0
        date_of_Entry.append(x[i][j])
        j += 1
        name.append(fileNaming(x[i][j], "File"))
        j += 1
        address.append(fileNaming(x[i][j], "File"))
        j += 1
        contact_Number.append(x[i][j])
        j = 0
    file.close()


def saveFile():
    file = (open("database.txt", "w"))

    for i in range(len(name)):
        file.write(
            f"{date_of_Entry[i]} {fileNaming(name[i], 'Input')} {fileNaming(address[i], 'Input')} {contact_Number[i]}\n")
    file.close()


# Main
loadFile()
while True:
    displayMenu()
    entryChoice = str(input("Enter choice: "))

    if entryChoice == '1':
        addEntry()
    elif entryChoice == '2':
        deleteEntry()
    elif entryChoice == '3':
        deleteByDate()
    elif entryChoice == '4':
        findEntry()
    elif entryChoice == '5':
        findEntriesByDate()
    elif entryChoice == '6':
        showEntries()
    elif entryChoice == '0':
        print("------------END--------------")
        break
    else:
        print(f"\n{entryChoice}...? You blind or something?")
    print("")
    input("Enter anything to continue >> ")
    print("")
saveFile()
