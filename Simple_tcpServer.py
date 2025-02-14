from socket import *

# Função para descriptografar a mensagem usando a Cifra de César (inverso da criptografia)
def cifra_de_cesar_descriptografar(texto, chave):
    texto_descriptografado = ""
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            deslocamento = chave % 26
            if char.islower():
                texto_descriptografado += chr((ord(char) - ord('a') - deslocamento) % 26 + ord('a'))
            elif char.isupper():
                texto_descriptografado += chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))
        else:
            texto_descriptografado += char  # Não descriptografa caracteres não alfabéticos
    return texto_descriptografado

# Função Diffie-Hellman para gerar chave secreta compartilhada
def diffie_hellman(g, n, chave_secreta):
    return pow(g, chave_secreta, n)

# Parâmetros do servidor
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print("TCP Server\n")
connectionSocket, addr = serverSocket.accept()

# Passo 1: Recebe o valor A do cliente
A = int(connectionSocket.recv(65000).decode("utf-8"))

# Solicita ao servidor o valor de 'b' (chave secreta do servidor)
b = int(input("Digite sua chave secreta 'b' (número entre 1 e N-1): "))

# Parâmetros de Diffie-Hellman (devem ser os mesmos que o cliente usou)
g = 7
n = 23
# Passo 2: O servidor calcula B = (G^b) mod N e envia ao cliente
B = diffie_hellman(g, n, b)
connectionSocket.send(bytes(str(B), "utf-8"))

# Passo 3: O servidor calcula a chave secreta compartilhada K = (A^b) mod N
K = diffie_hellman(A, n, b)

# Passo 4: Recebe a mensagem criptografada do cliente
sentence = connectionSocket.recv(65000).decode("utf-8")

# Passo 5: Descriptografa a mensagem usando a chave K (Cifra de César inversa)
sentence_descriptografada = cifra_de_cesar_descriptografar(sentence, K)

# Exibe a mensagem descriptografada
print("R1: ", A)
print("R2: ", B)
print("Chave K: ", K)
print("Mensagem recebida criptografada: ", sentence)
print("Mensagem descriptografada: ", sentence_descriptografada)

# Envia a resposta ao cliente (após processamento, neste caso, apenas capitalizando)
capitalizedSentence = sentence_descriptografada.upper()

# Envia de volta a mensagem processada ao cliente
connectionSocket.send(bytes(capitalizedSentence, "utf-8"))

# Fecha o socket
connectionSocket.close()
