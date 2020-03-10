import random


def game(n):
    """Simulate a game in "The Chase" and return amount that the winner received."""
    bank = 0

    def step(player, n):
        """Return next player with dice."""
        r = random.randint(1, 6)
        if r < 3:
            return (player + 1) % n
        if r > 4:
            return (player - 1) % n
        return player
    for i in range(n-1, -1, -1):
        s = 0 # turns
        # beginning of round, 2 random players with dice
        players_with_dices = [random.randint(0, i), random.randint(0, i)]
        # break when one player has two dieces
        while players_with_dices[0] != players_with_dices[1]:
            players_with_dices[0] = step(players_with_dices[0], i+1)
            players_with_dices[1] = step(players_with_dices[1], i+1)
            s += 1

        bank += s**2

    return bank


n = 10
b = []
for i in range(n):
    b.append(game(500))

print(f'{sum(b)/n:.9e}')


