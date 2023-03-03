def get_todos(filepath="data/todos.txt"):
    """ This function gets the todos from a text file """
    with open(filepath, 'r') as fl:
        td = fl.readlines()
        return td


def write_todos(td, filepath="data/todos.txt"):
    """ This function writes a new todo item to the text file """
    with open(filepath, 'w') as fl:
        fl.writelines(td)
