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
        print(f"name: {self.name}")

        for position in definition["positions"]["positions"]:
            self.positions.append(position)
        
        for move, permutation in definition["moves"].items():
            self.moves[move] = permutation

        print(f"positions:\n{self.positions}")
        print(f"moves:\n{self.moves}")
