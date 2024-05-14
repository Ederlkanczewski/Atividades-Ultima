import PySimpleGUI as sg

def criar_janela_tarefa():
    sg.theme('darkblue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarfas', layout=linha,key='contanier')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]
    return sg.Window('todo list',layout=layout,finalize=True)

janela = criar_janela_tarefa()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa' :
        janela.extend_layout(janela['contanier'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Reset':
        janela.close()
        janela = criar_janela_tarefa()


