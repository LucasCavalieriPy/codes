import sqlite3
import random
import qrcode
import string
import datetime
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
from customtkinter.windows import *

conn = sqlite3.connect('bancomain.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS codigosV (id integer PRIMARY KEY AUTOINCREMENT, codigoValido VARCHAR(8), dataHora VARCHAR(17), nomeVendedor VARCHAR(50), nomeCliente VARCHAR(50), emailCliente VARCHAR(50), numeroCliente VARCHAR(11), valor VARCHAR (10))")

print('banco de dados ok')



def botaomain1():
    def focus_top():
        top.lift()
        root.after(500, focus_top)
    top = ctk.CTkToplevel(root)
    top.title('Gerar QrCode')
    top.attributes('-topmost', True)
    top.resizable(False, False)

    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    x = (screen_width // 2) - (700 // 2)
    y = (screen_height // 2) - (900 // 2)
    top.geometry(f"700x900+{x}+{y}")

def botaomain2():
    def focus_top():
        top.lift()
        root.after(500, focus_top)
    top = ctk.CTkToplevel(root)
    top.title('Buscar QrCode')
    top.attributes('-topmost', True)
    top.resizable(False, False)

    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    x = (screen_width // 2) - (700 // 2)
    y = (screen_height // 2) - (900 // 2)
    top.geometry(f"700x900+{x}+{y}")
def botaomain3():
    def focus_top():
        top.lift()
        root.after(500, focus_top)

    def botaocompra():
        global codigo_entry, valor_entry, valor_entry2
        top = ctk.CTkToplevel(root)
        top.title('Compra / Depósito')
        top.attributes('-topmost', True)
        top.resizable(False, False)

        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = (screen_width // 2) - (700 // 2)
        y = (screen_height // 2) - (900 // 2)
        top.geometry(f"700x900+{x}+{y}")

        valor_label = ctk.CTkLabel(top, text="Valor:", font=('arial', 18))
        valor_label.place(x=90, y=410)
        valor_entry = ctk.CTkEntry(top, font=('arial', 18), width=80, height=50)
        valor_entry.place(x=140, y=400)

        botaocompra_top = ctk.CTkButton(top, text="Compra", width=100, height=50, font=('arial', 22),command=compra)
        botaocompra_top.place(x=230, y=400)

        valor_label2 = ctk.CTkLabel(top, text="Valor:", font=('arial', 18))
        valor_label2.place(x=90, y=510)
        valor_entry2 = ctk.CTkEntry(top, font=('arial', 18), width=80, height=50)
        valor_entry2.place(x=140, y=500)

        botaodeposito_top = ctk.CTkButton(top, text="Depósito", width=100, height=50, font=('arial', 22),command=deposito)
        botaodeposito_top.place(x=230, y=500)

        codigo_label = ctk.CTkLabel(top, text="Código:", font=('arial', 18))
        codigo_label.place(x=75, y=160)
        codigo_entry = ctk.CTkEntry(top, font=('arial', 18), width=80, height=50)
        codigo_entry.place(x=140, y=150)

        botaobusca_top = ctk.CTkButton(top, text="Buscar", width=100, height=50, font=('arial', 22),command=verificarcodigo)
        botaobusca_top.place(x=230, y=150)






    def botaomain3():
        def focus_top():
            top.lift()
            root.after(500, focus_top)

        focus_top()
        botaocompra()

    top = ctk.CTkToplevel(root)
    top.title('Compra / Depósito')
    top.attributes('-topmost', True)
    top.resizable(False, False)

    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    x = (screen_width // 2) - (700 // 2)
    y = (screen_height // 2) - (900 // 2)
    top.geometry(f"700x900+{x}+{y}")

    botaocompra_main = ctk.CTkButton(root, text="Compra / Depósito", width=300, height=50, command=botaocompra,font=('arial', 22))
    botaocompra_main.place(x=200, y=600)


ctk.set_appearance_mode("dark")

root = ctk.CTk ()
root.title("beta")
root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (700 // 2)
y = (screen_height // 2) - (900 // 2)

root.geometry(f"700x900+{x}+{y}")

botaomain1 = ctk.CTkButton(root, text="Gerar QrCode", width=300, height=50, command=botaomain1,font=('arial', 22))
botaomain1.place(x=200, y=200)

botaomain2 = ctk.CTkButton(root, text="Buscar QrCode", width=300, height=50, command=botaomain2,font=('arial', 22))
botaomain2.place(x=200, y=400)

botaomain3 = ctk.CTkButton(root, text="Compra / Depósito", width=300, height=50, command=botaomain3,font=('arial', 22))
botaomain3.place(x=200, y=600)








def informacoes():
    #coleta informacoes como horas, valor nome e etc
    data = datetime.datetime.now()
    dataSimples = data.strftime('%d/%m/%Y %H:%M')
    print(dataSimples)

    vendedor = input('vendedor: ')
    cliente = input('cliente: ')

    while True:
        email = input('email: ')
        if "@gmail.com" in email:
            print('email OK')
            break
        else:
            print("E-mail inválido. Por favor, insira um e-mail válido com '@gmail.com'.")
            continue  # Solicita novamente a entrada do usuário

    while True:
        numeroTel = input('numero Tel: ')
        if numeroTel.isdigit():
            print("Número válido.")
            break
        else:
            print("Número inválido. Por favor, insira apenas números.")
            continue

    valor = input('valor: ')
    QRcode = 1
    code = 8

    for x in range(QRcode):
        CodigoFinal = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(code)))

        print(CodigoFinal)

    cursor.execute("SELECT * FROM codigosV WHERE codigoValido=?", (CodigoFinal,))
    row = cursor.fetchone()
    if row is not None:
        print('codigo ja existe tente novamente')
    else:
        img = qrcode.make(CodigoFinal)
        img.save("Codigo de teste .png")  # Salva a imagem do QRCode em um arquivo

        cursor.execute("INSERT INTO codigosV (codigoValido, dataHora, nomeVendedor, nomeCliente, emailCliente, numeroCliente, valor) VALUES (?, ?, ?, ?, ?, ?, ?)", (CodigoFinal, dataSimples, vendedor, cliente, email, numeroTel, valor))


    conn.commit()  # Confirma a transação no banco de dados

def verificarcodigo():
    global bcValor,buscarCodigo
    buscarCodigo = codigo_entry.get()
    cursor.execute("SELECT nomeCliente, valor FROM codigosV WHERE codigoValido=?", (buscarCodigo,))
    row = cursor.fetchone()
    if row is not None:
        print("Código encontrado")
        nomeCliente = row[0]
        bcValor = row[1]
        print("Nome do cliente:", nomeCliente)
        print("Valor: R$", bcValor)
        codigo_entry.delete(0,'end')
    else:
        print("Código não encontrado.")

def compra():
    '''buscarCodigo = valor_entry.get()
    cursor.execute("SELECT nomeCliente, valor FROM codigosV WHERE codigoValido=?", (buscarCodigo,))
    row = cursor.fetchone()
    if row is not None:
        print("Código encontrado")
        nomeCliente = row[0]
        bcValor = row[1]
        print("Nome do cliente:", nomeCliente)
        print("Valor: R$", bcValor)
    else:
        print("Código não encontrado.")
        return'''
    global bcValor,buscarCodigo
    descontarValor = valor_entry.get()
    bcValor = bcValor.replace(',', '.')
    descontarValor = descontarValor.replace(',', '.')
    valorDescontado = (float(bcValor) - float(descontarValor))
    if valorDescontado <= float('0'):
        print(f'nao há saldo o suficiente, saldo atual:{bcValor}')
    else:
        print("Valor após desconto: R$", valorDescontado)
        cursor.execute("UPDATE codigosV SET valor=? WHERE codigoValido=?", (valorDescontado, buscarCodigo))
        valor_entry.delete(0,'end')
        conn.commit()

def deposito():
    '''buscarCodigo = inputCodigo
    cursor.execute("SELECT nomeCliente, valor FROM codigosV WHERE codigoValido=?", (buscarCodigo,))
    row = cursor.fetchone()
    if row is not None:
        print("Código encontrado")
        nomeCliente = row[0]
        bcValor = row[1]
        print("Nome do cliente:", nomeCliente)
        print("Valor: R$", bcValor)
    else:
        print("Código não encontrado.")
        return'''
    global bcValor,buscarCodigo
    depositarValor = valor_entry2.get()
    bcValor = bcValor.replace(',', '.')
    depositarValor = depositarValor.replace(',', '.')
    valorDepositado = (float(bcValor) + float(depositarValor))
    cursor.execute("UPDATE codigosV SET valor=? WHERE codigoValido=?", (valorDepositado, buscarCodigo))
    print('valor após depóstio',valorDepositado)
    valor_entry2.delete(0, 'end')
    conn.commit()

'''def main():
    mainPage = input('compra[1]\ndeposito[2]')
    if mainPage == '1':
        compra()
    if mainPage == '2':
        deposito()'''

'''while True:
    menu = input ('gerar giftcard [1]\nverificar codigo[2]\nsistema[3]')
    if menu == '1':
        informacoes()
    if menu == '2':
        verificarcodigo()
    if menu == '3':
        main()
    if menu == 'sair':
        break'''


root.mainloop()

'''cursor.execute("SELECT * FROM codigosV")

resultados = cursor.fetchall()

for row in resultados:
    print(row)'''

conn.close()  # Fecha a conexão com o banco de dados
