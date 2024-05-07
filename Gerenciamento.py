from tkinter import Frame
from tkinter.ttk import Scrollbar

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

import mysql.connector
banco = mysql.connector.connect(
    host="roundhouse.proxy.rlwy.net",
    port="43194",
    user="root",
    passwd="NSfPGnljoKKvaIyqhWhoICbrkfBQHZPA",
    database="railway"
)



def func_limpar():
    idd.delete(0, END)
    cod.delete(0, END)
    prod.delete(0, END)
    prec.delete(0,END)
    quant.delete(0, END)
    ger.delete(0, END)
    gcod.delete(0, END)
    gprod.delete(0, END)
    gprec.delete(0, END)
    gquant.delete(0, END)
def func_cadastro():
    cod1 = cod.get()
    prod1 = prod.get()
    prec1 = prec.get()
    quant1 = quant.get()

    print(cod1)
    print(prod1)
    print(prec1)
    print(quant1)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,produto,preco, quantidade) VALUES (%s,%s,%s, %s)"
    dados = (str(cod1), str(prod1), str(prec1), str(quant1))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    lista_produtos.delete(*lista_produtos.get_children())
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    for i in dados_lidos:
        lista_produtos.insert("", END, values=i)
    func_limpar()

def duplo_clique(n):
    func_limpar()
    lista_produtos.selection()

    for n in lista_produtos.selection():
        col1, col2, col3, col4, col5 = lista_produtos.item(n, 'values')
        idd.insert(END, col1)
        gcod.insert(END, col2)
        gprod.insert(END, col3)
        gprec.insert(END, col4)
        gquant.insert(END, col5)

def apagar_registro():
    idd1 = idd.get()
    cod1 = cod.get()
    prod1 = prod.get()
    prec1 = prec.get()
    quant1 = quant.get()
    valor_id = idd1

    cursor = banco.cursor()
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))
    banco.commit()
    lista_produtos.delete(*lista_produtos.get_children())
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    for i in dados_lidos:
        lista_produtos.insert("", END, values=i)
    func_limpar()


def atualizar_estoque():
    idd1 = idd.get()
    cod1 = gcod.get()
    prod1 = gprod.get()
    prec1 =gprec.get()
    quant1 = gquant.get()
    atualiza = ger.get()
    valor_id = idd1
    soma = (int(quant1) + int(atualiza))
    quantidade_atual = (str(soma))

    cursor = banco.cursor()
    cursor.execute(
        "UPDATE produtos SET codigo = '{}', produto = '{}', preco = '{}', quantidade = '{}' WHERE id = {}".format(
            cod1, prod1, prec1, quantidade_atual, idd1))
    banco.commit()
    lista_produtos.delete(*lista_produtos.get_children())
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    for i in dados_lidos:
        lista_produtos.insert("", END, values=i)
    func_limpar()




app = ttk.Window("Cadastro")
app.geometry("650x610")
style = Style(theme="solar")



abas = ttk.Notebook(app)
aba1 = Frame(abas)
aba2 = Frame(abas)
aba3 = Frame(abas)

abas.add(aba1, text="Cadastro")
abas.add(aba2, text="Lista")
abas.add(aba3, text="Gestão de Estoque")
abas.place(relx= 0, rely= 0, relwidth=0.98, relheight=0.98)

label = ttk.Label(aba1, text="Cadastro de Produtos")
label.pack(pady=35)
label.config(font=("Arial", 20, "bold"))

id = ttk.Frame(aba3)
id.pack(pady=25)
ttk.Label(id, text="ID").pack(side=LEFT, padx=30)
idd = ttk.Entry(id)
idd.pack(side=LEFT, fill="x", expand=TRUE, padx=5)

codigo = ttk.Frame(aba1)
codigo.pack(pady=25)
ttk.Label(codigo, text="Código").pack(side=LEFT, padx=25)
cod = ttk.Entry(codigo)
cod.pack(side=LEFT, fill="x", expand=TRUE, padx=15)

produto = ttk.Frame(aba1)
produto.pack(pady=25)
ttk.Label(produto, text="Produto").pack(side=LEFT, padx=25)
prod = ttk.Entry(produto)
prod.pack(side=LEFT, fill="x", expand=TRUE, padx=10)

preco = ttk.Frame(aba1)
preco.pack(pady=25)
ttk.Label(preco, text="Preço").pack(side=LEFT, padx=30)
prec = ttk.Entry(preco)
prec.pack(side=LEFT, fill="x", expand=TRUE, padx=20)

quantidade = ttk.Frame(aba1)
quantidade.pack(pady=25)
ttk.Label(quantidade, text="Quantidade").pack(side=LEFT, padx=10)
quant = ttk.Entry(quantidade)
quant.pack(side=LEFT, fill="x", expand=TRUE, padx=20)


gcodigo = ttk.Frame(aba3)
gcodigo.pack(pady=25)
ttk.Label(gcodigo, text="Código").pack(side=LEFT, padx=15)
gcod = ttk.Entry(gcodigo)
gcod.pack(side=LEFT, fill="x", expand=TRUE, padx=5)

gproduto = ttk.Frame(aba3)
gproduto.pack(pady=25)
ttk.Label(gproduto, text="Produto").pack(side=LEFT, padx=10)
gprod = ttk.Entry(gproduto)
gprod.pack(side=LEFT, fill="x", expand=TRUE, padx=5)

gpreco = ttk.Frame(aba3)
gpreco.pack(pady=25)
ttk.Label(gpreco, text="Preço").pack(side=LEFT, padx=15)
gprec = ttk.Entry(gpreco)
gprec.pack(side=LEFT, fill="x", expand=TRUE, padx=5)

gquantidade = ttk.Frame(aba3)
gquantidade.pack(pady=25)
ttk.Label(gquantidade, text="Quantidade").pack(side=LEFT, padx=0)
gquant = ttk.Entry(gquantidade)
gquant.pack(side=LEFT, fill="x", expand=TRUE, padx=0)

gerir = ttk.Frame(aba3)
gerir.pack(pady=25)
ttk.Label(gerir, text="Atualizar").pack(side=LEFT, padx=0)
ger = ttk.Entry(gerir)
ger.pack(side=LEFT, fill="x", expand=TRUE, padx=0)


lista_produtos = ttk.Treeview(aba2, height= 3, column=("col1", "col2", "col3", "col4", "col5"))
lista_produtos.heading("#0", text="")
lista_produtos.heading("#1", text="ID")
lista_produtos.heading("#2", text="Código")
lista_produtos.heading("#3", text="Produto")
lista_produtos.heading("#4", text="Preço")
lista_produtos.heading("#5", text="Quantidade")

lista_produtos.column("#0", width=1)
lista_produtos.column("#1", width=50)
lista_produtos.column("#2", width=50)
lista_produtos.column("#3", width=250)
lista_produtos.column("#4", width=100)
lista_produtos.column("#5", width=100)

lista_produtos.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.98)
scroll_lista = Scrollbar(aba2, orient="vertical")
lista_produtos.configure(yscroll=scroll_lista.set)
scroll_lista.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.98)
lista_produtos.bind("<Double-1>", duplo_clique)

lista_produtos.delete(*lista_produtos.get_children())
cursor = banco.cursor()
comando_SQL = "SELECT * FROM produtos"
cursor.execute(comando_SQL)
dados_lidos = cursor.fetchall()

for i in dados_lidos:
    lista_produtos.insert("", END, values=i)

botao = ttk.Frame(aba1)
botao.pack(pady=10, padx=10, fill="x")
b1 = ttk.Button(botao, text="Salvar", bootstyle="SUCCESS", command=func_cadastro).pack(side=LEFT, padx=15)

b4 = ttk.Button(botao, text="Limpar", bootstyle="DANGER", command=func_limpar).pack(side=RIGHT, padx=15)


botao2 = ttk.Frame(aba3)
botao2.pack(pady=10, padx=10, fill="x")
b2 = ttk.Button(botao2, text="Apagar", bootstyle="WARNING", command=apagar_registro).pack(side=RIGHT, padx=15)
b6 = ttk.Button(botao2, text="Atualizar Estoque", bootstyle="INFO", command=atualizar_estoque).pack(side=LEFT, padx=15)


app.mainloop()
