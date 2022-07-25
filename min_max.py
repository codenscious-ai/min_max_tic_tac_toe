
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

                # Clean the move on x, y
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

                # Clean the move on x, y
                self.state[x][y] = 0
        
        return self.score

    def evaluate(self):
       
        for i in range(3):
            if (self.state[i][0] != 0 and self.state[i][0] == self.state[i][1] 
                and self.state[i][1] == self.state[i][2]):
                
                self.score = 1 if self.state[i][0] == 1 else -1
                self.has_game_ended = True
                
                return self.score, self.has_game_ended

        for i in range(3):
            if (self.state[0][i]!= 0 and self.state[0][i] == self.state[1][i] 
                and self.state[1][i] == self.state[2][i]):
                self.score = 1 if self.state[0][i] == 1 else -1
                self.has_game_ended = True
                
                return self.score, self.has_game_ended

        #checking left diagonal
        if (self.state[0][0] != 0 and self.state[0][0] == self.state[1][1] and
            self.state[1][1] == self.state[2][2]):
                self.score = 1 if self.state[i][0] == 1 else -1
                self.has_game_ended = True

                return self.score, self.has_game_ended
        
        #checking right diagonal
        if (self.state[0][2] != 0 and self.state[0][2] == self.state[1][1] and
            self.state[1][1] == self.state[2][0]):
                self.score = 1 if self.state[i][0] == 1 else -1
                self.has_game_ended = True

                return self.score, self.has_game_ended
                

        #Game has ended with draw        
        moves = self.get_possible_moves()
        if len(moves) == 0: 
            self.score = 0
            self.has_game_ended = True
        
        #Game has not ended.
        else:
            self.score = None
            self.has_game_ended = False

        return self.score, self.has_game_ended
            

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
    [1, 1, -1],
    [-1, -1, 1],
    [1, 1, -1]
]

game = TicTacToe(board)
# game.min_max(player = 'max')
# print(game.get_optimal_move())


game.evaluate()
print(game.has_game_ended, game.score)


