import numpy as np

class GameTable:
    def __init__(self, square_matrix):
        # convert strings to table
        table = [[int(i) for i in line.split(' ')] for line in square_matrix]
        self.table = np.array(table)
        self.record = np.zeros(self.table.shape, dtype=int)
        self.already_bingo = False

    def IfBingo(self, number):
        pose = np.where(self.table == number)
        self.record[pose] = 1
        if( (self.record.sum(axis=0).tolist().count(5) > 0) or (self.record.sum(axis=1).tolist().count(5) > 0)):
            self.already_bingo = True
        return self.already_bingo

    def GetAnswer(self, bingo_number):
        remained = 1 - self.record
        multiply = self.table * remained
        sum_matrix = sum(sum(multiply))
        return bingo_number * sum_matrix
    pass

input_lines = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
	    # replace many space to one space
        input_lines.append(' '.join(line.split()))

# get data for each round
play_rounds = [int(i) for i in input_lines[0].split(',')]

# delete first line for matrix pattern
del input_lines[0]

# create tables
spilted_line_groups = [input_lines[i:i+6] for i in range(0, len(input_lines), 6)]
game_tables = [GameTable(line_group[1:6]) for line_group in spilted_line_groups]

# part1
bingo_tables = []
bingo_numbers = []
for current_round in play_rounds:
    if bingo_tables:
        break

    for table in game_tables:
        if(table.IfBingo(current_round)):
            bingo_tables.append(table)
            bingo_numbers.append(current_round)

print(str(bingo_tables[-1].GetAnswer(bingo_numbers[-1])))


# part2
for current_round in play_rounds:
    for table in game_tables:
        if not table.already_bingo:
            if(table.IfBingo(current_round)):
                bingo_tables.append(table)
                bingo_numbers.append(current_round)

print(str(bingo_tables[-1].GetAnswer(bingo_numbers[-1])))
