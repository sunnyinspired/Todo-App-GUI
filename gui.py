import modules.functions as fn
import PySimpleGUI as App
import time

clock = App.Text('', key="clock", font=("Helvetica", 14))
label = App.Text("Enter A Todo Item")
input_box = App.InputText(tooltip='Enter Todo', key="todo")
add_button = App.Button("Add Todo")
list_box = App.Listbox(values=fn.get_todos(), key="todos", enable_events=True,
                       size=(45, 10))
edit_button = App.Button("Edit Todo")
delete_button = App.Button("Delete Todo")
exit_button = App.Button("Exit")

layout = [
    [clock], [label], [input_box, add_button], [list_box, edit_button, delete_button], [exit_button]
]

window = App.Window('Todo App', layout=layout, font=("Ubuntu", 14))
while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b-%m-%Y %H:%M:%S"))
    match event:
        case "Add Todo":
            todos = fn.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            # write the new todos to file
            fn.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit Todo":
            try:
                todo_to_edit = value["todos"][0]

                new_todo = value['todo']+"\n"

                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                fn.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                App.popup("Please select a Todo", font=("Helvetica", 14))
        case "Delete Todo":
            try:
                todo_to_delete = value["todos"][0]
                todos = fn.get_todos()
                todos.remove(todo_to_delete)

                fn.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                App.popup("Please select a Todo", font=("Helvetica", 14))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case App.WIN_CLOSED:
            break

window.close()
