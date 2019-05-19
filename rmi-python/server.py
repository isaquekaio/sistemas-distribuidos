import Pyro4

@Pyro4.expose
class Saudacao:
    def cumprimentar(self):
        return 'Ola Mundo'

print("Servidor iniciado")
daemon = Pyro4.Daemon()         #make a Pyro daemon

ns = Pyro4.locateNS()           #find the name server
uri = daemon.register(Saudacao) #register the Saudacao make as a Pyro object
ns.register('obj', uri)         #register the object with a name in the name server
print(uri)

print("Proxy iniciado")         # start the event loop of the server to wait for calls
daemon.requestLoop()