checklist = list()
# CREATE
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index +=1

def create(item):
    checklist.append(item)

    # READ
def read(index):
    index = int(index)
    item = checklist[index]
    print(item)

    # UPDATE
def update(index, item):
    checklist[index] = item
    # DESTROY
def destroy(index):
    checklist.pop(index)

def mark_completd(index):
     print("{} {}".format (indx, list_item))


def select(function_code):
    if function_code == "c":
        input_item = input("input item:")
        create(input_item)
    elif function_code == "r":
        item_index = input("index number")
        read(item_index)
    elif function_code =="p":
        list_all_items()
    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    else:
        #Catch all
        print("Unknown Option")
    return True


def test():
    create("purple sox")
    create("red cloak")

    (read(0))
    (read(1))

    update(0, "purple socks")
    destroy(1)

    (read(0))

    select("c")
    list_all_items()
    select("r")
    list_all_items()
running = True
while running:
    selection = input(
        "Press C to add to list, R to Read from list and P to display list")
    running = select(selection)
