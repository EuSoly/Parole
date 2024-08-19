
import random
import os
import time
import sys

print("======REGRAS=======")
print("||você terá uma quantidade de tempo para formar palavras no tabuleiro, lembrando que as paravars só poderão ser formadas com letras adjacentes")
print("||você pode roletar novamente o tabuleiro perdendo 30 segundos de tempo como forma de penalidade")
time.sleep(5)

# random pick
def sorterador_letra(*letras):
    return random.choice(letras)

# random de letras
def tabuleiro():
    letras = [
        ["N","Z","D","V","E","A"],
        ["A","M","E","D","P","C"],
        ["A","H","O","S","M","R"],
        ["U","C","O","T","D","N"],
        ["B","A","L","I","T","A"],
        ["G","U","R","I","L","J"],
        ["I","X","O","B","F","R"],
        ["T","O","C","A","I","A"],
        ["M","F","A","H","E","I"],
        ["S","E","H","I","P","M"],
        ["S","P","T","L","E","U"],
        ["A","B","O","J","Q","M"],
        ["E","R","O","N","D","S"],
        ["R","G","L","O","E","U"],
        ["C","L","S","R","A","E"],
        ["Z","C","H","O","B","G"]
    ]
    
    parole = [[sorterador_letra(*letras[linha*4+j]) for j in range(4)] for linha in range(4)]
    
    return parole

# print do parole
def print_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))
        print("-" * 13)


def palavra_in_tabuleiro(tab, palavra):
    rows, cols = len(tab), len(tab[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def dfs(x, y, idx, visited):
        if idx == len(palavra):
            return True
        if (x < 0 or x >= rows or y < 0 or y >= cols or
            (x, y) in visited or tab[x][y] != palavra[idx]):
            return False

        visited.add((x, y))# Função para escolher uma letra aleatória de uma lista de letras
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            if dfs(nx, ny, idx + 1, visited):
                return True
        visited.remove((x, y))
        return False

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0, set()):
                return True
    return False

# Função para configurar o tempo do jogo
def Tempo():
    pergunta_tempo = int(input("Escolha um tempo para uma rodada durar \n 1| 30seg\n 2| 1min\n 3| 1min e 30seg\n 4| 2min\n"))
    os.system("cls" if os.name == "nt" else "clear")
    if pergunta_tempo == 1:
        a = 30
    elif pergunta_tempo == 2:
        a = 60
    elif pergunta_tempo == 3:
        a = 90
    elif pergunta_tempo == 4:
        a = 120
    return a

# Reroll do tabuleiro
def reroll_tabuleiro():
    print("\nRerollando o tabuleiro...")
    os.system("cls" if os.name == "nt" else "clear")
    return tabuleiro()

# jogo 
def main():
    init = input("Deseja jogar parole? S/N\n").strip().lower()
    
    # pergunta de inicialização
    if init in ["s", "sim"]:
        os.system("cls" if os.name == "nt" else "clear")
        print("==============_PAROLE_==============")
        jogar = True
        tempo = Tempo()
        start_time = time.time()
        tab = tabuleiro()
        print_tabuleiro(tab)
        usadas = set()
        pontuacao = 0
    elif init in ["n", "nao"]:
        os.system("cls" if os.name == "nt" else "clear")
        print("ok, tenha um bom dia")
        jogar = False
    else:
        print("Resposta inválida.")
        jogar = False

    if jogar:
        while jogar:
            # tempo restante
            elapsed_time = time.time() - start_time
            remaining_time = tempo - int(elapsed_time)

            # sem tempo
            if remaining_time <= 0:
                os.system("cls" if os.name == "nt" else "clear")
                print("=========FIM DE TEMPO=======")
                print(f"Pontuação final: {pontuacao}")
                break

            # Atualizar o tempo restante na mesma linha
            sys.stdout.write(f"\rTempo restante: {remaining_time} seg")
            sys.stdout.flush()
            
            palavra = input("\nDigite uma palavra ou 'reroll' para reembaralhar o tabuleiro\n").upper()
            
            if palavra == "REROLL":
                tab = reroll_tabuleiro()
                tempo -= 30  # Penalidade de 30 segundos
                # reset no timer
                start_time = time.time()
                print("Tabuleiro reembaralhado")
                print_tabuleiro(tab)
            elif palavra_in_tabuleiro(tab, palavra):
                if palavra not in usadas:
                    usadas.add(palavra)
                    #pontuacao
                    pontuacao += len(palavra) 
                    print("Certo")
                else:
                    print("Você já usou essa palavra.")
            else:
                print("Errado")
            
            print(f"Pontuação atual: {pontuacao}")

main()
