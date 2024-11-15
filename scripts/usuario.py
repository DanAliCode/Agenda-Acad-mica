from pymongo import MongoClient
import bcrypt
import uuid
from tkinter import messagebox

# Criando o banco
client = MongoClient("mongodb://localhost:27017/")
db = client['AgendaAcademica']

class Usuario:
    def __init__(self):
        self.usuarios = db["usuarios"]

    def cadastrar(self, nome, matricula, email, usuario, senha, curso):
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        usuario = {
            "_id": str(uuid.uuid4()),
            "nome": nome,
            "matricula": int(matricula),
            "email": email,
            "usuario": usuario,
            "senha": senha_hash,
            "curso": str(curso)
        }
        self.usuarios.insert_one(usuario)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

    def autenticar(self, usuario, senha):
        user = self.usuarios.find_one({"usuario": usuario})
        if user and bcrypt.checkpw(senha.encode('utf-8'), user['senha']):  # Corrigido para 'user'
            messagebox.showinfo("Sucesso", "Autenticação bem-sucedida!")
            return user
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")
        return None

    
    # def autenticar(self, usuario, senha):
    #     user = self.usuarios.find_one({"usuario": usuario})
    #     if user and bcrypt.checkpw(senha.encode('utf-8'), usuario['senha']):
    #         messagebox.showinfo("Sucesso", "Autenticação bem-sucedida!")
    #         return user
    #     messagebox.showerror("Erro", "E-mail ou senha incorretos.")
    #     return None