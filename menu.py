import sys  # system

selection = None


def run(handler):
    print(">", end=" ", flush=True)
    for input in sys.stdin:
        line = input.rstrip()
        parts = line.split(" ", 1)

        if len(parts) == 1:
            parts.append("")

        command = parts[0]
        arg = parts[1]

        if command == "quit" or command == "exit":
            break

        if command != "":
            handler(command, arg)

        if selection is not None:
            print(str(selection), end=" ")

        print(">", end=" ", flush=True)
