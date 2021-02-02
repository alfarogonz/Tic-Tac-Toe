# player 
# players play the game 
# players have turns and shape they can play
# the game renders a board 
# game checks after every move if the game has been won =

class Player:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.turn = None
        
    def renderBoard(self):
        start = 0
        end = 3
        for i in range(3):
            print('|' + '|'.join(self.board[start:end]) + '|')
            if i in [0,1]: print('--------')
            start+=3
            end+=3
            
    def movesAvailable:
        #returns bool if there are moves available on the board
        return ' ' in self.board
            
    def makeMove(self, player, location):
        if self.board[location] != ' ':
            print('not valid')  
        else: self.board[location]=player.shape 

    def checkForWinner(self):
        symbol = self.turn.shape
    
        for i in range(3):
            if self.board[i]==symbol and self.board[i+1]==symbol and
            self.board[i+2]==symbol: return True


    def playGame(self):

        player1 = input('enter player one')
        player2 = input('enter player two')
        p1 = Player(player1, 'X')
        p2 = Player(player2, 'O')
        self.turn = p1

        while self.movesAvailable:
            self.renderBoard()
            move = input('make a move 1-9')
            self.makeMove(self.turn, move)   
            self.checkForWinner()
            self.turn = p2 if self.turn is p1 else p1

game = Game()
game.renderBoard()
