from tkinter import *
from tkinter import Tk
from math import sqrt

# Cores
operacoes = "#323232"
numeros = "#3b3b3b"
igual = "#841a9b"
fundo = "#282a36"
cdisplay = '#202020'
letras = "#FFF"

# Criando janela da calculadora
app = Tk()
app.title('Calculadora')
app.geometry('240x385')
app.config(bg=fundo)
app.resizable(False, False)

# Criando frames da janela
display = Frame(app, width=240, height=80, bg=cdisplay)
display.place(x=0, y=0)

body = Frame(app, width=240, height=325, bg=fundo)
body.place(x=0, y=73)

all_values = ''
text_value = StringVar()


# Função para mostrar os valores no display
def enter_values(entry):
    global all_values
    all_values = all_values + str(entry)
    text_value.set(all_values)


# Função para calcular
def calc():
    global all_values
    global text

    text = all_values

    # Fazendo mudança para melhoras estetica na raiz quadrada e potência
    if '√' in text:
        text = text.replace('√', 'sqrt(')
        text = text + ')'

    if '^' in text:
        text = text.replace('^', '**')

    try:
        result = eval(text)
        text_value.set(str(result))
        all_values = str(result)

    except:
        clearScreen()


# Função para limpar a tela
def clearScreen():
    global all_values
    all_values = ''
    text_value.set('')


# Função para deletar apenas um caractere
def delet():
    global all_values
    all_values = all_values[:-1]
    text_value.set(all_values)


# Lugar onde os número vão aparecer
displayLabel = Label(display, textvariable=text_value, width=16, height=2, relief=FLAT,
                     anchor='e', justify=CENTER, font=('Ivy 18'), bg=cdisplay, fg=letras)
displayLabel.place(x=0, y=0)


# Criando Botões
button_C = Button(body, command=clearScreen, text='C', width=11, height=2, padx=1,
                  bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_C.place(x=0, y=0)


button_rest = Button(body, command=lambda: enter_values('√'), text='√', width=5, height=2,
                     padx=1, bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_rest.place(x=120, y=0)


button_pow = Button(body, command=lambda: enter_values('^'), text='^', width=5, height=2,
                    padx=1, bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_pow.place(x=180, y=0)


button_7 = Button(body, command=lambda: enter_values('7'), text='7', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_7.place(x=0, y=52)


button_8 = Button(body, command=lambda: enter_values('8'), text='8', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_8.place(x=60, y=52)


button_9 = Button(body, command=lambda: enter_values('9'), text='9', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_9.place(x=120, y=52)


button_div = Button(body, command=lambda: enter_values('/'), text='/', width=5, height=2,
                    padx=1, bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_div.place(x=180, y=52)


button_4 = Button(body, command=lambda: enter_values('4'), text='4', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_4.place(x=0, y=104)


button_5 = Button(body, command=lambda: enter_values('5'), text='5', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_5.place(x=60, y=104)


button_6 = Button(body, command=lambda: enter_values('6'), text='6', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_6.place(x=120, y=104)


button_mult = Button(body, command=lambda: enter_values('*'), text='*', width=5, height=2,
                     padx=1, bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_mult.place(x=180, y=104)


button_1 = Button(body, command=lambda: enter_values('1'), text='1', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_1.place(x=0, y=156)


button_2 = Button(body, command=lambda: enter_values('2'), text='2', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_2.place(x=60, y=156)


button_3 = Button(body, command=lambda: enter_values('3'), text='3', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_3.place(x=120, y=156)


button_sub = Button(body, command=lambda: enter_values('-'), text='-', width=5, height=2,
                    padx=1, bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_sub.place(x=180, y=156)


button_parenL = Button(body, command=lambda: enter_values('('), text='(', width=5, height=2,
                       padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_parenL.place(x=0, y=208)


button_pareR = Button(body, command=lambda: enter_values(')'), text=')', width=5, height=2,
                      padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_pareR.place(x=60, y=208)


button_3 = Button(body, command=lambda: enter_values('0'), text='0', width=5, height=2,
                  padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_3.place(x=120, y=208)


button_sub = Button(body, command=lambda: enter_values('+'), text='+', width=5, height=2,
                    padx=1, bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_sub.place(x=180, y=208)


button_del = Button(body, command=delet, text='DEL', width=5, height=2, padx=1,
                    bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_del.place(x=0, y=260)


button_porc = Button(body, command=lambda: enter_values('%'), text='%', width=5, height=2,
                     padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_porc.place(x=60, y=260)


button_point = Button(body, command=lambda: enter_values('.'), text='.', width=5, height=2,
                      padx=1, bg=numeros, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_point.place(x=120, y=260)


button_equal = Button(body, command=calc, text='=', width=5, height=2, padx=1,
                      bg=operacoes, fg=letras, font=('Ivy 13 bold'), relief=RAISED, overrelief=SUNKEN)
button_equal.place(x=180, y=260)

app.mainloop()
