
class TicTacToe:
    def __init__(self, state):
        self.state = state

        self.score = None
        self.has_game_ended = False
        self.optimal_move = (None, None)
    
    def min_max(self, player):
        self.evaluate()

        if self.has_game_ended:
            return self.score

        if player == 'max':
            self.score = -1
            for move in self.get_possible_moves():
                x, y = move[0], move[1]

                # make a move on x, y
                self.state[x][y] = 1

                s = self.min_max('min')
                if s >= self.score:
                    self.score = s
                    self.optimal_move = (x, y)

                self.state[x][y] = 0
        else:
            self.score = 1
            for move in self.get_possible_moves():
                x, y = move[0], move[1]

                # make a move on x, y
                self.state[x][y] = -1

                s = self.min_max('max')
                if s <= self.score:
                    self.score = s
                    self.optimal_move = (x, y)

                self.state[x][y] = 0
        
        return self.score

    def evaluate(self):
        #check the game state and update score and has game ended 
        pass

    
    def get_possible_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    moves.append((i, j))
        
        return moves

    def get_optimal_move(self):
        return self.optimal_move



board = [
    [1, 0, 0],
    [0, 0, -1],
    [0, 0, 0]
]

game = TicTacToe(board)
game.min_max(player = 'max')
print(game.get_optimal_move())



