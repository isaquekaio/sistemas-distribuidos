from socket import*
def main():
    host = ""              # Endereco IP do Servidor
    port = 5000            # Porta que o Servidor esta

    server = socket(AF_INET, SOCK_DGRAM)    #Criar socket
    
    print("Servidor iniciado")

    while True:
        #Receber a data e o endereço de conexão
        data, endereco = server.recvfrom(1024)

        #Imprimir as informações da conexão
        print("Mensagem recebida de ", str(endereco))
        print("Recebemos do cliente: ", str(data))

        #Vamos  mandar de volta a mensagem em eco
        resposta = "Eco==>" +str(data)
        server.sendto(data, endereco)

    #Fechando o serveirdor    
    server.close()
 
if __name__ == '__main__':
    main()

#video: https://www.youtube.com/watch?v=98CGGGiBX5k