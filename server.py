import socket
import threading

# Configuração do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 12345        # Porta do servidor

# Lista para armazenar clientes conectados
clients = []

# Função para gerenciar a comunicação com um cliente
def handle_client(client_socket, address):
    print(f"Nova conexão de {address}")
    
    while True:
        try:
            # Recebe mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{address}: {message}")

            # Envia a mensagem para todos os clientes conectados
            broadcast(message, client_socket)
        except:
            break

    print(f"Conexão encerrada: {address}")
    clients.remove(client_socket)
    client_socket.close()

# Função para enviar mensagens a todos os clientes conectados
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

# Inicialização do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criando socket
server.bind((HOST, PORT))  # Vinculando ao IP e porta
server.listen(5)  # Configurando para ouvir conexões
print(f"Servidor rodando em {HOST}:{PORT}")

# Aceita conexões de clientes
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
