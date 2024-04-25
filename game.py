art = r"""
/__ __\/ \/   _\  /__ __\/  _ \/   _\  /__ __\/  _ \/  __/
  / \  | ||  /      / \  | / \||  /      / \  | / \||  \  
  | |  | ||  \_     | |  | |-|||  \_     | |  | \_/||  /_ 
  \_/  \_/\____/    \_/  \_/ \|\____/    \_/  \____/\____\ 
by Gáspár Németh
"""


class TicTacToe:
    def __init__(self):
        # initialize every square as empty
        self.a1 = " "
        self.a2 = " "
        self.a3 = " "
        self.b1 = " "
        self.b2 = " "
        self.b3 = " "
        self.c1 = " "
        self.c2 = " "
        self.c3 = " "

        # print header art
        print(art)

        self.show_board()
        self.x_turn()

    def show_board(self):
        # print out the current board with A-B-C and 1-2-3 coordinate markers
        print("    A   B   C")
        print("   -----------")
        print(f"1 | {self.a1} | {self.b1} | {self.c1} |")
        print("  |-----------|")
        print(f"2 | {self.a2} | {self.b2} | {self.c2} |")
        print("  |-----------|")
        print(f"3 | {self.a3} | {self.b3} | {self.c3} |")
        print("   -----------")

    def x_turn(self):
        # ask for X player's input
        move = input("Choose a cell for X: \n").lower()

        try:
            # if the square is empty, put X mark
            if self.__dict__[move] == " ":
                self.__dict__[move] = "X"
            else:
                print("Invalid move, please try again.")
                self.x_turn()

        # catch invalid coordinate input
        except KeyError:
            print("Invalid move, please try again.")
            self.x_turn()

        else:
            self.show_board()
            self.check_winner()
            self.o_turn()

    def o_turn(self):
        # ask for O player's input
        move = input("Choose a cell for O: \n").lower()

        try:
            # if the square is empty, put O mark
            if self.__dict__[move] == " ":
                self.__dict__[move] = "O"
            else:
                print("Invalid move, please try again.")
                self.o_turn()

        # catch invalid coordinate input
        except KeyError:
            print("Invalid move, please try again.")
            self.o_turn()

        else:
            self.show_board()
            self.check_winner()
            self.x_turn()

    def check_winner(self):
        # sort squares into rows and diagonals
        row_a = self.a1 + self.a2 + self.a3
        row_b = self.b1 + self.b2 + self.b3
        row_c = self.c2 + self.c2 + self.c3
        col_1 = self.a1 + self.b1 + self.c1
        col_2 = self.a2 + self.b2 + self.c2
        col_3 = self.a3 + self.b3 + self.c3
        dia_1 = self.a1 + self.b2 + self.c3
        dia_2 = self.a3 + self.b2 + self.c1
        lines = [row_a, row_b, row_c, col_1, col_2, col_3, dia_1, dia_2]

        # check if any row, column or diagonal is filled with the same marks
        for line in lines:
            if line == "XXX":
                print("X won. Congrats!")
                self.go_again()
            elif line == "OOO":
                print("O won. Congrats!")
                self.go_again()
            else:
                # check if board is full
                if " " not in ",".join(lines):
                    print("It's a draw.")
                    self.go_again()

    def go_again(self):
        # ask user if they want to play again
        choice = input("Play again? Y/N\n").lower()
        if choice == "y":
            self.__init__()
        elif choice == "n":
            exit()
        else:
            print("Invalid answer.")
            self.go_again()
