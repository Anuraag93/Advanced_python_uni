from math import sqrt


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def _interaction(self):
        return int(input (f"Enter position for player {self.symbol}: "))

    def update_board(self, board):
        while True:
            try:
                position = self._interaction()
                if board[position - 1] == "X" or board[position - 1] == "O":
                    print(position,"has been taken by player", board[position-1], "Please choose a different position.")
                elif board[position - 1] != "X" and board[position - 1] != "O":
                    board[position - 1] = self.symbol
                    gameover = True
                    for b in board:
                        if b != "X" and b != "O":
                            gameover = False
                    return board, gameover
        
            except ValueError:
                print("Invalid value. Please enter an integer")
            except IndexError:
                print(f"Please enter an integer between 1 and {len(board)}")

    def __str__(self):
        return self.symbol


class Board:
    grid = []

    def display_board(self, board):
        size = int(sqrt(len(board)))
        pre_index = 0
        for i in range(size):
            subset = board[pre_index:pre_index+size]
            print(end="\t")
            for j in range(size):
                print(subset[j], end="\t")
            print(end="\n")
            pre_index += size

    def check_board(self, board, gameover):
        # if gameover:
        #     return False
        winner = ""
        row_index, col_index = 0, 0
        size = int(sqrt(len(board)))
        for i in range(size):
            # Check Rows 
            one_row = board[row_index:row_index + size]
            # print(one_row)
            if one_row.count("O") == size:
                # O Wins
                winner = "O"
                break
            elif one_row.count("X") == size:
                # X wins
                winner = "X"
                break
            else:
                row_index = row_index + size
                # print("No Win")

            # Check Columns 
            one_col = []
            col_val = col_index
            for j in range(size):
                one_col.append( board[col_val])
                col_val += size
            # print(one_col)
            if one_col.count("O") == size:
                # O Wins
                winner = "O"
                break
            elif one_col.count("X") == size:
                # X wins
                winner = "X"
                break
            else:
                col_index += 1
                # print("No Win")

        # Check first diagonal starts from the 1st element picking the size + 1 element to check
        if winner == "":
            first_diagonal = []
            first_index = 0
            for j in range(size):
                first_diagonal.append(board[first_index])
                first_index += size + 1
            # print(first_diagonal)
            if first_diagonal.count("O") == size:
                # O Wins
                winner = "O"
            elif first_diagonal.count("X") == size:
                # X wins
                winner = "X"
            # else:
                # print("No Win")
        
        # Check second diagonal starts from size element picking the size - 1 element to check
        if winner == "":
            second_diagonal = []
            second_index = size -1
            for j in range(size):
                second_diagonal.append(board[second_index])
                second_index += size - 1
            # print(second_diagonal)
            if second_diagonal.count("O") == size:
                # O Wins
                winner = "O"
            elif second_diagonal.count("X") == size:
                # X wins
                winner = "X"
            # else:
            #     print("No Win")


        if winner == "" and gameover:
            winner = "draw"

        return winner

        

class GameState:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.turn_toggle = False
        pass

    def turn(self, board):
        player_turn = ""
        p1_count = board.grid.count(str(self.p1))
        p2_count = board.grid.count(str(self.p2))

        # print("p1_count",p1_count,"p2_count",p2_count)
        if p2_count < p1_count:
            # Player 2 plays
            player_turn = self.p2
        else:
            # Player 1 plays
            player_turn = self.p1
        return player_turn

    def place(self, player, old_board):
        new_board, gameover = player.update_board(old_board.grid)
        status = old_board.check_board(new_board, gameover)
        return status

    def game_loop(self, b):
        
        winner = ""
        while winner == "":
            b.display_board(b.grid)
            current_player = self.turn(b)
            winner = self.place(current_player, b)
        b.display_board(b.grid) # show the final Board
        return winner


class InvalidInputError(Exception):
    """Invalid Input"""
    pass


def main_menu():
    global isBegun
    # grid_size = 3 # comment this 
    grid_size = int(input("Please enter the grid size (3 or more): ")) 
    if grid_size > 2:
        grid = list(range(1, (grid_size*grid_size)+1))
        grid = [str(x) for x in grid]

        p1, p2 = Player("O"), Player("X")
        game_state = GameState(p1,p2)
        b = Board()
        b.grid = grid
        winner = game_state.game_loop(b)
        if len(winner) == 1:
            print(f"The game is won by: {winner}.")
        else:
            print(f"No Winner. The game is a {winner}.")
        isBegun = False
    else:
        raise InvalidInputError


def start_menu():
    print("-"*60)
    print("Welcome to the game of Naughts and Crosses")
    print("Please select one of the options below:")
    print("b: Begin the game")
    print("q: Quit the game")
    return input("Your Choice: ")


def naughts_and_crosses_game():
    global isBegun
    isBegun = False
    while True:
        try:
            if isBegun:
                main_menu()
            else:
                # choice = "b" # comment this
                choice = start_menu().lower()
                if choice == "q" or choice == "quit":
                    print("User has quit the game")
                    break
                elif choice == "b":
                    print("The game has begun")
                    isBegun = True
                    main_menu()
                else:
                    raise InvalidInputError()

        except InvalidInputError:
            print("Invalid Input entered. Please try again")
        except ValueError:
            print("Invalid value. Please enter an integer")
        except:
            print("Some unknown error has Occurred !")
            # break

if __name__ == '__main__':
    naughts_and_crosses_game()