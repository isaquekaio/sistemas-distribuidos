import Pyro4

#ns = Pyro4.locateNS()

#uri = ns.lookup('obj')

o = Pyro4.Proxy("PYRO:obj_a4957aad203e4c8081944d6be9bddf46@localhost:40459")

print(o.saudacao())