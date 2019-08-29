checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# LIST all items in array
def list_all_items():
    for list_item in checklist:
        index = 0
        print("{} {}".format(index, list_item))
        index += 1

#COMPLETE
def mark_completed(index, item):
    checklist.append("√" + index)
    update(index, item)
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

#SELECT
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)
    # Print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
    # This is where we want to stop our loop
        return False
    # Catch all
    else:
        print("Unknown Option")

# TEST function
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

#Run the Tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit ")
    running = select(selection)

