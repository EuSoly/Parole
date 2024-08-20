import random
import os
import time

# Função para escolher uma letra aleatória de uma lista de letras
def random_letters(*letras):
    return random.choice(letras)

# Função para criar o tabuleiro com letras aleatórias
def tabuleiro():
    le = [
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
    
    parole = [[random_letters(*le[li*4+j]) for j in range(4)] for li in range(4)]
    
    return parole

# Função para imprimir o tabuleiro
def print_board(tab):
    for li in tab:
        print(" | ".join(li))
        print("-" * 13)

# Função para verificar se uma palavra pode ser formada a partir de letras adjacentes
def word_in_tab(tab, palavra):
    rows, cols = len(tab), len(tab[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def dfs(x, y, idx, visited):
        if idx == len(palavra):
            return True
        if (x < 0 or x >= rows or y < 0 or y >= cols or
            (x, y) in visited or tab[x][y] != palavra[idx]):
            return False

        visited.add((x, y))
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
def Time():
    pergunta_tempo = int(input("Escolha quanto tempo uam rodada vai durar \n"))
    os.system("clear")
    return pergunta_tempo

# Função para aplicar reroll no tabuleiro
def reroll_tabuleiro():
    print("\nRerollando o tabuleiro...")
    return tabuleiro()

# Função principal do jogo
def main():
    init = input("Jogar parrole? S/N\n").strip().lower()
    
    if init in ["s", "sim"]:
        os.system("clear")
        print("==============_PAROLE_==============")
        play = True
        time = time()
        start_time = time.time()
        tab = tabuleiro()
        used = set()
        points = 0
    elif init in ["n", "nao"]:
        os.system("clear")
        print("ok, tenha um bom dia")
        play = False
    else:
        print("Resposta inválida.")
        play = False

    if play:
        while play:
            
            time_warped = time.time() - start_time
            time_remain = time - int(time_warped)

           
            if time_remain <= 0:
                os.system("clear")
                print("=========FIM DE TEMPO=======")
                print(f"Pontuação final: {points}")
                break

           
            os.system("clear")
        
            print("==============_PAROLE_==============")
            print_board(tab)
            print(f"Tempo restante: {time_remain} seg")
            print(f"Pontuação atual: {points}")

            # Obter a entrada do usuário
            palavra = input("\nDigite uma palavra:\n").upper()
            
           
            if word_in_tab(tab, palavra):
                if palavra not in used:
                    used.add(palavra)
                    points += len(palavra)  # Adiciona a pontuação baseada no comprimento da palavra
                    print("Certo")
                else:
                    print("Você já usou essa palavra.")
            else:
                print("Errado")

if __name__ == "__main__":
    main()
