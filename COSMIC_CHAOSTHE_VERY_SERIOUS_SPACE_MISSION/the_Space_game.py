import random
import time


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()


def show_status(player):
    print("\n" + "=" * 45)
    print("🚀 CAPTAIN STATUS")
    print("=" * 45)
    print(f"👨‍🚀 Captain      : {player['name']}")
    print(f"❤️ Health       : {player['health']}")
    print(f"⛽ Fuel         : {player['fuel']}")
    print(f"💎 Crystals     : {player['crystals']}")
    print(f"💰 Space Coins  : {player['coins']}")
    print(f"⭐ Score        : {player['score']}")
    print("=" * 45)


def explore_planet(player, planet):
    slow_print(f"\n🪐 Landing on {planet}...")

    event = random.randint(1, 5)

    if event == 1:
        crystals = random.randint(2, 5)
        player["crystals"] += crystals
        player["score"] += crystals * 10
        slow_print(
            f"💎 You found {crystals} cosmic crystals!"
        )

    elif event == 2:
        coins = random.randint(20, 80)
        player["coins"] += coins
        player["score"] += coins
        slow_print(
            f"💰 You found {coins} Space Coins!"
        )

    elif event == 3:
        damage = random.randint(10, 30)
        player["health"] -= damage
        slow_print(
            f"👽 An alien sneezed radioactive dust at you!"
        )
        slow_print(
            f"💥 You lost {damage} health."
        )

    elif event == 4:
        fuel = random.randint(10, 25)
        player["fuel"] += fuel
        player["score"] += 15
        slow_print(
            f"⛽ You found a mysterious fuel station."
        )
        slow_print(
            f"You gained {fuel} fuel."
        )

    else:
        slow_print(
            "😂 You found... absolutely nothing."
        )
        slow_print(
            "The planet has officially wasted your time."
        )

    player["fuel"] -= 10


def alien_battle(player):
    slow_print("\n👽 ALERT! ALIEN DETECTED!")
    slow_print(
        "The alien says: 'Pay me 30 coins or fight me.'"
    )

    while True:
        print("\n1. Fight")
        print("2. Pay 30 coins")
        print("3. Run away like a professional coward")

        try:
            choice = int(input("Choose: "))

            if choice == 1:
                player_attack = random.randint(10, 30)
                alien_health = random.randint(20, 50)

                slow_print(
                    f"\n⚔️ You attack for {player_attack} damage!"
                )

                if player_attack >= alien_health:
                    player["score"] += 100
                    player["crystals"] += 2
                    slow_print(
                        "🎉 YOU DEFEATED THE ALIEN!"
                    )
                    slow_print(
                        "The alien has filed a complaint."
                    )
                else:
                    damage = random.randint(10, 25)
                    player["health"] -= damage

                    slow_print(
                        f"👽 The alien survived!"
                    )
                    slow_print(
                        f"💥 You lost {damage} health."
                    )

                return

            elif choice == 2:
                if player["coins"] >= 30:
                    player["coins"] -= 30
                    slow_print(
                        "💰 You paid the alien."
                    )
                    slow_print(
                        "The alien says: 'Good human.'"
                    )
                else:
                    slow_print(
                        "😂 You don't even have 30 coins."
                    )
                    slow_print(
                        "The alien is now offended."
                    )
                    player["health"] -= 10

                return

            elif choice == 3:
                slow_print(
                    "🏃 You escaped at maximum speed."
                )
                slow_print(
                    "Your dignity did not survive."
                )
                player["fuel"] -= 15
                return

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a number.")


def repair_ship(player):
    if player["coins"] >= 40:
        player["coins"] -= 40
        player["health"] = min(100, player["health"] + 30)

        slow_print(
            "\n🔧 Ship repaired!"
        )
        slow_print(
            "❤️ You gained 30 health."
        )
    else:
        slow_print(
            "\n💸 You need 40 Space Coins for repairs."
        )


def game():
    print("\n" + "=" * 55)
    print("🚀🌌  COSMIC CHAOS  🌌🚀")
    print("=" * 55)

    slow_print(
        "\nWelcome, brave astronaut!"
    )

    slow_print(
        "Your mission is simple..."
    )

    slow_print(
        "Collect 10 cosmic crystals and return to Earth."
    )

    slow_print(
        "Unfortunately, the universe has other plans."
    )

    name = input("\nEnter your astronaut name: ").strip()

    if not name:
        name = "Captain Nobody"

    player = {
        "name": name,
        "health": 100,
        "fuel": 100,
        "crystals": 0,
        "coins": 100,
        "score": 0
    }

    planets = [
        "Mars",
        "Jupiter",
        "Neptune",
        "Saturn",
        "Moon",
        "Pluto"
    ]

    visited = set()

    while True:

        if player["health"] <= 0:
            print("\n💀 GAME OVER!")
            slow_print(
                "Your space career lasted approximately 7 minutes."
            )
            break

        if player["fuel"] <= 0:
            print("\n⛽ OUT OF FUEL!")
            slow_print(
                "You are now officially a satellite."
            )
            break

        if player["crystals"] >= 10:
            print("\n" + "=" * 55)
            print("🏆 MISSION SUCCESS!")
            print("=" * 55)

            slow_print(
                f"Captain {player['name']} returned to Earth!"
            )
            slow_print(
                f"💎 Crystals collected: {player['crystals']}"
            )
            slow_print(
                f"⭐ Final Score: {player['score']}"
            )

            if player["score"] >= 500:
                slow_print(
                    "👑 NASA has promoted you to Supreme Space Legend."
                )
            else:
                slow_print(
                    "👏 NASA says: 'Good enough. Please don't break anything.'"
                )

            break

        print("\n" + "=" * 45)
        print("🚀 SPACE CONTROL CENTER")
        print("=" * 45)

        print("1. 🪐 Explore a Planet")
        print("2. 👽 Fight an Alien")
        print("3. 🔧 Repair Ship")
        print("4. 📊 Check Status")
        print("5. 🌍 Return to Earth")

        try:
            choice = int(input("\nChoose an action: "))

            if choice == 1:

                available_planets = [
                    planet for planet in planets
                    if planet not in visited
                ]

                if not available_planets:
                    slow_print(
                        "\nYou've already visited every planet."
                    )
                    continue

                print("\nAvailable Planets:")

                for i, planet in enumerate(
                    available_planets, start=1
                ):
                    print(f"{i}. {planet}")

                try:
                    selection = int(
                        input("Choose a planet: ")
                    )

                    if 1 <= selection <= len(available_planets):
                        planet = available_planets[
                            selection - 1
                        ]

                        visited.add(planet)
                        explore_planet(
                            player, planet
                        )

                        if random.randint(1, 3) == 1:
                            alien_battle(player)

                    else:
                        print("Invalid planet.")

                except ValueError:
                    print("Please enter a number.")

            elif choice == 2:
                alien_battle(player)

            elif choice == 3:
                repair_ship(player)

            elif choice == 4:
                show_status(player)

            elif choice == 5:
                slow_print(
                    "\n🌍 Returning to Earth..."
                )

                if player["crystals"] >= 10:
                    slow_print(
                        "🏆 Mission accomplished!"
                    )
                else:
                    slow_print(
                        f"You still need "
                        f"{10 - player['crystals']} crystals."
                    )

            else:
                print("Invalid choice.")

        except ValueError:
            print(
                "🚨 Captain, please enter a valid number!"
            )

    print("\nThanks for playing COSMIC CHAOS! 🚀")


game()