import random


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.coins = 0
        self.clues = 0
        self.inventory = []

    def show_status(self):
        print("\n" + "=" * 45)
        print("🧭 PLAYER STATUS")
        print("=" * 45)
        print(f"Name       : {self.name}")
        print(f"Health     : {self.health}")
        print(f"Coins      : {self.coins}")
        print(f"Clues      : {self.clues}")
        print(f"Inventory  : {self.inventory}")
        print("=" * 45)

    def take_damage(self, damage):
        self.health -= damage
        print(f"\n💥 You lost {damage} health!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"\n🎒 You found: {item}")


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def explore(self, player):
        print("\n" + "=" * 45)
        print(f"📍 {self.name}")
        print("=" * 45)
        print(self.description)

        event = random.randint(1, 4)

        if event == 1:
            coins = random.randint(10, 50)
            player.coins += coins
            print(f"\n💰 You found {coins} coins!")

        elif event == 2:
            player.clues += 1
            print("\n🔍 You discovered a treasure clue!")

        elif event == 3:
            damage = random.randint(10, 30)
            player.take_damage(damage)
            print("🪤 You triggered a hidden trap!")

        else:
            player.add_item("Mysterious Key")
            print("🗝️ Nobody knows what this key opens...")

        return False


class TreasureLocation(Location):
    def explore(self, player):
        print("\n" + "=" * 45)
        print(f"🏴‍☠️ {self.name}")
        print("=" * 45)
        print(self.description)

        if player.clues >= 3:
            print("\n✨ The mysterious door opens...")
            print("💎 GOLD! JEWELS! ANCIENT ARTIFACTS!")
            print("\n🏆 YOU FOUND THE TREASURE! 🏆")
            return True

        needed = 3 - player.clues

        print("\n🔒 The treasure chamber is locked!")
        print(f"🔍 You need {needed} more clue(s).")

        return False


def game():
    print("\n" + "=" * 55)
    print("🗺️  THE LOST TREASURE")
    print("=" * 55)

    print("\nWelcome, brave explorer!")
    print("Find 3 clues and unlock the legendary treasure.")
    print("But be careful... the map is not exactly trustworthy. 😂")

    name = input("\nEnter your explorer name: ").strip()

    if not name:
        name = "Unknown Explorer"

    player = Player(name)

    locations = [
        Location(
            "Dark Forest",
            "Tall trees surround you. Something is watching..."
        ),
        Location(
            "Abandoned Village",
            "Broken houses and mysterious footprints cover the ground."
        ),
        Location(
            "Ancient Temple",
            "A giant stone temple stands silently before you."
        ),
        Location(
            "Crystal Cave",
            "The walls sparkle with strange glowing crystals."
        ),
        TreasureLocation(
            "Hidden Treasure Chamber",
            "A massive golden door stands deep inside the mountain."
        )
    ]

    visited = set()

    while player.health > 0:

        print("\n" + "=" * 45)
        print("🗺️  AVAILABLE LOCATIONS")
        print("=" * 45)

        for i, location in enumerate(locations, start=1):
            print(f"{i}. {location.name}")

        status_choice = len(locations) + 1
        exit_choice = len(locations) + 2

        print(f"{status_choice}. 🎒 Check Status")
        print(f"{exit_choice}. 🚪 Exit Game")

        try:
            choice = int(input("\nChoose your destination: "))

            if choice == status_choice:
                player.show_status()
                continue

            if choice == exit_choice:
                print("\n🚪 You left the treasure hunt.")
                print("The treasure will miss you. Probably. 😂")
                break

            if choice < 1 or choice > len(locations):
                print("\n❌ Invalid choice.")
                continue

            location = locations[choice - 1]

            if location.name in visited:
                print("\n⚠️ You already explored this location!")
                continue

            visited.add(location.name)

            treasure_found = location.explore(player)

            if treasure_found:
                print("\n" + "=" * 45)
                print("🎉 MISSION COMPLETE!")
                print("=" * 45)
                print(f"Explorer       : {player.name}")
                print(f"Clues Found    : {player.clues}")
                print(f"Coins Collected: {player.coins}")
                print(f"Health Remaining: {player.health}")
                print("\n💎 The legendary treasure is yours!")
                print("🏆 Congratulations, Explorer!")
                break

        except ValueError:
            print("\n❌ Please enter a valid number.")

    if player.health <= 0:
        print("\n" + "=" * 45)
        print("💀 GAME OVER")
        print("=" * 45)
        print("The treasure hunt defeated you. 😭")
        print("Better luck next expedition!")


game()