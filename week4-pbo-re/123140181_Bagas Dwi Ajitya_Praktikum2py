import random
import sys

class Hangman:
    def __init__(self, words=None, stages=None):
        self.words = words or [
            'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
            'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
            'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
            'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
            'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
        ]
        self.stages = stages or [
            """
                ------
                |    |
                |
                |
                |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |
                |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |   /
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |   / \
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |  --|
                |    |
                |   / \
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |  --|--
                |    |
                |   / \
                |
            ------------
            """
        ]
        self.secret = random.choice(self.words)
        self.guessed_letters = set()
        self.wrong_letters = set()
        self.max_wrong = len(self.stages) - 1

    def display_state(self):
        print(self.stages[len(self.wrong_letters)])
        displayed = ' '.join(
            [ch if ch in self.guessed_letters else '_' for ch in self.secret]
        )
        print(f"Kata: {displayed}")
        if self.wrong_letters:
            print(f"Salah: {', '.join(sorted(self.wrong_letters))}")
        print()

    def guess(self, letter):
        letter = letter.lower()
        if not letter.isalpha() or len(letter) != 1:
            print("Masukkan satu huruf saja!")
            return
        if letter in self.guessed_letters or letter in self.wrong_letters:
            print("Huruf ini sudah ditebak.")
            return
        if letter in self.secret:
            self.guessed_letters.add(letter)
            print(f"Benar! Huruf '{letter}' ada dalam kata.")
        else:
            self.wrong_letters.add(letter)
            print(f"Salah! Huruf '{letter}' tidak ada dalam kata.")

    def is_won(self):
        return set(self.secret) <= self.guessed_letters

    def is_lost(self):
        return len(self.wrong_letters) >= self.max_wrong

    def play(self):
        print("=== Selamat datang di Hangman OOP ===")
        while True:
            self.display_state()
            if self.is_won():
                print(f"Selamat! Kamu menebak kata: '{self.secret}'")
                break
            if self.is_lost():
                self.display_state()
                print(f"Game over! Kata sebenarnya adalah: '{self.secret}'")
                break
            guess = input("Tebak huruf: ")
            self.guess(guess)

if __name__ == '__main__':
    game = Hangman()
    try:
        game.play()
    except KeyboardInterrupt:
        print("\nTerima kasih sudah bermain!")
        sys.exit()
