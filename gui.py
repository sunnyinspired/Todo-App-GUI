import modules.functions as fn
import PySimpleGUI as App

label = App.Text("Enter A Todo Item")
input_box = App.InputText(tooltip='Enter Todo', key="todo")
add_button = App.Button("Add Todo")
list_box = App.Listbox(values=fn.get_todos(), key="todos", enable_events=True,
                       size=(45, 10))
edit_button = App.Button("Edit Todo")

layout = [
    [label], [input_box, add_button], [list_box, edit_button]
]

window = App.Window('Todo App', layout=layout, font=("Ubuntu", 14))
while True:
    event, value = window.read()
    print(event)
    print(value)
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
            todo_to_edit = value["todos"][0]

            new_todo = value['todo']+"\n"

            todos = fn.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            fn.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case App.WIN_CLOSED:
            break

window.close()
