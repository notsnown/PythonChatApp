import socket
import threading

# Configuração do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345        # Porta do servidor

# Função para receber mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nMensagem recebida: {message}")
        except:
            print("Conexão com o servidor perdida.")
            break

# Criando o socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectando ao servidor
    client.connect((HOST, PORT))
    print("Conectado ao servidor. Digite suas mensagens abaixo:")

    # Inicia uma thread para receber mensagens do servidor
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    # Loop para enviar mensagens
    while True:
        message = input("")
        if message.lower() == 'sair':
            break
        client.send(message.encode('utf-8'))

except Exception as e:
    print(f"Erro ao conectar: {e}")

finally:
    client.close()
