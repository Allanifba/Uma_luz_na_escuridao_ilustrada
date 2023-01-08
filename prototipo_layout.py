'''
(1) Parte referente ao layout do livro-jogo, Uma luz na escuridão
(2) Há um pequeno bug ao fechar a janela no 'x'. Neste caso deve-se apertar 'Stop' nesta janela logo após. Fechar a
janela apertando o botão 'Exit' está funcionando normalmente. Recomendamos o uso do arquivo
'Uma_luz_na_escuridao_ilustrada.py' para entender o layout. Nesta janela estão somente os elementos do layout sem
qualquer funcionalidade, exceto, o botão 'Exit'.
(3) Caso esteja rodando pela primeira vez este programa use o terminal para instalar a biblioteca PySimpleGUI por
meio do comando pip install PySimpleGUI.
'''

import PySimpleGUI as sg

layout = [
            [sg.Text('Aventura Solo: Uma Luz na Escuridão \n'               #Texto do Cabeçalho
                     'Aperte "Tutorial" para começar.')],
            [sg.Output(size=(110,25),font='Times 12 italic bold'),          #Campo onde a história é contada
            sg.Image(filename='image.png',key='image.png',visible=True)],   #Campo onde aparece a imagem
            [sg.Text('Escolhas: ')],                                        #Texto abaixo dos campos anteriores
            [sg.Input(key='-IN-', do_not_clear=True)],                      #Campo para o usuário inserir dados
            [sg.Button('Seguir', bind_return_key=True, key='Seguir',visible=True), #Botões do jogo
             sg.Button('Inventário',bind_return_key=True),
             sg.Button('Caminho',bind_return_key=True),
             sg.Button('Tutorial',bind_return_key=True),
             sg.Button('Exit',bind_return_key=True)]
]

window = sg.Window('Aventura Solo', layout)     #Criação de uma janela de interface gráfica do usuário (GUI)

event=0     #Um valor incial atribuído à variável que armazena as escolhas

while event != 'Exit':                     #Condição para que a janela aberta com o comando interno fique aberta
    event, values = window.read()          #Carrega a janela

# Programação dos eventos e funções dos botões vai está aqui....
window.close()

'''
Explicações:
(1) PySimpleGUI é uma biblioteca de interface gráfica do usuário (GUI) para Python que permite ao usuário criar 
aplicativos de GUI de forma rápida e fácil. Ela é baseada em outra biblioteca chamada Tkinter e oferece uma interface 
de alto nível para criar janelas, botões, menus e outros elementos da interface gráfica do usuário. PySimpleGUI é 
compatível com Python 2 e Python 3 e pode ser usada em sistemas operacionais como Windows, Linux e macOS.
(2) O comando "bind_return_key" é usado para atribuir uma função ou método a ser chamado quando a tecla "Enter" é 
pressionada em um elemento de interface de usuário (UI) do PySimpleGUI.
(3) O comando do_not_clear é um parâmetro opcional que pode ser usado com a função print do PySimpleGUI. Quando esse 
parâmetro é definido como True, o conteúdo da caixa de saída (output) não é limpo antes de imprimir o novo texto. 
Isso significa que o novo texto será adicionado ao final do conteúdo já existente na caixa de saída, em vez de 
substituí-lo.
(4) O parâmetro key é um parâmetro opcional que pode ser usado ao criar elementos de interface de usuário (UI) com o 
PySimpleGUI. Ele serve para atribuir uma chave única ao elemento, que pode ser usada posteriormente para acessar o 
valor deste elemento.
(5) No caso específico da chave '-IN-', ela é usada para criar uma caixa de entrada de texto, que é um elemento UI 
onde o usuário pode digitar um texto. A chave '-IN-' é apenas uma das chaves pré-definidas que podem ser usadas para 
criar elementos de entrada de texto. Outras opções incluem '-IN_L-', '-IN_R-' e '-IN_M-', que criam caixas de entrada 
alinhadas à esquerda, à direita e no centro, respectivamente.
'''
