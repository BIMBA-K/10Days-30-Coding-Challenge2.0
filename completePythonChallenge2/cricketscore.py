def cricket_scoreboard():
    players = {}

    while True:
        name = input("Enter player name (or 'stop' to finish): ")

        if name.lower() == "stop":
            break

        runs = int(input("Enter runs scored: "))
        players[name] = runs

    if not players:
        print("No player data available.")
        return

    highest = max(players, key=players.get)
    lowest = min(players, key=players.get)

    total = sum(players.values())
    average = total / len(players)

    print("\n------ SCOREBOARD ------")

    for player, score in players.items():
        print(f"{player} : {score}")

    print("\nHighest Scorer:", highest, "-", players[highest])
    print("Lowest Scorer :", lowest, "-", players[lowest])
    print("Total Team Score:", total)
    print("Average Score:", round(average, 2))

    print("\nPlayers scoring 50 or more:")

    found = False
    for player, score in players.items():
        if score >= 50:
            print(player, "-", score)
            found = True

    if not found:
        print("No player scored a half-century.")

cricket_scoreboard()