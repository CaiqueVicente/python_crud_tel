#o objetivo ao criar esse crud vai ser coletar os dados e fazer uma lista telefônica. dados necessários: id, nome, cidade e número
# usuario
# idade
# cidade
# telefone





#aqui nessa classe criamos os atributos 
class crudUsuario:
    def __init__(self,user,idade,cidade,telefone):
        self.user = user
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone

class gerenciar:
    def __init__(self):
        self.clientes = [] #basicamente esse será o nosso banco de dados
        pass

    def criar(self,cliente):
        self.clientes.append(cliente)

    def ler(self):
        for cliente in self.clientes:
            print( "Nome:",cliente.user,"idade:", cliente.idade, "cidade:",cliente.cidade, "telefone:", cliente.telefone)

    #Aqui dentro do meu update, aprendi a utilizar o método Kwargs (**dados), onde eu posso passar a quantidade de váriaveis em forma de um dicionário 
    def update(self, indice, **dados):
        cliente = self.clientes[indice]
        for chave, valor in dados.items():
            setattr(cliente,chave, valor)

    def delete(self, indice):
        #caso o meu cliente for removido imprimir a mensagem "cliente removido com sucesso!" caso contrário imprimir "indice inválido!"
        if indice <=3:
            self.clientes.pop(indice)
            print("Cliente removido com sucesso!")
        else: 
            print("Indice inválido")


crud = gerenciar()

while True:
    try:
        cadastro = cadastro = int(input("Seja Bem-Vindo(a) ao nosso sistema de registro!\n =================================================\n Selecione uma das seguintes opções pelo número:\n1- Criar Usuário\n2- Ver Usuário Criado\n3- Atualizar Usuário\n4- Deletar Usuário\nSelecione uma opção:"))
        break
    except ValueError:
        print("ops... algo deu errado. Digite um número!")
    
    
    
    








        
        

   
        

