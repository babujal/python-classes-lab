class Game():
    def __init__(self ):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.player_turn = 'x'

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def switch_turn(self):
        self.player_turn = self.player_turn = 'o' if self.player_turn == 'x' else 'x'

    def get_move(self):
          while True:
                move = input(f"Enter a valid move (example: a1): ").lower()
                if move not in self.board:
                    print('Invalid input, combine letters from A to B with num from 1 to 3 like a1')
                elif self.board[move] !=None:
                    print('Space already taken, enter the corresponding to an empty space')
                else:
                    return move

    def check_for_winner(self):
        winning_patterns = [
            ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"],
            ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"],
            ["a1", "b2", "c3"], ["c1", "b2", "a3"]
        ]
        for pattern in winning_patterns:
            we_have_a_winner = True
            for position in pattern:
                if self.board[position] != self.player_turn:
                    we_have_a_winner = False
                    break
            if we_have_a_winner:
                return True
        return False    

    def check_for_tie(self):
        return all(value != None for value in self.board.values())  #This line of code takes care of the whle logic below perfectly!
        # for position in self.board.values():
        #     if position == None:
        #         return False
        # return True

    def play_game(self):
        print('Shall we play Tic Tac Toe!?')
        while True:
            self.print_board()
            move = self.get_move()
            self.board[move] = self.player_turn
            print(self.board.values())

            if self.check_for_winner():
                self.print_board()
                print(f'{self.player_turn} wins!')
                break
            elif self.check_for_tie():
                self.print_board()
                print('It is a tie!')
                break
            else: self.switch_turn()

            



game_instance = Game()
game_instance.play_game()

