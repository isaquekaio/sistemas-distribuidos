from socket import*

def main():
    host = "localhost"     # Endereco IP do Servidor
    port = 5000            # Porta que o Servidor esta

    #O servidor será um par endereço e porta
    server = (host, port)

    #Criando o socket
    conexao = socket (AF_INET, SOCK_DGRAM)
    conexao.bind((host, port))

    #Vamos mandar mensagem enquanto for diferente de (s)
    msg = input("->")
    while msg != "s":
        #Mandar a mensagem através da conexão
        conexao.sendto(msg.encode(), server)
        
        #Receber uma resposta do servidor
        data, endereco = conexao.recvfrom(1024)

        #Imprimirndo a mensagem recebida
        print("Recebido -> ", str(data))
        print("Recebido do endereco -> ", str(endereco), "\n")

        #Mandar mais mensagem
        msg = input("->")
    conexao.close()

if __name__ == '__main__':
    main()