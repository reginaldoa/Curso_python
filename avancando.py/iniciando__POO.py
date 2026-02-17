#Iniciando programação orientada a objetos

#Criando classes

class Casa:
    def __init__(self,cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')

    def quantos_quartos(self):
        print(f"A casa tem {self.quartos} quartos")

    def quantos_banheiros(self):
        print(f"A casa tem {self.banheiros} banheiros")
    
    def add_quarto(self):
        self.quartos += 1       
        print(f"Esta casa tem {self.quartos} quartos")

    def trocar_cor(self, nova_cor):
        print(f"antes a cor era {self.cor}, agora a casa é : {nova_cor}")



casa1 = Casa("Crômio", 2 , 1 )
casa2 = Casa("Verde", 6 , 10)

print('\nCasa 1: ') #"\n" pula uma linha
casa1.mostrar_cor()
casa1.quantos_quartos()
casa1.quantos_banheiros()
casa1.add_quarto()
casa1.trocar_cor("ROSA")


print('\nCasa 2: ')
casa2.mostrar_cor()
casa2.quantos_quartos()
casa2.quantos_banheiros()
casa2.add_quarto()
casa2.trocar_cor("VERDE MARINHO")