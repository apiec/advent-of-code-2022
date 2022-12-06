from io import TextIOWrapper

class Sign:
    def __init__(self, points: int, lose: str, win: str):
        self.points: int = points
        self.lose: str = lose
        self.win: str = win

signs: dict[str: Sign] = {
    'rock': Sign(points=1, lose='paper', win='scissors'),
    'paper': Sign(points=2, lose='scissors', win='rock'),
    'scissors': Sign(points=3, lose='rock', win='paper')
}

opponentMap = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

myMap = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

def get_points_for_round_v1(op, me):
    op, me = opponentMap[op], myMap[me]
    mySign = signs[me]
    if mySign.win == op:
        return 6 + mySign.points
    elif mySign.lose == op:
        return mySign.points
    else:
        return 3 + mySign.points

def get_points_for_round_v2(op, strat):
    op = opponentMap[op]
    if strat == 'X':
        mySign = signs[signs[op].win]
        return mySign.points
    elif strat == 'Y':
        mySign = signs[op]
        return 3 + mySign.points
    elif strat == 'Z':
        mySign = signs[signs[op].lose]
        return 6 + mySign.points
    
f = open('./input.txt', 'r')

total1 = total2 = 0
for line in f.readlines():
    A, B = line[:-1].split()
    total1 += get_points_for_round_v1(A, B)
    total2 += get_points_for_round_v2(A, B)

print(total1, total2)