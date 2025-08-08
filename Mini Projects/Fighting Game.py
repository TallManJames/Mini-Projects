import random

class character:
    def __init__(self, health, power, dodge, accuracy):
        self.health = health
        self.power = power
        self.dodge = dodge
        self.accuracy = accuracy
        self.heal_remaining = True
    def take_damage(self, damage):
        self.health -= int(damage)
    def light_attack(self):
        if random.randint(1,100) <= self.accuracy:
            return self.power
        else:
            return 0
    def heavy_attack(self):
        temp_accuracy = self.accuracy * .7
        if random.randint(1,100) <= temp_accuracy:
            return int(self.power * 1.5)
        else:
            print("MISSED!")
            return 0
    def healing(self):
        if self.heal_remaining == True:
            self.health = max_health
            print("Fully recovered!")
            self.heal_remaining = False
        else:
            print("No heals remaining!")

base_stats = character(100,20,10,100)

#warrior ↑health10% and ↑power20%
class warrior(character):
    def __init__(self, health, power, dodge, accuracy):
        health = int(health*1.1)
        power = int(power*1.2)
        super().__init__(health, power, dodge, accuracy)
    def take_damage(self, damage):
        super().take_damage(damage)
    def light_attack(self):
        return super().light_attack()
    def heavy_attack(self):
        return super().heavy_attack()
    def healing(self):
        return super().healing()

warrior_class = warrior(base_stats.health, base_stats.power, base_stats.dodge, base_stats.accuracy)

#knight ↑health30% and ↓dodge=0
class knight(character):
    def __init__(self,  health, power, dodge, accuracy):
        health = int(health*1.3)
        dodge = 0
        super().__init__(health, power, dodge, accuracy)
    def take_damage(self, damage):
        super().take_damage(damage)
    def light_attack(self):
        return super().light_attack()
    def heavy_attack(self):
        return super().heavy_attack()
    def healing(self):
        return super().healing()

knight_class = knight(base_stats.health, base_stats.power, base_stats.dodge, base_stats.accuracy)

#ninja ↓health25% and ↑dodge200%
class ninja(character):
    def __init__(self,  health, power, dodge, accuracy):
        health = int(health*.75)
        dodge = int(dodge*3)
        super().__init__(health, power, dodge, accuracy)
    def take_damage(self, damage):
        super().take_damage(damage)
    def light_attack(self):
        return super().light_attack()
    def heavy_attack(self):
        return super().heavy_attack()
    def healing(self):
        return super().healing()

ninja_class = ninja(base_stats.health, base_stats.power, base_stats.dodge, base_stats.accuracy)

lvlOneEnemy = character(int(.8*base_stats.health), int(.8*base_stats.power), 0, base_stats.accuracy)
lvlTwoEnemy = character(base_stats.health, base_stats.power, 0, base_stats.accuracy)
lvlThreeEnemy = character(int(1.3*base_stats.health), int(1.3*base_stats.power), 0, base_stats.accuracy)

print("\nHello, welcome to my fighting game!\n")

print('Warrior: wields an axe and medium armor' 
    f'\nHealth-{warrior_class.health} Power-{warrior_class.power} Dodge-{warrior_class.dodge}\n')
print('Knight: wields a sword and heavy armor'
    f'\nHealth-{knight_class.health} Power-{knight_class.power} Dodge-{knight_class.dodge}\n')
print('Ninja: wields a dagger and light armor'
    f'\nHealth-{ninja_class.health} Power-{ninja_class.power} Dodge-{ninja_class.dodge}\n')

while True:
    while True:
        character_choice = input("Which class will you play as?:\n")
        if character_choice.lower() == "warrior":
            selected_character = warrior_class
            break
        elif character_choice.lower() == "knight":
            selected_character = knight_class
            break
        elif character_choice.lower() == "ninja":
            selected_character = ninja_class
            break
        else:
            print("\nError with selected class, please select between:\nWarrior, Knight, or Ninja")

    character_name = input("Next, what is your name challenger?:\n")

    print(f"Just to make sure... your name is {character_name.capitalize()}, and you are a {character_choice.capitalize()}?")
    
    check = input("If this is correct, say continue: ")
    if check.lower() == "continue":
        break
    else:
        print("Ok, let's try again!")
    
max_health = selected_character.health

print("\nAlright! Here are some general tips to get you started:\n1. Only your character has a chance to dodge\n2. There are 3 levels total" \
    "\n3. You must select which attack you would like:\n     A regular attack with a guarateed chance to hit, "
    "or a strong attack with 50% more power, but 70% the accuracy"
    "\n4. You have ONE full health recovery"
    "\n5. And most importantly, have fun!")

print("\nIt is time for your first challenge!\nFor this challenge, you will face off an easy enemy" \
    f" with {lvlOneEnemy.health} health, and {lvlOneEnemy.power} power!")

lvl_counter = 1

#level 1
while True:
    print(f"\nYou have {selected_character.health} health remaining, and the enemy has {lvlOneEnemy.health} health remaining")
    while True:
        attack_selection = input("Which attack will you use? Or would you rather heal? 'Light' / 'Heavy' / 'Heal'?\n")
        if attack_selection.lower() == "light":
            damage = selected_character.light_attack()
            lvlOneEnemy.take_damage(damage)
            break
        elif attack_selection.lower() == "heavy":
            damage = selected_character.heavy_attack()
            lvlOneEnemy.take_damage(damage)
            break
        elif attack_selection.lower() == "heal":
            selected_character.healing()
            break
        else:
            print("Invalid attack selection, try again.")
        
    if lvlOneEnemy.health <= 0:
        print("The enemy has been slain!")
        lvl_counter += 1
        break
    else:    
        print(f"You hit the enemy for {damage} damage! Now the enemy is attacking...")
        
        hit_chance = 100 - (selected_character.dodge)
        if random.randint(1,100) <= hit_chance:
            enemy_damage = lvlOneEnemy.power
            selected_character.take_damage(enemy_damage)
            print(f"You got hit for {enemy_damage} damage!")
        else:
            print("They missed! No damage!")
        
    if selected_character.health <= 0:
        print("Game Over...")
        break
    else:
        pass

#level 2
if lvl_counter != 2:
    pass
else:
    print("\nCongratulations! Now it is time for your challenge two!\nFor this challenge, you will face off a standard enemy" \
    f" with {lvlTwoEnemy.health} health, and {lvlTwoEnemy.power} power!")
    while True:
        print(f"\nYou have {selected_character.health} health remaining, and the enemy has {lvlTwoEnemy.health} health remaining")
        while True:
            attack_selection = input("Which attack will you use? Or would you rather heal? 'Light' / 'Heavy' / 'Heal'?\n")
            if attack_selection.lower() == "light":
                damage = selected_character.light_attack()
                lvlTwoEnemy.take_damage(damage)
                break
            elif attack_selection.lower() == "heavy":
                damage = selected_character.heavy_attack()
                lvlTwoEnemy.take_damage(damage)
                break
            elif attack_selection.lower() == "heal":
                selected_character.healing()
                break
            else:
                print("Invalid attack selection, try again.")
            
        if lvlTwoEnemy.health <= 0:
            print("The enemy has been slain!")
            lvl_counter += 1
            break
        else:    
            print(f"You hit the enemy for {damage} damage! Now the enemy is attacking...")
            
            hit_chance = 100 - (selected_character.dodge)
            if random.randint(1,100) <= hit_chance:
                enemy_damage = lvlTwoEnemy.power
                selected_character.take_damage(enemy_damage)
                print(f"You got hit for {enemy_damage} damage!")
            else:
                print("They missed! No damage!")
            
        if selected_character.health <= 0:
            print("Game Over...")
            break
        else:
            pass

#level 3
if lvl_counter != 3:
    pass
else:
    print("\nLastly for you third challenge!\nFor this challenge, you will face off a difficult enemy" \
    f" with {lvlThreeEnemy.health} health, and {lvlThreeEnemy.power} power!")
    while True:
        print(f"\nYou have {selected_character.health} health remaining, and the enemy has {lvlThreeEnemy.health} health remaining")
        while True:
            attack_selection = input("Which attack will you use? Or would you rather heal? 'Light' / 'Heavy' / 'Heal'?\n")
            if attack_selection.lower() == "light":
                damage = selected_character.light_attack()
                lvlThreeEnemy.take_damage(damage)
                break
            elif attack_selection.lower() == "heavy":
                damage = selected_character.heavy_attack()
                lvlThreeEnemy.take_damage(damage)
                break
            elif attack_selection.lower() == "heal":
               selected_character.healing()
               break
            else:
                print("Invalid attack selection, try again.")
            
        if lvlThreeEnemy.health <= 0:
            print("The enemy has been slain!" \
            f"\nCongratulations {character_name.capitalize()}, you won!")
            lvl_counter += 1
            break
        else:    
            print(f"You hit the enemy for {damage} damage! Now the enemy is attacking...")
            
            hit_chance = 100 - (selected_character.dodge)
            if random.randint(1,100) <= hit_chance:
                enemy_damage = lvlThreeEnemy.power
                selected_character.take_damage(enemy_damage)
                print(f"You got hit for {enemy_damage} damage!")
            else:
                print("They missed! No damage!")
            
        if selected_character.health <= 0:
            print("Game Over...")
            break
        else:
            pass