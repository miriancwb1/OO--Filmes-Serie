class Progama: 

    def __init__(self, nome, ano, ):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property 
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome (self,novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes +=1

    def __str__ (self):
        return f'{self.nome} - {self.ano} - {self._likes} likes'

class Filme(Progama):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
        self._likes = 0
        
class Serie(Progama):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas 
        self._likes = 0   

class Playlist(list):
    def __init__(self, nomes, progamas):
        self.nome = nomes
        super().__init__(progamas)


vingadores = Filme('vingadores - guerra infinita', 2018,160)
atlanta = Serie ('atlanta', 2018, 2) 
tmp = Filme ('todo mundo em pânico', 1999,100)
demolidor = Serie ('demolidor', 2016,2)

vingadores.dar_likes
atlanta.dar_likes
tmp.dar_likes
tmp.dar_likes
tmp.dar_likes
tmp.dar_likes
demolidor.dar_likes
demolidor.dar_likes
demolidor.dar_likes


filmes_e_series = [vingadores,atlanta,demolidor,tmp]
Playlist_fim_de_semana = Playlist ('fim de semana', filmes_e_series)

print (f'Tamanho da Playlit:{len(Playlist_fim_de_semana)}')

for progama in Playlist_fim_de_semana:
    print (progama)

