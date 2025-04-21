import random

class minesweeper:
    def __init__(self):
        self.rows = 3
        self.column = 3
        self._hidden = [[False]* self.column for _ in range(self.rows)]
        r = random.randint(0, self.rows - 1)
        c = random.randint(0, self.column - 1)
        self._hidden[r][c] = True
        self.visible = [['?' for _ in range(self.column)] for _ in range(self.rows)]
        self.total_safe = self.rows * self.column - 1
        self.opened_safe = 0
        self.game_over = False

    def print_board(self):
        print("Papan saat ini :")
        for row in self.visible:
            print(' '.join(row))
        print()
    
    def reveal(self, row, col):
        if self.visible[row][col] != '?':
            print ("Sudah terbuka")
            return
        
        if self._hidden[row][col]:
            self.visible[row][col] = 'X'
            self.game_over = True
            self.print_board()
            print("BOOM! Kamu kalah!")
        else:
            self.visible[row][col] = '0'
            self.opened_safe += 1
            if self.opened_safe == self.total_safe:
                self.print_board()
                print("Selamat! Kamu menang!")
                self.game_over = True
    
    def play(self):
        print("== Selamat datang di Minesweeper 3x3 ===")
        while not self.game_over:
            self.print_board()
            try:
                r = int(input(f"Pilih baris (1-{self.rows}): ")) - 1
                c = int(input(f"Pilih kolom (1-{self.column}): ")) - 1
            except ValueError:
                print("Input tidak valid, Masukkan angka.")
                continue
            if not (0 <= r < self.rows and 0<=c < self.column):
                print("Koordinat di luar rentang, Coba lagi!")
                continue
            self.reveal(r, c)

if __name__ == "__main__":
    game = minesweeper()
    game.play()