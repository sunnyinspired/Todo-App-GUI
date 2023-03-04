import modules.functions as fn
import PySimpleGUI as App

label = App.Text("Enter A Todo Item")
input_box = App.InputText(tooltip='Enter Todo', key="todo")
add_button = App.Button("Add Todo")

layout = [
    [label], [input_box, add_button]
]

window = App.Window('Todo App', layout=layout, font=("cambria", 14))
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
        case App.WIN_CLOSED:
            break

window.close()
