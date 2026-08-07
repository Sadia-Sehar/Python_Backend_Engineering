# --------- Character (Base Class) ---------
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health  
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        self._health = max(0, value)
    @property
    def is_alive(self):
        return self._health > 0
    def take_damage(self, amount):
        self.health -= amount  
    def __str__(self):
        return f"{self.name} | HP: {self.health}"
    
# -------- Player --------
class Player(Character):
    max_health = 100
    total_players = 0
    def __init__(self, name):
        super().__init__(name, Player.max_health)
        self.inventory = []   
        Player.total_players += 1
    @Character.health.setter
    def health(self, value):
        self._health = max(0, min(value, Player.max_health))
    def pick_up(self, item):
        self.inventory.append(item)
        return f"{self.name} picked up {item.name}."
    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.heal_amount > 0:
                    self.health += item.heal_amount
                    self.inventory.remove(item)
                    return f"{item.name} used! +{item.heal_amount} HP"
                return "Item cannot be used."
        return "Item not found."
    def __str__(self):
        items = [item.name for item in self.inventory]
        return f"{self.name} | HP: {self.health} | Bag: {items}"

# -------- Monster --------
class Monster(Character):
    total_monsters = 0
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage
        Monster.total_monsters += 1
    def attack(self, target):
        target.take_damage(self.damage)
        return f"{self.name} attacked {target.name} for {self.damage} damage!"
    def __str__(self):
        return f"{self.name} | HP: {self.health} | Damage: {self.damage}"

# -------- Item --------
class Item:
    def __init__(self, name, heal_amount=0):
        self.name = name
        self.heal_amount = heal_amount
    def __str__(self):
        return self.name

# -------- Room (Composition-Aggregation) --------
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.monster = None
        self.exits = {}
    def add_exit(self, direction, room):
        self.exits[direction] = room
    def add_item(self, item):
        self.items.append(item)
    def set_monster(self, monster):
        self.monster = monster
    def take_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        return None
    def __str__(self):
        item_names = [item.name for item in self.items]
        exits = list(self.exits.keys())
        return f"\n{self.name}\n{self.description}\nItems: {item_names}\nExits: {exits}"

# -------- Game --------
class Game:
    def __init__(self, player, start_room):
        self.player = player
        self.current_room = start_room
    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print("You moved to", self.current_room.name)
        else:
            print("You can't go that way.")
    def play(self):
        while self.player.is_alive:
            print("\n" + str(self.player))
            print(self.current_room)

            if self.current_room.monster and self.current_room.monster.is_alive:
                print("A monster is here:", self.current_room.monster)

            print("\nActions: move / take / use / attack / quit")
            choice = input("Choose action: ").lower()

            if choice == "move":
                direction = input("Direction: ").lower()
                self.move(direction)

            elif choice == "take":
                item_name = input("Item name: ")
                item = self.current_room.take_item(item_name)
                if item:
                    print(self.player.pick_up(item))
                else:
                    print("Item not found.")

            elif choice == "use":
                item_name = input("Item name: ")
                print(self.player.use_item(item_name))

            elif choice == "attack":
                monster = self.current_room.monster
                if monster and monster.is_alive:
                    monster.take_damage(20)
                    print("You attacked the monster for 20 damage.")
                    if monster.is_alive:
                        print(monster.attack(self.player))
                    else:
                        print("Monster defeated!")
                else:
                    print("No monster here.")

            elif choice == "quit":
                print("Game ended.")
                break
            else:
                print("Invalid choice.")

        if not self.player.is_alive:
            print("You died. Game Over.")

# -------- Setup World --------
potion = Item("Potion", 20)
forest = Room("Forest", "You are in a dark forest.")
cave = Room("Cave", "A cold cave with strange sounds.")
forest.add_exit("north", cave)
cave.add_exit("south", forest)
forest.add_item(potion)
goblin = Monster("Goblin", 40, 15)
cave.set_monster(goblin)
player = Player("Hero")

print("Total Players:", Player.total_players)
print("Total Monsters:", Monster.total_monsters)

game = Game(player, forest)
game.play()