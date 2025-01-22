from database import create_tables
from function import ls, insert, delete, search, update, get

create_tables()

if __name__ == "__main__":
    while True:
        command = input("sieuthixu.com: ")
        if not command:
            continue
        split_commands = command.split()
        match split_commands[0]:
            case 'ls':
                if len(split_commands)==1:
                    ls()
                else:
                    split_commands.pop(0)
                    ls(split_commands)
            case 'insert':
                if len(split_commands)==1:
                    insert()
                else:
                    split_commands.pop(0)
                    insert(split_commands)
            case 'delete':
                if len(split_commands)==1:
                    delete()
                else:
                    split_commands.pop(0)
                    delete(split_commands)
            case 'search':
                if len(split_commands)==1:
                    search()
                else:
                    split_commands.pop(0)
                    search(split_commands)
            case 'update':
                if len(split_commands)==1:
                    update()
                else:
                    split_commands.pop(0)
                    update(split_commands)
            case 'get':
                if len(split_commands)==1:
                    get()
                else:
                    split_commands.pop(0)
                    get(split_commands)
            case _:
                print("command not found")
