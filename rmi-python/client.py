import Pyro4

ns = Pyro4.locateNS()

uri = ns.lookup('obj')    #o servidor de nomes para facilitar a pesquisa de objetos.

#o = Pyro4.Proxy("PYRO:Pyro.NameServer@localhost:9090")
x=int(input("Digite um numero: "))
y=int(input("Digite outro numero: "))

o = Pyro4.Proxy(uri)
print(o.soma(x,y))
print(o.subt(x,y))
print(o.mult(x,y))
print(o.divi(x,y))
