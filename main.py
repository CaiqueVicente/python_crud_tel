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

    def update(self, indice, new):
        self.clientes[indice].user = new
        self.clientes [indice].idade = new
        self.clientes [indice].cidade = new
        self.clientes [indice].telefone = new

    def delete(self, indice):
        del self.clientes[indice]


crud = gerenciar()

c1 = crudUsuario("Caique", 21, "sp", "4352325")
crud.criar(c1)

crud.ler()




        
        

   
        

