from socket import *

# Função para criptografar a mensagem usando a Cifra de César
def cifra_de_cesar(texto, chave):
    texto_criptografado = ""
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            deslocamento = chave % 26
            if char.islower():
                texto_criptografado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
            elif char.isupper():
                texto_criptografado += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
        else:
            texto_criptografado += char  # Não criptografa caracteres não alfabéticos
    return texto_criptografado

# Função Diffie-Hellman para gerar chave secreta compartilhada
def diffie_hellman(g, n, chave_secreta):
    return pow(g, chave_secreta, n)

# Parâmetros do servidor
serverName = "10.1.70.15"
serverPort = 1300

# Criação do socket do cliente
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Solicita ao usuário os valores de G, N, chave da cifra e mensagem
g = 7
n = 23
sentence = input("Digite a mensagem para enviar: ")

# Passo 1: O cliente escolhe sua chave secreta 'a' (número entre 1 e N-1)
a = int(input(f"Digite sua chave secreta 'a' (número entre 1 e {n-1}): "))

# Passo 2: O cliente calcula A = (G^a) mod N e envia ao servidor
A = diffie_hellman(g, n, a)

# Envia o valor A para o servidor
clientSocket.send(bytes(str(A), "utf-8"))

# Recebe o valor B do servidor
B = int(clientSocket.recv(65000).decode("utf-8"))

# Passo 3: O cliente calcula a chave secreta compartilhada K = (B^a) mod N
K = diffie_hellman(B, n, a)

# Passo 4: Usar a chave secreta compartilhada K para criptografar a mensagem
# A chave compartilhada será usada como deslocamento para a cifra de César
sentence_criptografada = cifra_de_cesar(sentence, K)

# Envia a mensagem criptografada para o servidor
clientSocket.send(bytes(sentence_criptografada, "utf-8"))

# Recebe a resposta do servidor (que deve ser descriptografada)
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence, "utf-8")

# Exibe a resposta recebida (descriptografada, se necessário)
print("R1: ", A)
print("R2: ", B)
print("Chave K: ", K)
print("Mensagem Criptografada: ", sentence_criptografada)
print("Recebido do servidor: ", text)

# Fecha o socket
clientSocket.close()
