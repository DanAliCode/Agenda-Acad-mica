# Importando as bibliotecas
from pymongo import MongoClient
from tkinter import messagebox

# Configuração do banco de dados MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['AgendaAcademica']
collection = db['atividades']
counter_collection = db['counters']  # Coleção para gerenciar contadores

# Função para obter o próximo ID automático
def get_next_sequence(sequence_name):
    sequence_document = counter_collection.find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"sequence_value": 1}},
        upsert=True,
        return_document=True
    )
    return sequence_document['sequence_value']

class Atividade:
    def __init__(self):
        self.atividades = db["atividades"]

    def adicionar_atividade(self, usuario_id, titulo, descricao, data_inicio, data_termino, tipo, status):
        # Obtendo o próximo ID automático
        atividade_id = get_next_sequence("atividade_id")

        atividade = {
            "_id": atividade_id,
            "usuario_id": usuario_id,
            "titulo": titulo,
            "descricao": descricao,
            "data_inicio": data_inicio,
            "data_termino": data_termino,
            "tipo": tipo,
            "status": status
        }
        self.atividades.insert_one(atividade)
        messagebox.showinfo("Sucesso", "Atividade adicionada com sucesso!")