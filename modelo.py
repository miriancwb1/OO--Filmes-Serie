class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0 

    def dar__likes(self):
        self.likes +=1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas 
        self.likes = 0   

    def dar__likes(self):
        self.likes +=1


vingadores = Filme('vingadores - guerra infinita', 2018,160)
print(f'nome: {vingadores.nome} - Ano: {vingadores.ano} - likes: {vingadores.likes}')

atlanta = Serie ('atlanta', 2018, 2)

print(f'nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes {atlanta.likes}')
