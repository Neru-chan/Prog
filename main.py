from asyncio.windows_events import NULL


def get_action():

    print(
        "Options:\n"
        "1 - Lab 1\n"
        "Enter 'exit' to exit"
        )
    return input("Select Action: ")



s = NULL
while True:
    s = get_action()
    if s == "exit": break   

    # open another py script
    path = f"Lab{s}/task.py"
    try:
        with open(path, 'r') as file:
            py = file.read()
            exec(py)
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")

    print("Going Back...")