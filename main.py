#o objetivo ao criar esse crud vai ser coletar os dados e fazer uma lista telefônica. dados necessários: id, nome, cidade e número
# usuario
# idade
# cidade
# telefone





#aqui nessa classe criamos os atributos 


class crudUsuario:
    def __init__(self):
        self.user = ''
        self.idade = ''
        self.cidade = ''
        self.telefone = ''

    def __str__(self):
        return f"Nome: {self.user} \nidade: {self.idade} \ncidade:{self.cidade} \ntelefone:{self.telefone}"

class gerenciar:
    def __init__(self):
        self.clientes = [] #basicamente esse será o nosso banco de dados
        pass

    def criar(self,cliente):
        cliente.user = input("Digite seu nome: ")
        try:
            cliente.idade = int(input("Digite a sua idade: "))
            
        except ValueError:
            print("algo deu errado. Digite um número!")
            return

        cliente.cidade = input("Digite sua cidade: ")
        cliente.telefone = str(input("Digite seu telefone: "))
        self.clientes.append(cliente)
        print("Cliente Cadastrado com Sucesso!")
    def ler(self):
        for cliente in self.clientes:
            print(f"\n\n====================\nAQUI ESTÃO OS SEUS DADOS\n{cliente}\n====================\n\n")

    #Aqui dentro do meu update, aprendi a utilizar o método Kwargs (**dados), onde eu posso passar a quantidade de váriaveis em forma de um dicionário 
    def update(self, indice, **dados):
        cliente = self.clientes[indice]
        for chave, valor in dados.items():
            setattr(cliente,chave, valor)

    def delete(self, indice):
        #caso o meu cliente for removido imprimir a mensagem "cliente removido com sucesso!" caso contrário imprimir "indice inválido!"
        if 0 <= indice < len(self.clientes):
            removido = self.clientes.pop(indice)
            print(f"Cliente {removido.user} removido com sucesso!")
        else: 
            print("Indice inválido")


crud = gerenciar()

while True:
    try:
        cadastro =  int(input("Seja Bem-Vindo(a) ao nosso sistema de registro!\n =================================================\n Selecione uma das seguintes opções pelo número:\n1- Criar Usuário\n2- Ver Usuário Criado\n3- Atualizar Usuário\n4- Deletar Usuário\n5-Sair\nSelecione uma opção:"))
        
    except ValueError:
        print("ops... algo deu errado. Digite um número!")
        continue

    if cadastro == 1:
        c1 = crudUsuario()
        crud.criar(c1)
    elif cadastro == 2:
        crud.ler()

    elif cadastro == 3:
        atualizar = input("Selecione o indice do usuário para atualizar: ")
        crud.update(0, user="joão")
    elif cadastro == 4:
        indice = int(input("Digite o indice do cliente para deletar: "))
        crud.delete(indice)
    else:
        print("==================\nEncerrando sistema...\nFinalizado!\n=================")
        break

    
    


    


    





    
    
    








        
        

   
        

