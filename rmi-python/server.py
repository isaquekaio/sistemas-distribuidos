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
daemon = Pyro4.Daemon()         #make a Pyro daemon

uri = daemon.register(calculadora) #register the Saudacao make as a Pyro object
ns = Pyro4.locateNS()           #find the name server
ns.register('obj', uri)         #register the object with a name in the name server
print(uri)

print("Proxy iniciado")         # start the event loop of the server to wait for calls
daemon.requestLoop()