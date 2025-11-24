import sys
if __name__ == "__main__":  # stop users from running this as a program
    print("this script is not to be run as a stand-alone program!")
    sys.exit(1)

class Puzzle:               # yeah, thait's OOP for you
    def __init__(self, definition):
        if definition["basic-information"]["type"] != "puzzle":
            raise Exception("is not a puzzle!")
        self.name = definition["basic-information"]["name"]
        self.positions = []
        self.moves = {}
        self.position_indexes = {}
        self.space_indexes = {}
        self.color_indexes = {}
        self.colors = {}

        for position in definition["positions"]["positions"]:
            self.positions.append(position)
        
        for move, permutation in definition["moves"].items():
            self.moves[move] = permutation

        for color in definition["visual"]["colors"]:
            self.colors[color[0]] = (color[1][0], color[1][1], color[1][2])
        
        index = 0

        for position in self.positions:          # store what position names have what indexes in positions
            self.position_indexes[position[0]] = index
            index = index + 1

    def apply_move(self, move_name):
        try:
            move = self.moves[move_name]
        except:
            raise Exception("unknown move")
        temporary_positions = []
        for position in self.positions:
            temporary_positions.append([position[0],None])
        
        for position in temporary_positions:
            for swap in move:
                if swap[1] == position[0]:
                    break
            position[1] = self.positions[self.position_indexes[swap[0]]][1]

        self.positions = temporary_positions
