import os

os.system('cls')


def openRecord():

    with open('database.txt', "r") as f:
        lines = f.read()
        return lines.splitlines()


def saveRecord(tasks):

    with open('database.txt', "w") as f:
        for task in tasks:
            f.write(task + '\n')


def editTask():

    while True:

        browseTask()
        num = input(
            "\n\nInsert the number of the task you want to edit. Press enter to go back to main: ")

        if num == '':
            os.system('cls')
            main()

        tasks = openRecord()

        if not len(tasks) or not num.isdigit() or int(selection) > len(tasks):
            print("Invalid selection. Please try again.\n")
        else:
            newTask = input("Insert the new task you want to change: ")
            tasks[int(num) - 1] = newTask
            saveRecord(tasks)
            print("Task successfully edited..\n\n")


def browseTask():

    print("\n\n=================THINGS TO DO!====================\n\n")
    tasks = openRecord()

    index = 1
    for task in tasks:
        print(str(index) + ". " + task + '\n')
        index = index + 1


def arrangeOrderTask():

    while (True):
        browseTask()
        fromNum = input(
            "\n\nInsert the first number to be switched. Press enter to go back to main: ")

        if fromNum == '':
            os.system('cls')
            main()

        toNum = input("Insert the second number to be switched: ")

        if fromNum.isdigit() and toNum.isdigit():

            fromNum = int(fromNum)
            toNum = int(toNum)

            tasks = openRecord()
            if not len(tasks) or fromNum not in range(1, len(tasks)) or toNum not in range(1, len(tasks)):
                print("Invalid Selection. Please try again.\n")
            else:
                tasks[fromNum - 1], tasks[toNum -
                                          1] = tasks[toNum - 1], tasks[fromNum - 1]
                saveRecord(tasks)
                os.system('cls')
        else:
            print("Invalid selection. Please try again.\n")


def addTask():

    while True:
        browseTask()
        task = input("\n\nInsert your task. Press enter to go back to main: ")

        if task == '':
            os.system('cls')
            main()

        tasks = openRecord()
        tasks.append(task)
        saveRecord(tasks)

        print("Task added succesfully")
        os.system('cls')


def deleteTask():

    while True:
        browseTask()
        selection = input(
            "\n\nSelect the task number you want to delete. Press enter to go back to main: ")

        if selection == '':
            os.system('cls')
            main()

        tasks = openRecord()

        if not len(tasks) or not selection.isdigit() or int(selection) > len(tasks):
            print("Invalid Selection. Please try again\n")

        else:
            tasks.pop(int(selection) - 1)
            saveRecord(tasks)
            os.system('cls')


def main():

    tasks = openRecord()
    print("\n\n==================TO-DO List===================\n\n")
    print("Whats up in your mind?\n\n")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Edit Task")
    print("4. Arrange Tasks")
    print("5. Browse Tasks")
    print("6. Quit")

    choice = input("\n\nPlease make a choice: ")

    match choice:
        case '1':
            os.system('cls')
            addTask()
        case '2':
            os.system('cls')
            deleteTask()
        case '3':
            os.system('cls')
            editTask()
        case '4':
            os.system('cls')
            arrangeOrderTask()
        case '5':
            os.system('cls')
            browseTask()
            input("Press enter to go back to main menu.")
            os.system('cls')
            main()
        case _:
            os.system('cls')
            quit()


if __name__ == "__main__":
    main()
