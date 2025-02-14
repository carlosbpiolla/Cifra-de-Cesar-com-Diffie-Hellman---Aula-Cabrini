## Descrição
Este projeto implementa um servidor e um cliente TCP que se comunicam de forma segura utilizando a troca de chaves Diffie-Hellman para gerar uma chave secreta compartilhada. Essa chave é usada para criptografar e descriptografar mensagens via Cifra de César.

## Tecnologias Utilizadas
- Python
- Socket Programming
- Cifra de César
- Algoritmo de troca de chaves Diffie-Hellman

---

## Funcionamento do Sistema

### 1. Cliente (`Simple_tcpClient.py`)
O cliente estabelece uma conexão TCP com o servidor e realiza os seguintes passos:

1. **Gera uma chave secreta 'a'** e usa o algoritmo Diffie-Hellman para calcular um valor `A = (g^a) mod n`.
2. **Envia o valor `A` ao servidor**.
3. **Recebe o valor `B` do servidor** e calcula a chave secreta compartilhada `K = (B^a) mod n`.
4. **Criptografa a mensagem** usando a Cifra de César com a chave `K` e a envia ao servidor.
5. **Recebe a resposta do servidor**, que foi processada e retornada.

### 2. Servidor (`Simple_tcpServer.py`)
O servidor escuta conexões TCP e segue os seguintes passos:

1. **Recebe o valor `A` do cliente**.
2. **Solicita ao usuário uma chave secreta `b`** e calcula `B = (g^b) mod n`.
3. **Envia `B` ao cliente**.
4. **Calcula a chave compartilhada `K = (A^b) mod n`**.
5. **Recebe a mensagem criptografada do cliente** e a **descriptografa usando a chave `K`**.
6. **Processa a mensagem** (converte para maiúsculas, por exemplo) e a envia de volta ao cliente.

---

## Conceitos Utilizados

### Cifra de César
A Cifra de César é um dos métodos mais simples de criptografia, onde cada letra do texto original é deslocada um número fixo de posições no alfabeto. Neste projeto, a chave `K` gerada pelo Diffie-Hellman é utilizada como deslocamento.

Exemplo:
- Texto original: `HELLO`
- Chave: `3`
- Texto criptografado: `KHOOR`

### Diffie-Hellman (Troca de Chaves)
O protocolo Diffie-Hellman permite que duas partes compartilhem uma chave secreta sem nunca transmiti-la diretamente. Isso é feito utilizando um par de números `g` (base) e `n` (módulo), juntamente com chaves secretas escolhidas por cada parte.

Os cálculos são feitos da seguinte maneira:
1. O cliente escolhe `a` e calcula `A = (g^a) mod n`, enviando `A` ao servidor.
2. O servidor escolhe `b` e calcula `B = (g^b) mod n`, enviando `B` ao cliente.
3. Ambos calculam a chave secreta compartilhada:
   - Cliente: `K = (B^a) mod n`
   - Servidor: `K = (A^b) mod n`

Como resultado, ambos obtêm o mesmo valor `K`, que é usado como chave para a Cifra de César.

---

## Como Executar
1. **Inicie o Servidor**
   ```bash
   python Simple_tcpServer.py
   ```
   - O servidor solicitará a chave secreta `b`.

2. **Inicie o Cliente**
   ```bash
   python Simple_tcpClient.py
   ```
   - O cliente solicitará uma mensagem e a chave secreta `a`.

3. **Verifique a comunicação segura** entre o cliente e o servidor.

---

## Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no projeto.

---

## Autor
Desenvolvido por Carlos B. Piolla (082200013), Guilherme S. Cavinato (082200032), Thiago C. Hanna (082200021) e Bruna dos Santos Freitas (082200015).

