# Importando as bibliotecas
import customtkinter
from usuario import *
from tasks import *
from tkinter import *
from tkinter import messagebox as msg
from pymongo import MongoClient
from datetime import datetime, timedelta
import bcrypt
import uuid



# Criando as classes das funcionalidades (BackEnd)
client = MongoClient("mongodb://localhost:27017/")
db = client['AgendaAcademica']
collection = db['atividades']

window = customtkinter.CTk()
menu_frame = Frame(window, width=920, height=497, bg='white')
menu_frame.pack()
register_frame = Frame(window, width=425, height=497, bg='white')
register_frame.pack(side=RIGHT)
main_frame = Frame(window, width=350, height=497, bg='white')
main_frame.pack(side=LEFT)
frame_right = Frame(window, width=572, height=497, bg='white')
frame_right.pack(side=RIGHT)
list_frame_right = Frame(window, width=572, height=497, bg='white')
list_frame_right.pack(side=RIGHT)
edit_frame_right = Frame(window, width=572, height=497, bg='white')
edit_frame_right.pack(side=RIGHT)
del_frame_right = Frame(window, width=572, height=497, bg='white')
del_frame_right.pack(side=RIGHT)
frame_instruction = Frame(window, width=572, height=497, bg='white')
frame_instruction.pack(side=RIGHT)



class App():
    def __init__(self):
        super().__init__()
        self.usuario_fuction = Usuario()
        self.tasks_fuction = Atividade()
        self.usuario_logado = None
        window.title('AgendaAcademica')
        window.geometry('925x500')
        window.configure(bg='#fff')
        window.resizable(False,False)
        self.show_login_screen()
        
        
        window.mainloop()
        pass
        
    # Criando o tamanho da janela inicial
    
        
    def show_login_screen(self):
        
        main_frame.pack_forget()
        frame_right.pack_forget()
        list_frame_right.pack_forget()
        edit_frame_right.pack_forget()
        del_frame_right.pack_forget()
        frame_instruction.pack_forget()
        
        menu_frame.pack()
         
        # Adicionando as informações no Frame da etla inicial lado direito
        menu_label = customtkinter.CTkLabel(master=menu_frame, text='Bem vindo a Agenda Academica', text_color="#4391D1", font=("Microsoft YaHei UI Lighty", 20))
        menu_label.place(x=300, y=5)
        
        # Campo digite o nome do usuario Frame
        self.username_entry = customtkinter.CTkEntry(master=menu_frame, placeholder_text="Usuario", width=300, text_color="#4391D1", font=("Microsoft YaHei UI Light", 14))
        self.username_entry.place(x=300, y=105)
        
        # Campo digite a senha Frame
        self.password_entry = customtkinter.CTkEntry(master=menu_frame, placeholder_text="Senha", width=300, font=("Microsoft YaHei UI Light", 14), show="*")
        self.password_entry.place(x=300, y=165)
        
        # Adicionando botão login
        ButtonLogin = customtkinter.CTkButton(master=menu_frame,text='Login', width=300, command=self.login)
        ButtonLogin.place(x=300, y=235)
        register_span = customtkinter.CTkLabel(master=menu_frame, text='Não tem cadastro?', text_color='#4391D1', font=('Microsoft YaHei UI Light',14))
        register_span.place(x=300, y=275)
        registerButton = customtkinter.CTkButton(master=menu_frame, text='Cadastrar', width=150, fg_color='green', hover_color='#2D9334', command=self.show_register_screen)
        registerButton.place(x=455, y=275)
              
        
    def show_register_screen(self):
        menu_frame.pack_forget()
        
        # Criando o Frame do cadastro de usuario
        frame_cadastro = register_frame
        frame_cadastro.pack(side=RIGHT)
        title_register_label = customtkinter.CTkLabel(master=frame_cadastro, text='Cadastro de Aluno', text_color='#4391D1', font=('Microsoft YaHei UI Light', 20)).place(x=25, y=5)
        span_register_label = customtkinter.CTkLabel(master=frame_cadastro, text='Preencha os dados para cadastro', text_color='#4391D1', font=('Microsoft YaHei UI Light', 10)).place(x=25, y=35)
        
        # Campos de cadastro
        self.nome_entry = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Nome Completo', width=300, font=('Microsoft YaHei UI Light',14))
        self.nome_entry.place(x=25, y=85)
        self.matricula_entry = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Número de Matricula', width=300, font=('Microsoft YaHei UI Light', 14))
        self.matricula_entry.place(x=25, y=125)
        self.email_entry = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='E-mail', width=300, font=('Microsoft YaHei UI Light', 14))
        self.email_entry.place(x=25, y=165)
        self.username_entry = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Usuario', width=300, font=('Microsoft YaHei UI Light', 14))
        self.username_entry.place(x=25, y=205)
        self.password_entry = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Senha', width=300, font=('Microsoft YaHei UI Light', 14),show='*')
        self.password_entry.place(x=25, y=245)
        self.curso_entry = customtkinter.CTkEntry(master=frame_cadastro, placeholder_text='Curso', width=300, font=('Microsoft YaHei UI Light', 14))
        self.curso_entry.place(x=25, y=285)
        checkregister = customtkinter.CTkCheckBox(master=frame_cadastro, text='Aceito todos os Termos e Políticas')
        checkregister.place(x=25, y=325)
        buttonregister = customtkinter.CTkButton(master=frame_cadastro, text='Cadastrar', fg_color='green', hover_color='#2D9334', command=self.register)
        buttonregister.place(x=25, y=395)
        buttonback = customtkinter.CTkButton(master=frame_cadastro, text='Voltar', command=self.back)
        buttonback.place(x=175, y=395)
        
    def back(self):
            # Removendo a tela de cadastro
        register_frame.pack_forget()
            
        menu_frame.pack(side=RIGHT)
        
    def show_main_screen(self):
        
        menu_frame.pack_forget()
        register_frame.pack_forget()
        frame_right.pack_forget()
        edit_frame_right.pack_forget()
        del_frame_right.pack_forget()
        frame_instruction.pack_forget()

        # Criando o frame do menu principal
        main_menu = main_frame
        main_menu.pack(side=LEFT)
        
        title_main = customtkinter.CTkLabel(master=main_menu, text='Menu', text_color='#4391D1', font=('Microsoft YaHei UI Light', 20))
        title_main.place(x=5, y=25)
        button_new_tasks = customtkinter.CTkButton(master=main_menu, text='Adicionar Atividade',width=200, command=self.add_activity_screen)
        button_new_tasks.place(x=20, y=85)
        button_list_activity = customtkinter.CTkButton(master=main_menu, text='Lista de Atividades', width=200, command=self.list_activity_screen)
        button_list_activity.place(x=20, y=125)
        button_edit_activity = customtkinter.CTkButton(master=main_menu, text='Editar Atividade', width=200, command=self.show_edit_activity_screen)
        button_edit_activity.place(x=20, y=165)
        button_del_activity = customtkinter.CTkButton(master=main_menu, text='Deletar Atividade', width=200, command=self.show_delete_activity_screen)
        button_del_activity.place(x=20, y=205)
        button_instructions = customtkinter.CTkButton(master=main_menu, text='Sobre', width=200, command=self.show_instruction_screen)
        button_instructions.place(x=20, y=385)
        
        
        button_back_login = customtkinter.CTkButton(master=main_menu, text='Sair', width=200, command=self.show_login_screen)
        button_back_login.place(x=20, y=425)
        
        
    def add_activity_screen(self):
        # Apagando os frames para não sobrepor
        menu_frame.pack_forget()
        register_frame.pack_forget()
        list_frame_right.pack_forget()
        del_frame_right.pack_forget()
        frame_instruction.pack_forget()
        
        #Criando o novo frame
        frame_tasks = frame_right
        frame_tasks.pack(side=RIGHT)
        
        title_activity = customtkinter.CTkLabel(master=frame_tasks, text='Adicionar Nova Atividade',text_color='#4391D1', font=('Microsoft YaHei UI Light', 20))
        title_activity.place(x=25, y=5)
        span_activity = customtkinter.CTkLabel(master=frame_tasks, text='Preencha os dados corretamente', text_color='#4391D2', font=('Microsoft YaHei UI Light', 10))
        span_activity.place(x=25, y=35)
        
        self.title_entry = customtkinter.CTkEntry(master=frame_tasks, placeholder_text='Titulo', width=300, font=('Micrososft YaHei UI Light', 14))
        self.title_entry.place(x=25, y=85)
        self.description_entry = customtkinter.CTkEntry(master=frame_tasks, placeholder_text='Descrição da Atividade', width=300, font=('Microsoft YaHei UI Light', 14))
        self.description_entry.place(x=25, y=125)
        self.date_begin_entry = customtkinter.CTkEntry(master=frame_tasks, placeholder_text='Data de inicio = DD/MM/YYYY HH:MM', width=300, font=('Microsoft YaHei UI Light', 14))
        self.date_begin_entry.place(x=25, y=165)
        self.date_end_entry = customtkinter.CTkEntry(master=frame_tasks, placeholder_text='Data de termino = DD/MM/YYYY HH:MM', width=300, font=('Microsoft YaHei UI Light', 14))
        self.date_end_entry.place(x=25, y=205)
        self.category_entry = customtkinter.CTkEntry(master=frame_tasks)
        #Criando uma lista de tipos de atividades
        tipos = ["Provas", "Reunião", "Estudos", "Trabalho Academico", "Encontro", "Outros"]
        self.type_var = StringVar(value=tipos[0])
        self.type_entry = customtkinter.CTkOptionMenu(master=frame_tasks,values=tipos, variable=self.type_var, width=300)
        self.type_entry.place(x=25, y=245)
        #Criando uma lista para o status da atividade
        opcoes = ["Pendente", "Concluido", "Em Andamento", "Atrasado"]
        self.status_var = StringVar(value=opcoes[0])
        self.status_entry = customtkinter.CTkOptionMenu(master=frame_tasks, values=opcoes, variable=self.status_var, width=300)
        self.status_entry.place(x=25, y=285)
        
        button_save_activity = customtkinter.CTkButton(master=frame_tasks, text='Salvar', fg_color='green', hover_color='#2D9334', command=self.add_activity)
        button_save_activity.place(x=25, y=325)
        button_back_menu = customtkinter.CTkButton(master=frame_tasks, text='Voltar', command=self.show_main_screen)
        button_back_menu.place(x=25, y=355)
        
    def list_activity_screen(self):
        #Apagando os frames para não sobrepor
        menu_frame.pack_forget()
        register_frame.pack_forget()
        frame_right.pack_forget()
        edit_frame_right.pack_forget()
        del_frame_right.pack_forget()
        frame_instruction.pack_forget()
        
        # Criando a logica para extrair os dados do banco
        atividades = list(self.tasks_fuction.atividades.find().sort("data_inicio", 1))
        if atividades:
            frame_list = list_frame_right
            frame_list.pack(side=RIGHT)
            y_offset = 25

        for atividade in atividades:
            atividade_label = customtkinter.CTkLabel(master=frame_list, text=f"ID: {atividade['_id']} Titulo: {atividade['titulo']} - Data Início: {atividade['data_inicio']} - Status: {atividade['status']}", text_color='#4391D1')
            atividade_label.place(x=25, y=y_offset)
            y_offset += 30
            
            
    def show_edit_activity_screen(self, atividade=None):
        #Apagando os frames para não sobrepor
        menu_frame.pack_forget()
        register_frame.pack_forget()
        frame_right.pack_forget()
        list_frame_right.pack_forget()
        del_frame_right.pack_forget()
        frame_instruction.pack_forget()
        
        #Criando o novo frame 
        frame_edit = edit_frame_right
        frame_edit.pack(side=RIGHT)
        
        # Lógica para busca de dados por ID no banco de dados
        if atividade is None:
            self.id_entry = customtkinter.CTkEntry(master=frame_edit, placeholder_text='Digite o ID da atividade', width=300, font=('Microsoft YaHei UI Light', 14))
            self.id_entry.place(x=25, y=20)
            
            button_search = customtkinter.CTkButton(master=frame_edit, text='Buscar', width=150, command=lambda: self.search_activity_by_id(self.id_entry.get()))
            button_search.place(x=25, y=60)
            
            msg.showinfo("Atenção", "Digite o ID da atividade para carregá-la")
            return
        
        # Configurando o Cabeçalho dos conjuntos dos campos (Dados atuais / Novos Dados)
        old_data_label = customtkinter.CTkLabel(master=frame_edit, text='Dados Atuais', text_color='#4391D1', font=('Microsoft YaHei UI Light', 20))
        old_data_label.place(x=15, y=100)
        
        new_data_label = customtkinter.CTkLabel(master=frame_edit, text='Edição de Atividade', text_color='#4391D1', font=('Microsoft YaHei UI Light', 20))
        new_data_label.place(x=300, y=100)
        
        # Dados atuais (à esquerda)
        
        old_title = customtkinter.CTkLabel(master=frame_edit, text=f"Título: {atividade['titulo']}", width=200, font=('Microsoft YaHei UI Light', 14))
        old_title.place(x=15, y=180)
        
        old_date_begin = customtkinter.CTkLabel(master=frame_edit, text=f"Data Inicio: {atividade['data_inicio']}", width=200, font=('Microsoft YaHei UI Light', 14))
        old_date_begin.place(x=15, y=220)
        
        old_date_end = customtkinter.CTkLabel(master=frame_edit, text=f"Data Termino: {atividade['data_termino']}", width=200, font=('Microsoft YaHei UI Light', 14))
        old_date_end.place(x=15, y=260)
        
        old_status = customtkinter.CTkLabel(master=frame_edit, text=f"Status: {atividade['status']}", width=200, font=('Microsft YaHei UI Light', 14))
        old_status.place(x=15, y=300)

        #Campos de edição (à direita)
        self.title_entry = customtkinter.CTkEntry(master=frame_edit, placeholder_text='Titulo', width=200, font=('Microsoft YaHei UI Light', 14))
        self.title_entry.insert(0, atividade['titulo'])
        self.title_entry.place(x=250, y=180)
        
        self.date_begin_entry = customtkinter.CTkEntry(master=frame_edit, placeholder_text='Data de inicio: DD/MM/YYYY HH:MM', width=200, font=('Microsoft YaHei UI Light', 14))
        #Verificando o tipo e formata a data se possível
        data_inicio = atividade.get('data_inicio')
        if isinstance(data_inicio, datetime):
            self.date_begin_entry.insert(0, data_inicio.strftime("%d/%m/%Y %H:%M"))
        else:
            self.date_begin_entry.insert(0, '')
        self.date_begin_entry.place(x=250, y=220)
        
        self.date_end_entry = customtkinter.CTkEntry(master=frame_edit, placeholder_text='Data de Termino: DD/MM/YYYY HH:MM', width=250, font=('Microsoft YaHei UI Light', 14))
        # Verificando o tipo e formata a data se possivel
        data_termino = atividade.get('data_termino')
        if isinstance(data_termino, datetime):
            self.date_end_entry.insert(0, data_termino.strftime("%d/%m/%Y %H:%M"))
        else:
            self.date_end_entry.insert(0, '')
        self.date_end_entry.place(x=250, y=260)
        
        self.status_entry = customtkinter.CTkOptionMenu(master=frame_edit, values=["Pendente", "Concluido", "Em Andamento", "Atrasado"], width=250)
        self.status_entry.set(atividade.get('status', 'Pendente'))
        self.status_entry.place(x=250, y=300)
        
        button_save_edit = customtkinter.CTkButton(master=frame_edit, text='Salvar', width=150, fg_color='green', hover_color='#2D9334', command=lambda: self.update_activity(atividade['_id']))
        button_save_edit.place(x=250, y=340)
        
        button_back_main = customtkinter.CTkButton(master=frame_edit, text='Voltar', width=150, command=self.show_main_screen)
        button_back_main.place(x=420, y=340)
        
    def show_delete_activity_screen(self, atividade=None):
        menu_frame.pack_forget()
        register_frame.pack_forget()
        frame_right.pack_forget()
        list_frame_right.pack_forget()
        edit_frame_right.pack_forget()
        frame_instruction.pack_forget()
        
        frame_del = del_frame_right
        frame_del.pack(side=RIGHT)
        
        if atividade is None:
            self.id_search = customtkinter.CTkEntry(master=frame_del, placeholder_text='Digite o ID da atividade', width=300, font=('Microsoft YaHei UI Light', 20))
            self.id_search.place(x=25, y=20)
            
            button_search = customtkinter.CTkButton(master=frame_del, text='Bucar', width=150, command=lambda: self.search_activity_for_deletion(self.id_search.get()))
            button_search.place(x=25, y=60)
            
            msg.showinfo('Atenção', 'Digite o ID da atividade para carregar e em seguida em Buscar')
            return
        
        del_data_label = customtkinter.CTkLabel(master=frame_del, text='Dados buscado,', text_color='#4391D1', font=('Microsoft YaHei UI Light', 18))
        del_data_label.place(x=25, y=120)
        
        del_title = customtkinter.CTkLabel(master=frame_del, text=f'Titulo: {atividade['titulo']}', width=300, font=('Microsoft YaHei UI Light', 14))
        del_title.place(x=25, y=160)
        
        del_description = customtkinter.CTkLabel(master=frame_del, text=f'Descrição: {atividade['descricao']}', width=300, font=('Microsoft YaHei UI Light', 14))
        del_description.place(x=25, y=200)
        
        del_date_begin = customtkinter.CTkLabel(master=frame_del, text=f'Data Inicio: {atividade['data_inicio']}', width=300, font=('Microsoft YaHei UI Light', 14))
        del_date_begin.place(x=25, y=240)
        
        del_date_end = customtkinter.CTkLabel(master=frame_del, text=f'Data Termino: {atividade['data_termino']}', width=300, font=('Microsoft YaHei UI Light', 14))
        del_date_end.place(x=25, y=280)
        
        del_status = customtkinter.CTkLabel(master=frame_del, text=f'Status: {atividade['status']}', width=300, font=('Microsoft YaHei UI Light', 14))
        del_status.place(x=25, y=320)
        
        # Execução e questionamento sobre a exclusão da atividade
        confirm_label = customtkinter.CTkLabel(master=frame_del, text='Deseja excluir essa atividade?', text_color='#FF0000', font=('Microsoft YaHei UI Light', 14))
        confirm_label.place(x=260, y=120)
        
        button_del = customtkinter.CTkButton(master=frame_del, text='Deletar', width=250, fg_color='red', hover_color='#D32F2F', command=lambda: self.confirm_delete_activity(atividade['_id']))
        button_del.place(x=260, y=170)
            
        button_back = customtkinter.CTkButton(master=frame_del, text='Voltar', width=250, command=self.show_main_screen)
        button_back.place(x=260, y=210)
    
    
    def show_instruction_screen(self):
        menu_frame.pack_forget()
        register_frame.pack_forget()
        frame_right.pack_forget()
        list_frame_right.pack_forget()
        edit_frame_right.pack_forget()
        del_frame_right.pack_forget()
        
        instructions_frame = frame_instruction
        instructions_frame.pack(side=RIGHT)
        
        title_instructions = customtkinter.CTkLabel(master=instructions_frame, text=' Instruções e Políticas de uso', text_color='#4391D1', font=('Microsoft YaHei UI Light', 20))
        title_instructions.place(x=120, y=25)
        
        instructions_text = """
            Esse é um projeto proposto pela minha
            Universidade (USJT UC Modelagem de software)
            PROPOSTA: Desenvolva uma especificação de software para um sistema de 
            agenda de atividades acadêmicas para alunos de 
            cursos de graduação da área de Tecnologia da Informação.
            Sua especificação deve conter:

            a) Listagem de requisitos funcionais e não funcionais
            b) Protótipos não funcionais das telas
            c) Modelo Entidade Relacionamento
            d) Modelo lógico de Banco de Dados

            Para utilizar o programa, siga os passos abaixo:
    
            1. Faça login com seu usuário e senha.
            2. No menu principal, você pode:
                - Adicionar novas atividades.
                - Listar todas as suas atividades.
                - Editar atividades existentes.
                - Deletar atividades que não são mais necessárias.
            3. Para cada atividade, você pode definir:
                - Título
                - Descrição
                - Datas de início e término
                - Status da atividade   
                
             """
        
        instructions_text_label = customtkinter.CTkLabel(master=instructions_frame, text=instructions_text, text_color='#000000', font=('Microsoft YaHei UI Light',12))
        instructions_text_label.place(x=15, y=55)
        
        
    
        
    def login(self):
        usuario = self.username_entry.get()
        senha = self.password_entry.get()
        self.usuario_logado = self.usuario_fuction.autenticar(usuario, senha)
        if self.usuario_logado:
            self.show_main_screen()
        else:
            msg.showinfo('Usuario ou senha incorreta !')     
        
    def register(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        email = self.email_entry.get()
        usuario = self.username_entry.get()
        senha = self.password_entry.get()
        curso = self.curso_entry.get()
        self.usuario_fuction.cadastrar(nome, matricula, email, usuario, senha, curso)
        self.show_login_screen
        
    def add_activity(self):
        if not self.usuario_logado:
            msg.showerror("Erro", "Você precisa estar logado para adicionar atividades.")
            return
        
        usuario_id = self.usuario_logado["_id"]
        titulo = self.title_entry.get()
        descricao = self.description_entry.get()
        try:
            data_inicio = datetime.strptime(self.date_begin_entry.get().strip(), "%d/%m/%Y %H:%M")
            data_termino = datetime.strptime(self.date_end_entry.get().strip(), "%d/%m/%Y %H:%M")
        except ValueError:
            msg.showerror("Erro", "Formato de data e hora inválido. Use o formato D-M-Y H:M.")
            return
        tipo = self.type_entry.get()
        status = self.status_entry.get()
        self.tasks_fuction.adicionar_atividade(usuario_id, titulo, descricao, data_inicio, data_termino, tipo, status)
        self.show_main_screen()
        
    def edit_activity(self, atividade_id):
        
        atividade = self.tasks_fuction.atividades.find_one({"_id": atividade_id})
        if atividade:
            self.show_edit_activity_screen(atividade)
        else:
            msg.showerror("Erro", "Atividade não encontrada")
        

    def update_activity(self, atividade_id):
        novos_dados = {
            "titulo": self.title_entry.get(),  # Corrigido aqui
            "data_inicio": datetime.strptime(self.date_begin_entry.get().strip(), "%d/%m/%Y %H:%M"),
            "data_termino": datetime.strptime(self.date_end_entry.get().strip(), "%d/%m/%Y %H:%M"),
            "status": self.status_entry.get(),
        }
        result = self.tasks_fuction.atividades.update_one({"_id": atividade_id}, {"$set": novos_dados})
        if result.modified_count > 0:
            msg.showinfo("Sucesso", "Atividade atualizada com sucesso!")
        else:
            msg.showerror("Erro", "Erro ao atualizar atividade.")
    
    def get_activity_by_id(self, activity_id):
    # Converte o ID para inteiro, se necessário
        try:
            
            activity_id = int(activity_id)  # Supondo que o ID seja um número inteiro
        except ValueError:
            return None  # Retorna None se a conversão falhar

    # Busca a atividade no banco de dados
        return self.tasks_fuction.atividades.find_one({"_id": activity_id})

    def search_activity_by_id(self, activity_id):
        # Busca a atividade pelo ID
        atividade = self.get_activity_by_id(activity_id)
    
        if atividade:
            self.show_edit_activity_screen(atividade)
        else:
            msg.showerror("Erro", "Atividade não encontrada pelo ID fornecido!")
            
    def search_activity_for_deletion(self, activity_id):
        atividade = self.get_activity_by_id(activity_id)
        if atividade:
            self.show_delete_activity_screen(atividade)
        else:
            msg.showerror("Erro", "Atividade não encontrada pelo ID fornecido!")
        
        
    
            
    def delete_activity(self, atividade_id):
        """Deleta uma atividade pelo ID"""
        result = self.tasks_fuction.atividades.delete_one({"_id": atividade_id})
        if result.deleted_count > 0:
            msg.showinfo("Sucesso", "Atividade deletada com sucesso!")
        else:
            msg.showerror("Erro", "Erro ao deletar atividade")
            
    def confirm_delete_activity(self, activity_id):
        if messagebox.askyesno("Confirmação", "Você realmente deseja deletar esta atividade?"):
            self.delete_activity(activity_id)
        else:
            msg.showinfo("Cancelado", "A operação de deleção foi cancelada.")          

    def logout(self):
        self.usuario_logado = None
        self.show_login_screen()
                  
App()