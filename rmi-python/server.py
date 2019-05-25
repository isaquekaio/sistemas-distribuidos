import Pyro4
@Pyro4.expose

class calculadora:
    def soma(self,x,y):
        return int(x+y)

    def subt(self,x,y):
        return int(x-y)

    def mult(self,x,y):
        return int(x*y)

    def divi(self,x,y):
        return int(x/y)

print("Servidor iniciado")
daemon = Pyro4.Daemon()             #faça um daemon do Pyro ()

uri = daemon.register(calculadora)  #registra a calculadora como um objeto Pyro
ns = Pyro4.locateNS()               #encontre o servidor de nomes
ns.register('obj', uri)             #registre o objeto com um nome no servidor de nomes
print(uri)

print("Proxy iniciado")             #iniciar o loop de eventos do servidor para aguardar chamadas
daemon.requestLoop()
