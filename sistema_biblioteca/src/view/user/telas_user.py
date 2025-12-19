from tkinter import *
from tkinter import ttk, messagebox

from sistema_biblioteca.src.controller import livro_controller


class TelaUser:
    def __init__(self, root):
        self.root = Tk()
        self.principal()


    def principal(self):
        self.root.title("Sistema de Biblioteca - Usuário", )
        self.root.geometry("445x550")

        self.borda = LabelFrame(self.root, background="#e9e9e9")
        self.borda.pack(ipady=3, ipadx=3, expand=True, fill="y")
        self.conteinerPrincipal = Frame(self.borda)
        self.conteinerPrincipal.pack(pady=20, padx=20, expand=True, fill=BOTH)

        scrollbar = ttk.Scrollbar(self.conteinerPrincipal, orient="vertical")
        scrollbar.pack(side=RIGHT, fill="y")

        self.mensagem = Label(
            self.conteinerPrincipal,
            text="Bem-vindo à Biblioteca",
            font=("Arial", 15, "bold")
        )
        self.mensagem.pack(pady=10)

        self.conteinerConsulta = LabelFrame(self.conteinerPrincipal, text="Pesquisar Livro")
        self.conteinerConsulta.pack(padx=10, pady=10, expand=True, fill="x")

        self.consultarLivro = Entry(self.conteinerConsulta)
        self.consultarLivro["width"] = 30
        self.consultarLivro.pack(pady=20, side=LEFT, expand=True, fill="x")
        self.buscar = Button(self.conteinerConsulta)
        self.buscar["command"] = self.buscarLivro
        self.buscar["text"] = "Buscar Livro"
        self.buscar.pack(pady=20, padx=5, side=RIGHT)

        self.conteinerEmpDev = LabelFrame(self.conteinerPrincipal, text="Empréstimo/Devolução de Livros")
        self.conteinerEmpDev.pack(padx=10, pady=10, expand=True, fill="x")

        # Função para criar os campos de input
        def criarCampo(frame, texto):
            f = Frame(frame)
            f.pack(pady=2)
            Label(f, text=texto, width=15, anchor="e").pack(side=LEFT)
            entry = Entry(f, width=30)
            entry.pack(side=LEFT)
            return entry

        self.isbnLivro = criarCampo(self.conteinerEmpDev, "ISBN:")

        self.opcoes = Frame(self.conteinerEmpDev)
        self.opcoes.pack()

        Button(self.opcoes, text="Pegar Livro", command=self.pegarLivro).pack(pady=10, side=LEFT, )
        Button(self.opcoes, text="Devolver Livro", command=self.devolverLivro).pack(pady=10, side=LEFT, )

        Label(self.conteinerEmpDev, text=f"OBS: Para reservar/devolver o livro coloque o ISBN\ndele e pressione Pegar/Devolver Livro.").pack()

        self.conteinerLista = LabelFrame(self.conteinerPrincipal, text="Acervo da Biblioteca")
        self.conteinerLista.pack(pady=10, padx=10, expand=True, fill=BOTH)

        # Botão para atualizar a lista
        Button(self.conteinerLista, text="Atualizar Lista", command=self.carregarLista).pack(anchor="e")

        # Lista de livros
        colunas = ("ID", "Título", "Autor", "ISBN")
        self.tree = ttk.Treeview(self.conteinerLista, columns=colunas, show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("ISBN", text="ISBN")

        self.tree.column("ID", width=25, anchor="center")
        self.tree.column("Título", width=150)
        self.tree.column("Autor", width=100)
        self.tree.column("ISBN", width=75)

        # Barra de rolagem da lista
        scrollbar = ttk.Scrollbar(self.conteinerLista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill="y")
        self.tree.pack(fill=BOTH, expand=True)

        # Carrega a lista quando abre a tela
        self.carregarLista()

    def buscarLivro(self):
        token = self.consultarLivro.get()
        # Chama o controller
        livro = livro_controller.pesquisarLivro(token)

        if livro is None:
            messagebox.showwarning("Atenção", "Livro não encontrado.")
        else:
            # Mostra os dados encontrados
            messagebox.showinfo("Livro Encontrado",
                                f"ID: {livro[0]}\nTítulo: {livro[1]}\nAutor: {livro[2]}\nISBN: {livro[3]}\nDisponível: {livro[4]}")

    def pegarLivro(self):
        pass

    def devolverLivro(self):
        pass

    def carregarLista(self):
        # Limpa a lista
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Busca os dados recentes
        livros = livro_controller.listarLivros()

        if livros:
            for livro in livros:
                # Insere na tabela
                self.tree.insert("", "end", values=(livro[0], livro[1], livro[2], livro[3]))