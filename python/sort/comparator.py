# Problem link
# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = str(name).lower()
        self.score = int(score)

    def __repr__(self):
        return f"{self.name} {self.score}"

    def comparator(a, b):
        # check alphabetical & numeric compare on each name, score
        if a.score < b.score:
            # change
            return 1
        elif a.score > b.score:
            # don't change
            return -1
        elif a.score == b.score:
            if a.name < b.name:
                # don't change
                return -1
            elif a.name > b.name:
                # change
                return 1
            else:
                return 0

# n = int(input())
n = 5
data = []
temp = [['amy', 100], ['david', 100], ['heraldo', 50], ['aakansha', 75], ['aleksa', 150]]
for i in range(n):
    name, score = temp[i][0], temp[i][1]
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
