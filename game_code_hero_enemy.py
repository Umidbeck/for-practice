import random

class Character:
    def __init__(self, name, health, attact_power):
        self.name = name
        self.health = health
        self.attact_power = attact_power

    def attact(self, other):
        damage = random.randint(1, self.attact_power)
        other.health -= damage
        print(f"{self.name} {other.name}ga {damage} zarba berdi. {other.name}ning hayoti: {other.health}")

    def is_alive(self):
        return self.health > 0 
    
class Hero(Character):
    def special(self, other):
        damage = random.randint(10,20)
        other.health -= damage

class Enemy(Character):
    pass


hero = Hero("Botir", 100, 15)
enemy = Enemy("Qodir", 80,10)


while hero.is_alive() and enemy.is_alive():
    action = input("Hujum (1) yoki maxsus (2)?")

    if action == '1':
        hero.attact(enemy)
    elif action == '2':
        hero.special(enemy)
    else:
        print('Xato tanlov.')

    if enemy.is_alive():
        enemy.attact(hero)
    else:
        print(f"{enemy.name} mag'lub bo'ldi!")

    if not hero.is_alive():
        print(f"{hero.name} yutqazdi... O'yin tugadi.")