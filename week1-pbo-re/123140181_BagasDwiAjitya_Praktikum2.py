import random
import time

class Robot:
    def __init__(self, name, attack, hp, accuracy):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.accuracy = accuracy
        self.is_silence = False
        self.is_shielded = False

    def attack_enemy(self, enemy):
        if random.randint(1, 100) <= self.accuracy:  # Cek apakah serangan berhasil
            damage = self.attack // 2 if enemy.is_shielded else self.attack
            enemy.hp -= damage
            print(f"{self.name} menyerang {enemy.name} dengan {damage} damage! (HP {enemy.name}: {enemy.hp})")
        else:
            print(f"{self.name} gagal menyerang {enemy.name}!")

    def regen_health(self):
        heal = random.randint(1, 10)
        self.hp += heal
        print(f"{self.name} mendapatkan {heal} HP!")

    def use_skill(self, enemy):
        if self.is_silence:
            print(f"{self.name} tidak bisa menggunakan skill karena terkena SILENCE!")
            self.is_silence = False  
            return None

        skill_choice = random.choice(["stun", "silence", "shield"])  

        if skill_choice == "stun":
            if random.random() < 0.3:  # 30% chance to stun
                print(f"{self.name} menggunakan skill STUN! {enemy.name} tidak bisa menyerang di ronde berikutnya!")
                return "stun"

        elif skill_choice == "silence":
            if random.random() < 0.3:  # 30% chance to silence
                print(f"{self.name} menggunakan skill SILENCE! {enemy.name} tidak bisa menggunakan skill di ronde berikutnya!")
                return "silence"

        elif skill_choice == "shield":
            print(f"{self.name} mengaktifkan SHIELD! Serangan musuh akan berkurang 50%!")
            self.is_shielded = True
            return "shield"

        return None

    def is_alive(self):
        return self.hp > 0


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    def start(self):
        print(f"Pertarungan dimulai antara {self.robot1.name} dan {self.robot2.name}!")
        round_num = 1
        stunned_robot = None

        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\n===== Ronde {round_num} =====")
            
            self.robot1.is_shielded = False
            self.robot2.is_shielded = False

            if stunned_robot:
                print(f"{stunned_robot.name} terkena STUN Abyssal Blade dan tidak bisa menyerang!")
                stunned_robot = None  
            else:
                self.robot1.attack_enemy(self.robot2)
                if self.robot2.is_alive():
                    self.robot2.attack_enemy(self.robot1)

            if self.robot1.is_alive():
                effect = self.robot1.use_skill(self.robot2)
                if effect == "stun":
                    stunned_robot = self.robot2
                elif effect == "silence":
                    self.robot2.is_silence = True

            if self.robot2.is_alive():
                effect = self.robot2.use_skill(self.robot1)
                if effect == "stun":
                    stunned_robot = self.robot1
                elif effect == "silence":
                    self.robot1.is_silence = True

            round_num += 1
            time.sleep(1)  

        if self.robot1.is_alive():
            print(f"\n{self.robot1.name} menang!")
        else:
            print(f"\n{self.robot2.name} menang!")

robot1 = Robot("Juggernaut", attack=10, hp=100, accuracy=100)
robot2 = Robot("Phantom Assassin", attack=10, hp=100, accuracy=100)

game = Game(robot1, robot2)
game.start()
