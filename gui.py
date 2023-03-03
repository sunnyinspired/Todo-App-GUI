import modules.functions
import PySimpleGUI as App

label = App.Text("Enter A Todo Item")
input_box = App.InputText(tooltip='Enter Todo')
add_button = App.Button("Add Todo")

layout = [
    [label], [input_box, add_button]
]

window = App.Window('Todo App', layout=layout)
window.read()
window.close()
