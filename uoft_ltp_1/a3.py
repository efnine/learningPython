# Do not call the print function

"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    return word in wordlist

#print(is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO'))

#------------------------------------------------------------------

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    char_cumulator = ""
    for i in board[row_index]:
        char_cumulator = str(char_cumulator + str(i))
    return char_cumulator
        
#print(make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0))

#------------------------------------------------------------------

def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    char_cumulator = ""
    for i in range(len(board)):
        char_cumulator = char_cumulator + board[i][column_index]
    return char_cumulator
    
#print(make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1))

#------------------------------------------------------------------

def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False

#print(board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB'))

#------------------------------------------------------------------

def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    
    for column_index in range(len(board[0])):
        if word in make_str_from_column(board, column_index):
            return True

    return False

#print(board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TB'))

#------------------------------------------------------------------


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    
    return board_contains_word_in_column(board,word) or board_contains_word_in_row(board, word)

#print(board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'XD'))

#------------------------------------------------------------------

def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    len_word = len(word)
    if len_word < 3:
        return 0
    elif len_word < 7:
        return 1 * len_word
    elif len_word < 10:
        return 2 * len_word
    elif len_word >= 10:
        return 3 * len_word
    
#print(word_score('to'))

#------------------------------------------------------------------

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    curr_pts = player_info[1] + word_score(word)
    return curr_pts
    
#print(update_score(['Jonathan', 4], 'ANT'))
    
#------------------------------------------------------------------

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    words_on_board = 0
    for i in range(len(words)):
        if board_contains_word(board, words[i]) == True:
            words_on_board = words_on_board + 1
    return words_on_board
    
#print(num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO']))
    
#------------------------------------------------------------------
def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    file_path = "/Users/danie/OneDrive/NON-PERSONAL/Programming/dnPythonFiles/learningPython/uoft_ltp_1/"
    file_name = words_file
    file_location = file_path + file_name
    opened_file = open(file_location,"r")
    lines = opened_file.readlines() #reads the entire file into memory a
    
    word_list = []
    for i in range(len(lines)):
        word_list.append(lines[i].strip())
    #word_list = lines[0]
    return word_list

#print(read_words("wordlist1.txt"))

#------------------------------------------------------------------

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    file_path = "/Users/danie/OneDrive/NON-PERSONAL/Programming/dnPythonFiles/learningPython/uoft_ltp_1/"
    file_name = board_file
    file_location = file_path + file_name
    opened_file = open(file_location,"r")
    words = opened_file.readlines() # reads the entire file into memory a
    
    # First we have to clean the list of the "\n"
    new_words_list = []
    for i in range(len(words)):
        cleaned_words = words[i].strip("\n")
        new_words_list.append(cleaned_words)
        #return new_words_list
    
    # Second we have to turn each char within each list element into a str
    # Each list element must have its own line
    char_list = []
    for i in range(len(new_words_list)): # for every element in new_words_list
        subject_word = new_words_list[i] # store the value of each word
                
        my_list = []
        for i in range(len(subject_word)): # for every element in each word
            #my_list.append(str(subject_word[i])) # give me a list with each char
            my_list.append(str(subject_word[i])) # give me a list with each char
            char_list.insert(i,my_list) # insert each list into a list
        return char_list

        #print(read_board("board1.txt"))










