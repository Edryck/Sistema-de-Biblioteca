from tkinter import *
from tkinter import messagebox, ttk

from sistema_biblioteca.src.controller import livro_controller
from sistema_biblioteca.src.model.bibliotecario import Bibliotecario

class TelaAdmin:
    def __init__(self, root):
        self.root = root
        self.principal()

    def principal(self):
        self.root.title("Sistema de Biblioteca - Administrador", )
        self.root.geometry("445x550")

        self.borda = LabelFrame(self.root, background="#e9e9e9")
        self.borda.pack(ipady=3, ipadx=3, expand=True, fill="y")
        self.conteinerPrincipal = Frame(self.borda)
        self.conteinerPrincipal.pack(pady=20, padx=20, expand=True, fill=BOTH)

        # Barra de rolagem da tela inteira
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

        self.conteinerCadastro = LabelFrame(self.conteinerPrincipal, text="Adicionar/Remover/Editar Livro")
        self.conteinerCadastro.pack(padx=10, pady=10, expand=True, fill="x")

        # Função para criar os campos de input
        def criarCampo(frame, texto):
            f = Frame(frame)
            f.pack(pady=2)
            Label(f, text=texto, width=15, anchor="e").pack(side=LEFT)
            entry = Entry(f, width=30)
            entry.pack(side=LEFT)
            return entry

        self.tituloLivro = criarCampo(self.conteinerCadastro, "Título do Livro:")
        self.autorLivro = criarCampo(self.conteinerCadastro, "Autor do Livro:")
        self.isbnLivro = criarCampo(self.conteinerCadastro, "ISBN:")

        self.opcoes = Frame(self.conteinerCadastro)
        self.opcoes.pack()

        Button(self.opcoes, text="Cadastrar Livro", command=self.cadastrarLivro).pack(pady=10, side=LEFT,)
        Button(self.opcoes, text="Editar Livro", command=self.editarLivro).pack(pady=10, side=LEFT, )
        Button(self.opcoes, text="Deletar Livro", command=self.deletarLivro).pack(pady=10, side=LEFT,)

        Label(self.conteinerCadastro, text=f"OBS: Para deletar o livro coloque o ISBN dele e clica deletar,\npara alterar adicione o ISBN e altere os dados titulo e autor.").pack()

        # Lista dos livros do banco de dados
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

        self.conteinerGerenciarUsuarios = LabelFrame(self.conteinerPrincipal, text="Gerenciar Usuários")

        self.idUsuario = criarCampo(self.conteinerGerenciarUsuarios, "Id do Usuário:")
        self.nomeUsuario = criarCampo(self.conteinerGerenciarUsuarios, "Nome do Usuário:")
        self.senhaUsuario = criarCampo(self.conteinerGerenciarUsuarios, "Senha de Usuário:")

        self.opcoes1 = Frame(self.conteinerGerenciarUsuarios)
        self.opcoes1.pack()

        Button(self.opcoes1, text="Atualizar Usuário", command=self.atualizarUsuario).pack(pady=10, side=LEFT, )
        Button(self.opcoes1, text="Deletar Usuário", command=self.deletarUsuario).pack(pady=10, side=LEFT, )

    def buscarLivro(self):
        token = self.consultarLivro.get()
        # Chama o controller
        livro = livro_controller.pesquisarLivro(token)

        if livro is None:
            messagebox.showwarning("Atenção", "Livro não encontrado.")
        else:
            # Mostra os dados encontrados
            messagebox.showinfo("Livro Encontrado", f"ID: {livro[0]}\nTítulo: {livro[1]}\nAutor: {livro[2]}\nISBN: {livro[3]}\nDisponível: {livro[4]}")

    def cadastrarLivro(self):
        bibliotecario = Bibliotecario()

        titulo = self.tituloLivro.get()
        autor = self.autorLivro.get()
        isbn = self.isbnLivro.get()

        sucesso = bibliotecario.cadastrarLivro(titulo, autor, isbn)

        if sucesso:
            messagebox.showinfo("Livro cadastrado!", "Cadastro realizado com sucesso!")
            # Limpa campos de input
            self.tituloLivro.delete(0, END)
            self.autorLivro.delete(0, END)
            self.isbnLivro.delete(0, END)
            # Atualiza a lista de livros
            self.carregarLista()
        else:
            messagebox.showerror("Erro", "Não foi possível realizar o cadastro!")

    def editarLivro(self):
        bibliotecario = Bibliotecario()

        titulo = self.tituloLivro.get()
        autor = self.autorLivro.get()
        isbn = self.isbnLivro.get()

        sucesso = bibliotecario.alterarLivro(titulo, autor, isbn)
        if sucesso:
            messagebox.showinfo("Livro Alterado!", "Os dados do livro foram alterados com sucesso!")
            # Limpa campos de input
            self.tituloLivro.delete(0, END)
            self.autorLivro.delete(0, END)
            self.isbnLivro.delete(0, END)
            # Atualiza a lista de livros
            self.carregarLista()
        else:
            messagebox.showerror("Erro", "Não foi possível realizar a alteração!")

    def deletarLivro(self):
        bibliotecario = Bibliotecario()

        isbn = self.isbnLivro.get()

        sucesso = bibliotecario.deletarLivro(isbn)
        if sucesso:
            messagebox.showinfo("Livro deletado!", "O livro deletado com sucesso!")
            self.isbnLivro.delete(0, END)
            self.carregarLista()
        else:
            messagebox.showerror("Erro", "Não foi possível deletar esse livro!")

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

    def atualizarUsuario(self):
        pass

    def deletarUsuario(self):
        pass