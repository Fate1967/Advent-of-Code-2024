import curses
import random
import string

def geraMatriz(linhas, colunas):
    # Gera matriz de caracteres aleatórios
    return [ [random.choice(string.ascii_letters + string.digits) for _ in range(colunas)] for _ in range (linhas) ]

def main(stdscr):
    # Configurações iniciais
    curses.curs_set(0)      # Oculta cursor
    stdscr.clear()

    linhas, colunas = 80,80

    # Obtém o tamanho máximo da janela do terminal
    max_y, max_x = stdscr.getmaxyx()

    if (linhas > max_y or colunas > max_x):
        stdscr.addstr(0, 0, "A janela é muito pequena")
        stdscr.refresh()
        stdscr.getch()      # Aguarda pressionamento de uma tecla
        return

    while True:
        # Gera os caracteres aleatórios
        matriz = geraMatriz(linhas, colunas)

        # Desenha a matriz na tela
        for i, linha in enumerate(matriz):
            stdscr.addstr(i, 0, ''.join(linha[:colunas]))
        
        stdscr.refresh()        # Atualiza o terminal
        curses.napms(500)       # Pausa por 500 ms

if __name__ == '__main__':
    curses.wrapper(main)
