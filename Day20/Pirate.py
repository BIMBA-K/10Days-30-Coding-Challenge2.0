import random


class Pirate:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 0
        self.map_pieces = 0
        self.inventory = []

    def show_status(self):
        print("\n" + "=" * 40)
        print("🏴‍☠️ PIRATE STATUS")
        print("=" * 40)
        print(f"Name       : {self.name}")
        print(f"Health     : {self.health}")
        print(f"Gold       : {self.gold}")
        print(f"Map Pieces : {self.map_pieces}")
        print(f"Inventory  : {self.inventory}")
        print("=" * 40)

    def take_damage(self, damage):
        self.health -= damage
        print(f"💥 You lost {damage} health!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"🎒 You collected: {item}")


class Island:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def explore(self, pirate):

        print("\n" + "=" * 40)
        print(f"🏝️ {self.name}")
        print("=" * 40)

        print(self.description)

        event = random.randint(1, 4)

        if event == 1:
            gold = random.randint(20, 60)
            pirate.gold += gold
            print(f"\n💰 You discovered {gold} gold coins!")

        elif event == 2:
            pirate.map_pieces += 1
            print("\n🗺️ You found a piece of the treasure map!")

        elif event == 3:
            damage = random.randint(10, 25)
            print("\n🐍 A dangerous creature attacked you!")
            pirate.take_damage(damage)

        else:
            pirate.add_item("Ancient Compass")
            print("🧭 The compass may help you find the treasure.")

        return False


class TreasureIsland(Island):

    def explore(self, pirate):

        print("\n" + "=" * 40)
        print("💀 TREASURE ISLAND")
        print("=" * 40)

        print(self.description)

        if pirate.map_pieces >= 3:

            print("\n🗺️ You combine the three map pieces...")
            print("📍 The map reveals the treasure location!")

            print("\n💎 You dig beneath an ancient palm tree...")
            print("✨ A legendary treasure chest appears!")

            print("\n🏆 YOU FOUND THE PIRATE TREASURE! 🏆")

            return True

        else:

            needed = 3 - pirate.map_pieces

            print("\n🔒 You don't know where the treasure is.")
            print(f"🗺️ Find {needed} more map piece(s).")

            return False


def start_game():

    print("\n" + "=" * 50)
    print("🏴‍☠️ PIRATE ISLAND ADVENTURE")
    print("=" * 50)

    print("\nYou are a pirate searching for legendary treasure.")
    print("Find 3 pieces of the treasure map.")
    print("Then travel to Treasure Island!")

    name = input("\nEnter your pirate name: ").strip()

    if not name:
        name = "Captain Unknown"

    pirate = Pirate(name)

    islands = [

        Island(
            "Skull Island",
            "A dark island filled with strange skull-shaped rocks."
        ),

        Island(
            "Snake Island",
            "You hear snakes moving through the tall grass."
        ),

        Island(
            "Ghost Island",
            "An abandoned pirate village stands near the shore."
        ),

        Island(
            "Volcano Island",
            "Smoke rises from a dangerous active volcano."
        ),

        TreasureIsland(
            "Treasure Island",
            "According to legend, the greatest pirate treasure is buried here."
        )
    ]

    visited = set()

    while pirate.health > 0:

        print("\n" + "=" * 40)
        print("🌊 CHOOSE AN ISLAND")
        print("=" * 40)

        for i, island in enumerate(islands, start=1):
            print(f"{i}. {island.name}")

        status_option = len(islands) + 1
        exit_option = len(islands) + 2

        print(f"{status_option}. 🏴‍☠️ Check Status")
        print(f"{exit_option}. 🚪 Exit Game")

        try:

            choice = int(input("\nWhere do you want to sail? "))

            if choice == status_option:
                pirate.show_status()
                continue

            if choice == exit_option:
                print("\n⛵ You sailed away from the adventure.")
                break

            if choice < 1 or choice > len(islands):
                print("\n❌ Invalid choice!")
                continue

            island = islands[choice - 1]

            if island.name in visited:
                print("\n⚠️ You already explored this island!")
                continue

            visited.add(island.name)

            treasure_found = island.explore(pirate)

            if treasure_found:

                print("\n" + "=" * 40)
                print("🎉 ADVENTURE COMPLETE!")
                print("=" * 40)

                print(f"Pirate     : {pirate.name}")
                print(f"Gold       : {pirate.gold}")
                print(f"Map Pieces : {pirate.map_pieces}")
                print(f"Health     : {pirate.health}")

                print("\n👑 You are now the richest pirate in the world!")

                break

        except ValueError:
            print("\n❌ Please enter a valid number.")

    if pirate.health <= 0:

        print("\n" + "=" * 40)
        print("💀 GAME OVER")
        print("=" * 40)

        print("Your pirate adventure has ended!")


start_game()
