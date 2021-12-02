from math import sqrt


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def _interaction(self):
        print(f"Player {self.symbol}: ")

    def update_board(self, board, index):
        self._interaction()
        board[index - 1] = self.symbol
        return board

    def __str__(self):
        return self.symbol


class Board:

    def display_board(board):
        size = int(sqrt(len(board)))
        pre_index = 0
        for i in range(size):
            print(board[pre_index:pre_index+size])
            pre_index += size

        # pass

    def check_board(board, gameover, index, p):
        if gameover:
            return False
        # return True
        if board[index-1] == "X" or board[index-1] == "O":
            return False, board
        elif board[index-1] != "X" and board[index-1] != "O":
            board = p.update_board(board, index)


class GameState:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.turn_toggle = False
        pass

    def turn(self, board):

        player_turn = ""
        try:
            if self.turn_toggle:
                # Player 1 plays
                player_turn = self.p1
            else:
                # Player 2 plays
                player_turn = self.p2


            player_position = int(input (f"Enter position for player {player_turn}: "))
            if 0 < player_position >= len(board):
                print("inside",player_position)
                raise IndexError
            print(player_position)

            return self.place(player_turn, board, player_position) 
        
        except ValueError:
           print("Invalid value. Please enter an integer")
        except IndexError:
           print(f"Please enter an integer between 1 and {len(board)}")
        return False, board

    def place(self, player, old_board, position):
        # Board.check_board(old_board, gameover="*" not in old_board)
        check, new_board = Board.check_board(old_board, False, player, position)
        
        return check, new_board
        

    def game_loop(self, board):
        
        Board.display_board(board)
        # add_x = True
        winner = ""
        while True:
            symbol_added = False
            while not symbol_added:
                symbol_added, board = self.turn(board)
                if symbol_added:
                    self.turn_toggle = not self.turn_toggle
            Board.display_board(board)
            print("Next player turn")
        return winner


class InvalidInputError(Exception):
    """Invalid Input"""
    pass


def main_menu():

    grid_size = 3 # comment this 
    # grid_size = int(input("Please enter the grid size (3 or more): ")) 
    if grid_size > 2:
        grid = list(range(1, (grid_size*grid_size)+1))
        p1, p2 = Player("O"), Player("X")
        game_state = GameState(p1,p2)
        winner = game_state.game_loop(grid)
        print(f"The game is won by: {winner}")
    else:
        raise InvalidInputError


def start_menu():
    print("-"*60)
    print("Welcome to the game of Naughts and Crosses")
    print("Please select one of the options below:")
    print("b: Begin the game")
    print("q: Quit the game")
    return input("Your Choice:")


isBegun = False

while True:
    try:
        if isBegun:
            main_menu()
        else:
            choice = "b" # comment this
            # choice = start_menu()
            if choice == "q" or choice == "Q":
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
    # except:
    #     print("Some unknown error has Occurred !")
    #     break
