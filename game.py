import random

class TeekoPlayer:
    """ An object representation for an AI game player for the game Teeko.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']
    drop_phase = True

    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    
    def heuristic_game_value(self, state):
        OPP_UNCONTESTED_WEIGHT = 20.0   
        MY_UNCONTESTED_WEIGHT  = 15.0   
        OPP_CONTESTED_WEIGHT   =  4.0   
        MY_CONTESTED_WEIGHT    =  1.0  

        ROW_WEIGHT       = 1.0     
        COL_WEIGHT       = 1.0     
        MAIN_DIAG_WEIGHT = 2.5     
        SUPP_DIAG_WEIGHT = 2.5      
        BOX_WEIGHT       = 5.0      

        my_row_score = 0
        my_col_score = 0
        opp_row_score = 0
        opp_col_score = 0

        my_main_diag_c = 0
        my_sec_diag_c = 0

        opp_main_diag_c = 0
        opp_sec_diag_c = 0

        for i in range(5):
            for start in (0, 1):
                my_temp_row = sum(ROW_WEIGHT if state[i][j] == self.my_piece else 0 for j in range(start, start+4))
                opp_temp_row = sum(ROW_WEIGHT if state[i][j] == self.opp else 0 for j in range(start, start+4))
                if my_temp_row == 0:
                    opp_temp_row *= OPP_UNCONTESTED_WEIGHT
                else:
                    opp_temp_row *= OPP_CONTESTED_WEIGHT
                if opp_temp_row == 0:
                    my_temp_row *= MY_UNCONTESTED_WEIGHT
                else:
                    my_temp_row *= MY_CONTESTED_WEIGHT
                my_row_score += my_temp_row
                opp_row_score += opp_temp_row

        for j in range(5):
            for start in (0, 1):
                my_temp_col = sum(COL_WEIGHT if state[i][j] == self.my_piece else 0 for i in range(start, start+4))
                opp_temp_col = sum(COL_WEIGHT if state[i][j] == self.opp else 0 for i in range(start, start+4))
                if my_temp_col == 0:
                    opp_temp_col *= OPP_UNCONTESTED_WEIGHT
                else:
                    opp_temp_col *= OPP_CONTESTED_WEIGHT
                if opp_temp_col == 0:
                    my_temp_col *= MY_UNCONTESTED_WEIGHT
                else:
                    my_temp_col *= MY_CONTESTED_WEIGHT
                my_col_score += my_temp_col
                opp_col_score += opp_temp_col

        my_main_diag_c_1 = 0
        my_main_diag_c_2 = 0
        my_sec_diag_c_1 = 0
        my_sec_diag_c_2 = 0

        opp_main_diag_c_1 = 0
        opp_main_diag_c_2 = 0
        opp_sec_diag_c_1 = 0
        opp_sec_diag_c_2 = 0
        for i in range(4):
            my_main_diag_c_1 += MAIN_DIAG_WEIGHT if state[i][i] == self.my_piece else 0
            my_main_diag_c_2 += MAIN_DIAG_WEIGHT if state[i+1][i+1] == self.my_piece else 0
            my_sec_diag_c_1 += MAIN_DIAG_WEIGHT if state[i][4-i] == self.my_piece else 0
            my_sec_diag_c_2 += MAIN_DIAG_WEIGHT if state[i+1][3-i] == self.my_piece else 0

            opp_main_diag_c_1 += MAIN_DIAG_WEIGHT if state[i][i] == self.opp else 0
            opp_main_diag_c_2 += MAIN_DIAG_WEIGHT if state[i+1][i+1] == self.opp else 0
            opp_sec_diag_c_1 += MAIN_DIAG_WEIGHT if state[i][4-i] == self.opp else 0
            opp_sec_diag_c_2 += MAIN_DIAG_WEIGHT if state[i+1][3-i] == self.opp else 0

        if my_main_diag_c_1 == 0:
            opp_main_diag_c_1 *= OPP_UNCONTESTED_WEIGHT
        else:
            opp_main_diag_c_1 *= OPP_CONTESTED_WEIGHT

        if opp_main_diag_c_1 == 0:
            my_main_diag_c_1 *= MY_UNCONTESTED_WEIGHT
        else:
            my_main_diag_c_1 *= MY_CONTESTED_WEIGHT

        if my_sec_diag_c_1 == 0:
            opp_sec_diag_c_1 *= OPP_UNCONTESTED_WEIGHT
        else:
            opp_sec_diag_c_1 *= OPP_CONTESTED_WEIGHT

        if opp_sec_diag_c_1 == 0:
            my_sec_diag_c_1 *= MY_UNCONTESTED_WEIGHT
        else:
            my_sec_diag_c_1 *= MY_CONTESTED_WEIGHT

        if my_main_diag_c_2 == 0:
            opp_main_diag_c_2 *= OPP_UNCONTESTED_WEIGHT
        else:
            opp_main_diag_c_2 *= OPP_CONTESTED_WEIGHT

        if opp_main_diag_c_2 == 0:
            my_main_diag_c_2 *= MY_UNCONTESTED_WEIGHT
        else:
            my_main_diag_c_2 *= MY_CONTESTED_WEIGHT

        if my_sec_diag_c_2 == 0:
            opp_sec_diag_c_2 *= OPP_UNCONTESTED_WEIGHT
        else:
            opp_sec_diag_c_2 *= OPP_CONTESTED_WEIGHT

        if opp_sec_diag_c_2 == 0:
            my_sec_diag_c_2 *= MY_UNCONTESTED_WEIGHT
        else:
            my_sec_diag_c_2 *= MY_CONTESTED_WEIGHT

        my_sec_diag_c = my_sec_diag_c_1 + my_sec_diag_c_2
        my_main_diag_c = my_main_diag_c_1 + my_main_diag_c_2

        opp_sec_diag_c = opp_sec_diag_c_1 + opp_sec_diag_c_2
        opp_main_diag_c = opp_main_diag_c_1 + opp_main_diag_c_2

        my_supp_1_c = 0
        my_supp_2_c = 0
        my_supp_3_c = 0
        my_supp_4_c = 0

        opp_supp_1_c = 0
        opp_supp_2_c = 0
        opp_supp_3_c = 0
        opp_supp_4_c = 0

        for i in range(4):
            my_supp_1_c += SUPP_DIAG_WEIGHT if state[i][i+1] == self.my_piece else 0
            my_supp_2_c += SUPP_DIAG_WEIGHT if state[i+1][i] == self.my_piece else 0

            my_supp_3_c += SUPP_DIAG_WEIGHT if state[i][3-i] == self.my_piece else 0
            my_supp_4_c += SUPP_DIAG_WEIGHT if state[i+1][4-i] == self.my_piece else 0

            opp_supp_1_c += SUPP_DIAG_WEIGHT if state[i][i+1] == self.opp else 0
            opp_supp_2_c += SUPP_DIAG_WEIGHT if state[i+1][i] == self.opp else 0

            opp_supp_3_c += SUPP_DIAG_WEIGHT if state[i][3-i] == self.opp else 0
            opp_supp_4_c += SUPP_DIAG_WEIGHT if state[i+1][4-i] == self.opp else 0

        opp_supp_1_c *= OPP_UNCONTESTED_WEIGHT if my_supp_1_c == 0 else OPP_CONTESTED_WEIGHT
        opp_supp_2_c *= OPP_UNCONTESTED_WEIGHT if my_supp_2_c == 0 else OPP_CONTESTED_WEIGHT
        opp_supp_3_c *= OPP_UNCONTESTED_WEIGHT if my_supp_3_c == 0 else OPP_CONTESTED_WEIGHT
        opp_supp_4_c *= OPP_UNCONTESTED_WEIGHT if my_supp_4_c == 0 else OPP_CONTESTED_WEIGHT

        my_supp_1_c *= MY_UNCONTESTED_WEIGHT if opp_supp_1_c == 0 else MY_CONTESTED_WEIGHT
        my_supp_2_c *= MY_UNCONTESTED_WEIGHT if opp_supp_2_c == 0 else MY_CONTESTED_WEIGHT
        my_supp_3_c *= MY_UNCONTESTED_WEIGHT if opp_supp_3_c == 0 else MY_CONTESTED_WEIGHT
        my_supp_4_c *= MY_UNCONTESTED_WEIGHT if opp_supp_4_c == 0 else MY_CONTESTED_WEIGHT

        my_tot_supp_score = my_supp_1_c + my_supp_2_c + my_supp_3_c + my_supp_4_c
        opp_tot_supp_score = opp_supp_1_c + opp_supp_2_c + opp_supp_3_c + opp_supp_4_c

        my_box_c = 0
        opp_box_c = 0
        for i in range(4):
            for j in range(4):
                my_temp_c = 0
                opp_temp_c = 0
                my_temp_c += BOX_WEIGHT if state[i][j] == self.my_piece else 0
                my_temp_c += BOX_WEIGHT if state[i+1][j] == self.my_piece else 0
                my_temp_c += BOX_WEIGHT if state[i][j+1] == self.my_piece else 0
                my_temp_c += BOX_WEIGHT if state[i+1][j+1] == self.my_piece else 0
                opp_temp_c += BOX_WEIGHT if state[i][j] == self.opp else 0
                opp_temp_c += BOX_WEIGHT if state[i+1][j] == self.opp else 0
                opp_temp_c += BOX_WEIGHT if state[i][j+1] == self.opp else 0
                opp_temp_c += BOX_WEIGHT if state[i+1][j+1] == self.opp else 0
                opp_box_c += opp_temp_c * (OPP_UNCONTESTED_WEIGHT if my_temp_c == 0 else OPP_CONTESTED_WEIGHT)
                my_box_c += my_temp_c * (MY_UNCONTESTED_WEIGHT if opp_temp_c == 0 else MY_CONTESTED_WEIGHT)

        my_tot_score = my_row_score + my_col_score + my_main_diag_c + my_sec_diag_c + my_tot_supp_score + my_box_c
        opp_tot_score = opp_row_score + opp_col_score + opp_main_diag_c + opp_sec_diag_c + opp_tot_supp_score + opp_box_c

        score = my_tot_score - opp_tot_score
        return score / (1 + abs(my_tot_score + opp_tot_score))
        

    def make_move(self, state):

        drop_phase = self.det_drop_state(state)  

        if drop_phase:
            move = None
            value = float('-inf')

            for succ, (x, y) in self.succ(state):
                temp_val = self.min_value(succ, float('-inf'), float('inf'), 2)

                if temp_val > value:
                    value = temp_val
                    move = [(x, y)]
            return move
        
        else:
            move = None
            value = float('-inf')

            for succ, (x, y, new_x, new_y) in self.succ(state):
                temp_val = self.min_value(succ, float('-inf'), float('inf'), 2)

                if temp_val > value:
                    value = temp_val
                    move = [(new_x, new_y), (x, y)]
            return move
            

    def succ(self, state):
        # returns list of all successors on a deep copy of state
        successors = list()

        drop_phase = self.det_drop_state(state)

        if(drop_phase):
            for i in range(5):
                for j in range(5):
                    if(state[i][j] == ' '):
                        deep_copy = [row[:] for row in state]
                        deep_copy[i][j] = self.my_piece
                        successors.append((deep_copy, (i, j)))
        else:
            for i in range(5):
                for j in range(5):
                    if(state[i][j] == self.my_piece):
                        deep_copy = [row[:] for row in state]
                        deep_copy[i][j] = ' '

                        if(self.check_valid_indices(i-1, j, deep_copy)):
                            successors.append((self.deep_copy_place(i-1, j, deep_copy), (i, j, i-1, j)))

                        if(self.check_valid_indices(i-1, j-1, deep_copy)):
                            successors.append((self.deep_copy_place(i-1, j-1, deep_copy), (i, j, i-1, j-1)))

                        if(self.check_valid_indices(i, j-1, deep_copy)):
                            successors.append((self.deep_copy_place(i, j-1, deep_copy), (i, j, i, j-1)))

                        if(self.check_valid_indices(i+1, j, deep_copy)):
                            successors.append((self.deep_copy_place(i+1, j, deep_copy), (i, j, i+1, j)))

                        if(self.check_valid_indices(i+1, j+1, deep_copy)):
                            successors.append((self.deep_copy_place(i+1, j+1, deep_copy), (i, j, i+1, j+1)))

                        if(self.check_valid_indices(i, j+1, deep_copy)):
                            successors.append((self.deep_copy_place(i, j+1, deep_copy), (i, j, i, j+1)))

                        if(self.check_valid_indices(i+1, j-1, deep_copy)):
                            successors.append((self.deep_copy_place(i+1, j-1, deep_copy), (i, j, i+1, j-1)))

                        if(self.check_valid_indices(i-1, j+1, deep_copy)):
                            successors.append((self.deep_copy_place(i-1, j+1, deep_copy), (i, j, i-1, j+1)))
        return successors
    
    def min_value(self, state, alpha, beta, depth):
        game_value = self.game_value(state)
        if(game_value == 1 or game_value == -1):
            return game_value
        if(depth == 0):
            return self.heuristic_game_value(state)
        v = float('inf')
        for succ, _ in self.succ(state):
            v = min(v, self.max_value(succ, alpha, beta, depth-1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def max_value(self, state, alpha, beta, depth):
        game_value = self.game_value(state)
        if(game_value == 1 or game_value == -1):
            return game_value
        if(depth == 0):
            return self.heuristic_game_value(state)
        v = float('-inf')
        for succ, _ in self.succ(state):
            v = max(v, self.min_value(succ, alpha, beta, depth-1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
        


    def det_drop_state(self, state):
        num_pieces = 0
        for i in range(5):
            for j in range(5):
                if(state[i][j] == self.my_piece or state[i][j] == self.opp):
                    num_pieces = num_pieces+1
        
        return num_pieces < 8
                        
    def check_valid_indices(self, x, y, state):
        if not (0 <= x < 5 and 0 <= y < 5):
            return False
        return state[x][y] == ' '
    
    def deep_copy_place(self, x, y, state):
        deep_copy = [row[:] for row in state]
        deep_copy[x][y] = self.my_piece
        return deep_copy

    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase).
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase).

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row)+": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this TeekoPlayer object, or a generated successor state.

        Returns:
            int: 1 if this TeekoPlayer wins, -1 if the opponent wins, 0 if no winner

        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return 1 if row[i]==self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:
                    return 1 if state[i][col]==self.my_piece else -1

        # TODO: check \ diagonal wins
        for i in range(2):
            if(state[i][i] != ' ' and state[i][i] == state[i+1][i+1] == state[i+2][i+2] == state[i+3][i+3]):
                return 1 if state[i][i]==self.my_piece else -1
        
        if(state[0][1] != ' ' and state[0][1] == state[1][2] == state[2][3] == state[3][4]):
            return 1 if state[0][1] == self.my_piece else -1
        if(state[1][0] != ' ' and state[1][0] == state[2][1] == state[3][2] == state[4][3]):
            return 1 if state[1][0] == self.my_piece else -1
            
        for i in range(2):
            if(state[i][4-i] != ' ' and state[i][4-i] == state[i+1][3-i] == state[i+2][2-i] == state[i+3][1-i]):
                return 1 if state[i][4-i]==self.my_piece else -1
        
        if(state[0][3] != ' ' and state[0][3] == state[1][2] == state[2][1] == state[3][0]):
            return 1 if state[0][3] == self.my_piece else -1
        if(state[1][4] != ' ' and state[1][4] == state[2][3] == state[3][2] == state[4][1]):
            return 1 if state[1][4] == self.my_piece else -1
        
            
        # TODO: check box wins
        for i in range(4):
            for j in range(4):
                if(state[i][j] != ' ' and state[i][j] == state[i+1][j] == state[i][j+1] == state[i+1][j+1]):
                    return 1 if state[i][j]==self.my_piece else -1

        return 0 # no winner yet

"""
    Demo    
"""
def main():
    print('Hello, this is Samaritan')
    ai = TeekoPlayer()
    piece_count = 0
    turn = 0

    # drop phase
    while piece_count < 8 and ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved at "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece+" moved from "+chr(move[1][1]+ord("A"))+str(move[1][0]))
            print("  to "+chr(move[0][1]+ord("A"))+str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp+"'s turn")
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0])-ord("A")),
                                    (int(move_from[1]), ord(move_from[0])-ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        print("AI wins! Game over.")
    else:
        print("You win! Game over.")


if __name__ == "__main__":
    main()
