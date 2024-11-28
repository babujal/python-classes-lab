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

    def play_game(self):
        print('Welcome message')


    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or None} | {b['b1'] or None} | {b['c1'] or None}
            ----------
        2)  {b['a2'] or None} | {b['b2'] or None} | {b['c2'] or None}
            ----------
        3)  {b['a3'] or None} | {b['b3'] or None} | {b['c3'] or None}
        """)
# Define a render        

game_instance = Game()
game_instance.play_game()
game_instance.print_board()

