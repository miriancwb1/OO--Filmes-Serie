class Progama: 

    def __init__(self, nome, ano, ):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property 
    def nome(self):
        return self.__nome
    
    
    @nome.setter
    def nome (self,novo_nome):
        self.__nome = novo_nome.title()


    @property 
    def likes(self):
        return self.__likes
    
    def dar__likes(self):
        self.__likes +=1

class Filme(Progama):
  
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
        

class Serie(Progama):
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas 
        self.__likes = 0   


vingadores = Filme('vingadores - guerra infinita', 2018,160)
vingadores.dar__likes()
print(f'nome: {vingadores.nome} - Ano: {vingadores.ano} - likes: {vingadores.likes}')

atlanta = Serie ('atlanta', 2018, 2)
atlanta.dar__likes()
atlanta.dar__likes()

print(f'nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes {atlanta.likes}')
