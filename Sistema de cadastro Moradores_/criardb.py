import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('moradores.db')
        self.c = self.conn.cursor()
        self.create_table()
        
    
    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS moradores ( 
                               id INTEGER PRIMARY KEY,
                               nome TEXT NOT NULL,
                               email TEXT NOT NULL,
                               tel TEXT NOT NULL,
                               bloco TEXT NOT NULL,
                               apto TEXT NOT NULL,
                               data_recebimento TEXT NOT NULL,
                               data_entrega TEXT NOT NULL,
                               responsavel TEXT NOT NULL,
                               status TEXT NOT NULL,
                               picture TEXT NOT NULL) ''')
        
    def register_resident(self, dados):
    # Encontrar o maior ID atualmente
        self.c.execute("SELECT MAX(id) FROM moradores")
        max_id = self.c.fetchone()[0]

    # Se não houver registros, comece com 1
        new_id = 1 if max_id is None else max_id + 1

    # Inserir novo registro com o novo ID
        self.c.execute("INSERT INTO moradores (id, nome, email, tel, bloco, apto, data_recebimento, data_entrega, responsavel, status, picture) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                   (new_id, *dados))
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Registrado com sucesso!')
         
    def view_all_residents(self):
        self.c.execute("SELECT * FROM moradores")
        dados = self.c.fetchall()
        
        return dados
    def search_resident(self, id):
        self.c.execute("SELECT * FROM moradores WHERE id=?", (id,))
        dados = self.c.fetchone()
        
        return dados
        
    def update_resident(self, novos_valores):
        query = "UPDATE moradores SET nome=?, email=?, tel=?, bloco=?, apto=?, data_recebimento=?, data_entrega=?, responsavel=?, status=?, picture=? WHERE id=? "
        self.c.execute(query, novos_valores)
        self.conn.commit()
        
        messagebox.showinfo('Sucesso', f'Morador com ID:{novos_valores[10]} foi atualizado!')
        
    def delete_resident(self, id):
         self.c.execute("DELETE FROM moradores WHERE id=?", (id,))
         self.conn.commit()
         
         messagebox.showinfo('Sucesso', f'Morador com ID:{id} foi deletado!')
    
sistema_de_resgitro = SistemaDeRegistro()



    