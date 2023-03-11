import pandas as pd 
indice = ["thrusters", "sensores", "ano de criação", "numero de hidrofones"]


class AUV: 
    def __init__(self, nome: str, thrusters: int, sensores: list, ano: int, hidrofones: int):
        self.nome = nome
        self.thrusters = thrusters
        self.sensores = sensores
        self.ano = ano
        self.hidrofones = hidrofones

    def get_ano(self):
        return self.ano
    
    def get_thruster(self):
        return self.thrusters

    def __repr__(self): 
        return "%s" % (self.nome)

class lista:
    def __init__(self):
        pass

    def ranking(self):
        rank = sorted(auvs, key= AUV.get_ano, reverse=True)
        print("AUV's por ano (mais novo ao mais antigo):", rank)

    def unico(self):
        aux = input("Escolha um AUV \n")
        auv_escolhido = aux.upper()

        if auv_escolhido == 'LUA':
            nome = ["Lua"]
            atributos = [Lua.thrusters, Lua.sensores, Lua.ano, Lua.hidrofones] 
            dataframe = pd.DataFrame(atributos, columns= nome, index= indice)
            print(dataframe)

        elif auv_escolhido == 'BRHUE':
            nome = ["BrHUE"]
            atributos = [BrHUE.thrusters, BrHUE.sensores, BrHUE.ano, BrHUE.hidrofones]
            dataframe = pd.DataFrame(atributos, columns= nome, index= indice)
            print(dataframe)

        else:
            print("AUV inexistente")
    

    def mostra_todos(self):
        atributos = [[BrHUE.thrusters, Lua.thrusters],
            [BrHUE.sensores, Lua.sensores],
            [BrHUE.ano, Lua.ano],
            [BrHUE.hidrofones,Lua.hidrofones]]
        df = pd.DataFrame(atributos, columns=['BrHUE', 'Lua'], index= ["thrusters","sensores", "ano de criação","numero de hidrofones"])
        print(df)

    def decrescente_thruster(self): 
        listad = sorted(auvs, key= AUV.get_thruster, reverse=True)
        print("AUV's por número de thrusters:", listad)
          
BrHUE = AUV(nome='BrHUE', thrusters=6, sensores=['sensor de pressão e profundidade'], ano=2020, hidrofones=4)
Lua = AUV(nome='LUA', thrusters=8, sensores=['BAR30: sensor de pressão externa', 'BMP180: sensor de pressão inerna', "sensor de vazamento"], ano=2022, hidrofones=4)

auvs = [BrHUE, Lua]

lista.mostra_todos(auvs)
lista.unico(auvs)
lista.ranking(auvs)
lista.decrescente_thruster(auvs)
