# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Ibrahim Jomaa
# MarkUs Login: jomaaibr
#

PUZZLE1 = '''
tlkutqyu
hyrreiht
inokdcne
eaccaayu
riainpaf
rrpnairb
ybybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyyrreihtpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    r'''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# There are 6 possible rectangluar puzzle formats that need to be tested
# 1. Square (25 by 25)
# Words:
# zip          --> 3 occurrences[right-to-left|left-to-right|bottom-to-top]
# cozy         --> 3 occurrences[right-to-left|left-to-right|top-to-bottom]
# ninja        --> 3 occurrences[top-to-bottom|bottom-to-top|right-to-left]
# puzzle       --> 3 occurrences[top-to-bottom|bottom-to-top|left-to-right]
# mechanics    --> 2 occurrences[top-to-bottom]
# workload     --> 2 occurrences[bottom-to-top]
# civic        --> 2 occurrences[top-to-bottom|bottom-to-top]
# manipulation --> 2 occurrences[right-to-left]
# polish       --> 2 occurrences[left-to-right]
# rotor        --> 2 occurrences[right-to-left|left-to-right]
# banning      --> 2 occurrences[right-to-left|top-to-bottom]
# architecture --> 2 occurrences[left-to-right|top-to-bottom]
# warehouse    --> 2 occurrences[right-to-left|bottom-to-top]
# predecessor  --> 2 occurrences[left-to-right|bottom-to-top]
# dentist      --> 1 occurrence[top-to-bottom]
# measuring    --> 1 occurrence[bottom-to-top]
# ecology      --> 1 occurrence[right-to-left]
# husband      --> 1 occurrence[left-to-right]

PUZZLE_SQUARE = '''
mjhpredecessorderrocziptr
epqhusbanddddmabvoqikqpyr
clamxizndurhepoqwslvmmvjx
hmygolocepprnnlqwsjicozyj
adkwitnbivcdtmkqwencekwsp
noitalupinamimrndcaalmbku
ikodbieoggrnsnoqqegezqosz
ckofpqaazscbtnwfedngzvjez
sdlgiengiahhlrigmembufkil
gninnabqqwiopttrerbepqpxe
fkgnesagbdtfkeibcpnspizzb
polishnndeepolishbfulbirc
ddkfiznibfcgleikaiyoavico
aldoedirbftbkibfnbbhjpyrz
obkicdnubfubiwmdivdenqify
lldogegskjrgkdiecnmribmid
kdfhplgabfelldoesnhanzldf
rotorasevikesuoherawyzocn
odiqncomnoitalupinamviwur
wadarchitectureboekabmehd
ndkaysdntmchvbpldjweajnin
iasdfqqkeefkvingmlcpority
ndfimbsespuzzledkfjumblap
jdfimvnalqpowejfimodmivsi
askdinxnciohasdflpqwetrez
'''

# 2. Horizontally long rectangle (30 by 5)
# Words:
# key     --> 3 occurrences[right-to-left|left-to-right|bottom-to-top]
# mop     --> 3 occurrences[right-to-left|left-to-right|top-to-bottom]
# fly     --> 3 occurrences[top-to-bottom|bottom-to-top|right-to-left]
# axe     --> 3 occurrences[top-to-bottom|bottom-to-top|left-to-right]
# pizza   --> 2 occurrences[top-to-bottom]
# coat    --> 2 occurrences[bottom-to-top]
# level   --> 2 occurrences[top-to-bottom|bottom-to-top]
# flux    --> 2 occurrences[right-to-left]
# job     --> 2 occurrences[left-to-right]
# reviver --> 2 occurrences[right-to-left|left-to-right]
# jumbo   --> 2 occurrences[right-to-left|top-to-bottom]
# junk    --> 2 occurrences[left-to-right|top-to-bottom]
# wind    --> 2 occurrences[right-to-left|bottom-to-top]
# fork    --> 2 occurrences[left-to-right|bottom-to-top]
# waste   --> 1 occurrence[top-to-bottom]
# punt    --> 1 occurrence[bottom-to-top]
# jump    --> 1 occurrence[right-to-left]
# whiz    --> 1 occurrence[left-to-right]

PUZZLE_HORIZONTALLY_LONG_RECTANGLE = '''
phljunkwhizjkdobmujpkeyyahefmy
iteujtzaxulfrnpmujtimoplxgxloe
zavmunksjobfoiforkazylffejaypk
zoebnultxulffwdniwozpomdkwices
aclokpeejobrevivercayeklofdaxe
'''

# 3. Vertically long rectangle (5 by 30)
# Words:
# yam      --> 3 occurrences[right-to-left|left-to-right|bottom-to-top]
# pig      --> 3 occurrences[right-to-left|left-to-right|top-to-bottom]
# ink      --> 3 occurrences[top-to-bottom|bottom-to-top|right-to-left]
# wig      --> 3 occurrences[top-to-bottom|bottom-to-top|left-to-right]
# passive  --> 2 occurrences[top-to-bottom]
# paranoid --> 2 occurrences[bottom-to-top]
# pullup   --> 2 occurrences[top-to-bottom|bottom-to-top]
# grab     --> 2 occurrences[right-to-left]
# tux      --> 2 occurrences[left-to-right]
# tnt      --> 2 occurrences[right-to-left|left-to-right]
# size     --> 2 occurrences[right-to-left|top-to-bottom]
# gum      --> 2 occurrences[left-to-right|top-to-bottom]
# gym      --> 2 occurrences[right-to-left|bottom-to-top]
# by       --> 2 occurrences[left-to-right|bottom-to-top]
# media    --> 1 occurrence[top-to-bottom]
# artist   --> 1 occurrence[bottom-to-top]
# cup      --> 1 occurrence[right-to-left]
# six      --> 1 occurrence[left-to-right]

PUZZLE_VERTICALLY_LONG_RECTANGLE = '''
msptp
eiusa
dzlis
ielts
aquri
pipav
dtuxe
ibarg
oezis
npucy
asixb
rbarg
acvmd
ppeyi
amygo
sgumn
subya
imwqr
vtnta
etuxp
yamkm
gipna
wppiy
iqkni
gkifg
loasi
wigmw
dsaip
pigni
maykg
'''

# 4. Single horizontal line (20 by 1)
# Words:
# electrocardiographic --> 1 occurrence[left-to-right]
PUZZLE_SINGLE_HORIZONTAL_LINE = '''
electrocardiographic
'''

# 5. Single vertical line (1 by 20)
# Words:
# counterdemonstration --> 1 occurrence[top-to-bottom]
PUZZLE_SINGLE_VERTICAL_LINE = '''
c
o
u
n
t
e
r
d
e
m
o
n
s
t
r
a
t
i
o
n
'''

# 6. One character (1 by 1)
# Word:
# q --> 4 occurrences[top-to-bottom|bottom-to-top|left-to-right|right-to-left]
PUZZLE_ONE_CHARACTER = '''
q
'''

# For all instances when we need an example where a word is not in a puzzle,
# we'll use this variable
WORD_NOT_IN_PUZZLE = "brian"


def rotate_puzzle_right_to_left_position(puzzle):
    r'''(str) -> str
    Given a rectangular word puzzle: returns said puzzle rotated 180 degrees
    to the left. Therefore, the displayed words are read from right-to-left.
    REQ: None
    >>> rotate_puzzle_right_to_left_position(
    ... "segatest\nnintendo\natariyet\nsonyleft")
    'tfelynos\nteyirata\nodnetnin\ntsetages'
    '''
    # Call the "rotate_puzzle" function to change puzzle orientation to
    # top-to-bottom
    puzzle_top_to_bottom_position = rotate_puzzle(puzzle)
    # Call the "rotate_puzzle" function again to change puzzle orientation to
    # right-to-left
    puzzle_right_to_left_position = rotate_puzzle(
                                    puzzle_top_to_bottom_position)
    # Return the newly rotated puzzle in the right-to-left position
    return puzzle_right_to_left_position


def rotate_puzzle_bottom_to_top_position(puzzle):
    r'''(str) -> str
    Given a rectangular word puzzle: returns said puzzle rotated 270 degrees
    to the left. Therefore, the displayed words are read from bottom-to-top.
    REQ: None
    >>> rotate_puzzle_bottom_to_top_position(
    ... "segatest\nnintendo\natariyet\nsonyleft")
    'sans\notie\nnang\nyrta\nliet\neyne\nfeds\nttot'
    '''
    # Call the "rotate_puzzle_right_to_left_position" function to change puzzle
    # orientation to right-to-left
    puzzle_right_to_left_position = (
        rotate_puzzle_right_to_left_position(puzzle))
    # Call the "rotate_puzzle" function again to change puzzle orientation to
    # bottom-to-top
    puzzle_bottom_to_top_position = (
        rotate_puzzle(puzzle_right_to_left_position))
    # Return the newly rotated puzzle in the bottom-to-top-position
    return puzzle_bottom_to_top_position

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    r'''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''
    # your code here
    # Have all possible puzzle rotations connected to one line of string
    # 1. Add the normal puzzle
    puzzle_all_positions = puzzle + " "
    # 2. Add the puzzle rotated 90 degrees to the left
    puzzle_all_positions += rotate_puzzle(puzzle) + " "
    # 3. Add the puzzle rotated 180 degrees to the left
    puzzle_all_positions += rotate_puzzle_right_to_left_position(puzzle) + " "
    # 4. Add the puzzle rotated 270 degrees to the left
    puzzle_all_positions += rotate_puzzle_bottom_to_top_position(puzzle)
    # Check for the word occurrence for all rotations
    total_word_count = lr_occurrences(puzzle_all_positions, word)
    # Returns the amount of occurrences of the desired word
    return total_word_count


# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    r'''(str, str) -> bool
    Given a rectangular word puzzle, and a desired word: returns True if the
    word is found in the puzzle on the horizontal axis, either in the
    left-to-right position, right-to-left position, or both.
    REQ: None
    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "zip")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "cozy")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "ninja")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "puzzle")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "mechanics")
    False

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "workload")
    False

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "civic")
    False

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "manipulation")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "polish")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "rotor")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "banning")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "architecture")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "warehouse")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "predecessor")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "dentist")
    False

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "measuring")
    False

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "ecology")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, "husband")
    True

    >>> in_puzzle_horizontal(PUZZLE_SQUARE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "key")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "mop")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fly")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "axe")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "pizza")
    False

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "coat")
    False

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "level")
    False

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "flux")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "job")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "reviver")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jumbo")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "junk")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "wind")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fork")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "waste")
    False

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "punt")
    False

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jump")
    True

    >>> in_puzzle_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "whiz")
    True

    >>> in_puzzle_horizontal(
    ... PUZZLE_HORIZONTALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "yam")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pig")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "ink")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "wig")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "passive")
    False

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "paranoid")
    False

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pullup")
    False

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "grab")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tux")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tnt")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "size")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gum")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gym")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "by")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "media")
    False

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "artist")
    False

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "cup")
    True

    >>> in_puzzle_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "six")
    True

    >>> in_puzzle_horizontal(
    ... PUZZLE_VERTICALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_horizontal(
    ... PUZZLE_SINGLE_HORIZONTAL_LINE, "electrocardiographic")
    True

    >>> in_puzzle_horizontal(PUZZLE_SINGLE_HORIZONTAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_horizontal(
    ... PUZZLE_SINGLE_VERTICAL_LINE, "counterdemonstration")
    False

    >>> in_puzzle_horizontal(PUZZLE_SINGLE_VERTICAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_horizontal(PUZZLE_ONE_CHARACTER, "q")
    True

    >>> in_puzzle_horizontal(PUZZLE_ONE_CHARACTER, WORD_NOT_IN_PUZZLE)
    False
    '''
    # Have all possible horizontal puzzle positions connected to one line of
    # string
    # 1. Add the normal puzzle
    puzzle_horizontal_positions = puzzle + " "
    # 2. Add the puzzle rotated 180 degrees to the left
    puzzle_horizontal_positions += rotate_puzzle_right_to_left_position(puzzle)
    # Check if the word appears at least once in the horizontal axis
    horizontal_word_count = (
        lr_occurrences(puzzle_horizontal_positions, word) > 0)
    # Return the status on the word's appearence
    return horizontal_word_count


# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    r'''(str, str) -> bool
    Given a rectangular word puzzle, and a desired word: returns True if the
    word is found in the puzzle on the vertical axis, either in the
    top-to-bottom position, bottom-to-top position, or both.
    REQ: None
    >>> in_puzzle_vertical(PUZZLE_SQUARE, "zip")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "cozy")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "ninja")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "puzzle")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "mechanics")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "workload")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "civic")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "manipulation")
    False

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "polish")
    False

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "rotor")
    False

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "banning")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "architecture")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "warehouse")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "predecessor")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "dentist")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "measuring")
    True

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "ecology")
    False

    >>> in_puzzle_vertical(PUZZLE_SQUARE, "husband")
    False

    >>> in_puzzle_vertical(PUZZLE_SQUARE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "key")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "mop")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fly")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "axe")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "pizza")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "coat")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "level")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "flux")
    False

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "job")
    False

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "reviver")
    False

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jumbo")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "junk")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "wind")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fork")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "waste")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "punt")
    True

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jump")
    False

    >>> in_puzzle_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "whiz")
    False

    >>> in_puzzle_vertical(
    ... PUZZLE_HORIZONTALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "yam")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pig")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "ink")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "wig")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "passive")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "paranoid")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pullup")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "grab")
    False

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tux")
    False

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tnt")
    False

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "size")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gum")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gym")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "by")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "media")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "artist")
    True

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "cup")
    False

    >>> in_puzzle_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "six")
    False

    >>> in_puzzle_vertical(
    ... PUZZLE_VERTICALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_vertical(
    ... PUZZLE_SINGLE_HORIZONTAL_LINE, "electrocardiographic")
    False

    >>> in_puzzle_vertical(PUZZLE_SINGLE_HORIZONTAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_vertical(PUZZLE_SINGLE_VERTICAL_LINE, "counterdemonstration")
    True

    >>> in_puzzle_vertical(PUZZLE_SINGLE_VERTICAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle_vertical(PUZZLE_ONE_CHARACTER, "q")
    True

    >>> in_puzzle_vertical(PUZZLE_ONE_CHARACTER, WORD_NOT_IN_PUZZLE)
    False
    '''
    # Have all possible vertical puzzle positions connected to one line of
    # string
    # 1. Add the puzzle rotated 90 degrees to the left
    puzzle_vertical_positions = rotate_puzzle(puzzle) + " "
    # 2. Add the puzzle rotated 270 degrees to the left
    puzzle_vertical_positions += (
        rotate_puzzle_bottom_to_top_position(puzzle))
    # Check if the word appears at least once in the vertical axis
    vertical_word_count = lr_occurrences(puzzle_vertical_positions, word) > 0
    # Return the status on the word's appearance
    return vertical_word_count


# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    r'''(str, str) -> bool
    Given a rectangular word puzzle, and a desired word: returns True if the
    word is found in the puzzle, either in the left-to-right position,
    right-to-left position, top-to-bottom position, bottom-to-top position,
    or a combination of the four.
    REQ: None
    >>> in_puzzle(PUZZLE_SQUARE, "zip")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "cozy")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "ninja")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "puzzle")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "mechanics")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "workload")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "civic")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "manipulation")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "polish")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "rotor")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "banning")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "architecture")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "warehouse")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "predecessor")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "dentist")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "measuring")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "ecology")
    True

    >>> in_puzzle(PUZZLE_SQUARE, "husband")
    True

    >>> in_puzzle(PUZZLE_SQUARE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "key")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "mop")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fly")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "axe")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "pizza")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "coat")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "level")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "flux")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "job")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "reviver")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jumbo")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "junk")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "wind")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fork")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "waste")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "punt")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jump")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "whiz")
    True

    >>> in_puzzle(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "yam")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pig")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "ink")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "wig")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "passive")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "paranoid")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pullup")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "grab")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tux")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tnt")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "size")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gum")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gym")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "by")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "media")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "artist")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "cup")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, "six")
    True

    >>> in_puzzle(PUZZLE_VERTICALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle(PUZZLE_SINGLE_HORIZONTAL_LINE, "electrocardiographic")
    True

    >>> in_puzzle(PUZZLE_SINGLE_HORIZONTAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle(PUZZLE_SINGLE_VERTICAL_LINE, "counterdemonstration")
    True

    >>> in_puzzle(PUZZLE_SINGLE_VERTICAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_puzzle(PUZZLE_ONE_CHARACTER, "q")
    True

    >>> in_puzzle(PUZZLE_ONE_CHARACTER, WORD_NOT_IN_PUZZLE)
    False
    '''
    # Check if the word appears in any of the axes
    is_in_puzzle = (in_puzzle_horizontal(puzzle, word) or
                    in_puzzle_vertical(puzzle, word))
    # Return the status on the word's appearence
    return is_in_puzzle

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    r'''(str, str) -> bool
    Given a rectangular word puzzle, and a desired word: returns True if the
    word is found in the puzzle either in the horizontal or vertical axis,
    but not both at the same time.
    REQ: None
    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "zip")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "cozy")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "ninja")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "puzzle")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "mechanics")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "workload")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "civic")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "manipulation")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "polish")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "rotor")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "banning")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "architecture")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "warehouse")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "predecessor")
    False

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "dentist")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "measuring")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "ecology")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, "husband")
    True

    >>> in_exactly_one_dimension(PUZZLE_SQUARE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "key")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "mop")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fly")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "axe")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "pizza")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "coat")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "level")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "flux")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "job")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "reviver")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jumbo")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "junk")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "wind")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fork")
    False

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "waste")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "punt")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jump")
    True

    >>> in_exactly_one_dimension(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "whiz")
    True

    >>> in_exactly_one_dimension(
    ... PUZZLE_HORIZONTALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "yam")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pig")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "ink")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "wig")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "passive")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "paranoid")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pullup")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "grab")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tux")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tnt")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "size")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gum")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gym")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "by")
    False

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "media")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "artist")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "cup")
    True

    >>> in_exactly_one_dimension(PUZZLE_VERTICALLY_LONG_RECTANGLE, "six")
    True

    >>> in_exactly_one_dimension(
    ... PUZZLE_VERTICALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_exactly_one_dimension(
    ... PUZZLE_SINGLE_HORIZONTAL_LINE, "electrocardiographic")
    True

    >>> in_exactly_one_dimension(
    ... PUZZLE_SINGLE_HORIZONTAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_exactly_one_dimension(
    ... PUZZLE_SINGLE_VERTICAL_LINE, "counterdemonstration")
    True

    >>> in_exactly_one_dimension(
    ... PUZZLE_SINGLE_VERTICAL_LINE, WORD_NOT_IN_PUZZLE)
    False

    >>> in_exactly_one_dimension(PUZZLE_ONE_CHARACTER, "q")
    False

    >>> in_exactly_one_dimension(PUZZLE_ONE_CHARACTER, WORD_NOT_IN_PUZZLE)
    False
    '''
    # Check if the word is in the horizontal axis
    is_in_puzzle_horizontal = in_puzzle_horizontal(puzzle, word)
    # Check if the word is in the vertical axis
    is_in_puzzle_vertical = in_puzzle_vertical(puzzle, word)
    # Check if the word appears in only 1 axes, not both
    is_in_puzzle_one_axis = (not(is_in_puzzle_horizontal and
                                 is_in_puzzle_vertical))
    # Check if the word appears in the puzzle at all
    is_in_puzzle_one_axis = is_in_puzzle_one_axis and in_puzzle(puzzle, word)
    # Return the status on the words appearance
    return is_in_puzzle_one_axis


# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    r'''(str, str) -> bool
    Given a rectangular word puzzle, and a desired word: returns True if the
    word is found in the puzzle only in the horizontal axis, and or if the word
    is not found in the puzzle at all.
    REQ: None
    >>> all_horizontal(PUZZLE_SQUARE, "zip")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "cozy")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "ninja")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "puzzle")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "mechanics")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "workload")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "civic")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "manipulation")
    True

    >>> all_horizontal(PUZZLE_SQUARE, "polish")
    True

    >>> all_horizontal(PUZZLE_SQUARE, "rotor")
    True

    >>> all_horizontal(PUZZLE_SQUARE, "banning")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "architecture")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "warehouse")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "predecessor")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "dentist")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "measuring")
    False

    >>> all_horizontal(PUZZLE_SQUARE, "ecology")
    True

    >>> all_horizontal(PUZZLE_SQUARE, "husband")
    True

    >>> all_horizontal(PUZZLE_SQUARE, WORD_NOT_IN_PUZZLE)
    True

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "key")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "mop")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fly")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "axe")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "pizza")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "coat")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "level")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "flux")
    True

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "job")
    True

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "reviver")
    True

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jumbo")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "junk")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "wind")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fork")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "waste")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "punt")
    False

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jump")
    True

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "whiz")
    True

    >>> all_horizontal(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    True

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "yam")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pig")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "ink")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "wig")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "passive")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "paranoid")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pullup")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "grab")
    True

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tux")
    True

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tnt")
    True

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "size")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gum")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gym")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "by")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "media")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "artist")
    False

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "cup")
    True

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, "six")
    True

    >>> all_horizontal(PUZZLE_VERTICALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    True

    >>> all_horizontal(PUZZLE_SINGLE_HORIZONTAL_LINE, "electrocardiographic")
    True

    >>> all_horizontal(PUZZLE_SINGLE_HORIZONTAL_LINE, WORD_NOT_IN_PUZZLE)
    True

    >>> all_horizontal(PUZZLE_SINGLE_VERTICAL_LINE, "counterdemonstration")
    False

    >>> all_horizontal(PUZZLE_SINGLE_VERTICAL_LINE, WORD_NOT_IN_PUZZLE)
    True

    >>> all_horizontal(PUZZLE_ONE_CHARACTER, "q")
    False

    >>> all_horizontal(PUZZLE_ONE_CHARACTER, WORD_NOT_IN_PUZZLE)
    True
    '''
    # Check if the word is in either one of the axes, but not both
    is_in_puzzle_one_axis = in_exactly_one_dimension(puzzle, word)
    # Check if the word is in the horizontal axis
    is_in_puzzle_horizontal = in_puzzle_horizontal(puzzle, word)
    # Check if the word does not appear in the puzzle at all
    is_in_puzzle = not(in_puzzle(puzzle, word))
    # Combine all boolean statements
    is_in_puzzle_horizontal_axis = ((is_in_puzzle_one_axis and
                                    is_in_puzzle_horizontal) or
                                    is_in_puzzle)
    # Return the status on the words appearance
    return is_in_puzzle_horizontal_axis

# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    r'''(str, str) -> bool
    Given a rectangular word puzzle, and a desired word: returns True if the
    word is found once in the puzzle in the vertical axis, and or if the word
    is not found in the puzzle at all.
    REQ: None
    >>> at_most_one_vertical(PUZZLE_SQUARE, "zip")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "cozy")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "ninja")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "puzzle")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "mechanics")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "workload")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "civic")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "manipulation")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "polish")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "rotor")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "banning")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "architecture")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "warehouse")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "predecessor")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "dentist")
    True

    >>> at_most_one_vertical(PUZZLE_SQUARE, "measuring")
    True

    >>> at_most_one_vertical(PUZZLE_SQUARE, "ecology")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, "husband")
    False

    >>> at_most_one_vertical(PUZZLE_SQUARE, WORD_NOT_IN_PUZZLE)
    True

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "key")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "mop")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fly")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "axe")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "pizza")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "coat")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "level")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "flux")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "job")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "reviver")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jumbo")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "junk")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "wind")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "fork")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "waste")
    True

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "punt")
    True

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "jump")
    False

    >>> at_most_one_vertical(PUZZLE_HORIZONTALLY_LONG_RECTANGLE, "whiz")
    False

    >>> at_most_one_vertical(
    ... PUZZLE_HORIZONTALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    True

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "yam")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pig")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "ink")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "wig")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "passive")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "paranoid")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "pullup")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "grab")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tux")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "tnt")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "size")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gum")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "gym")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "by")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "media")
    True

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "artist")
    True

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "cup")
    False

    >>> at_most_one_vertical(PUZZLE_VERTICALLY_LONG_RECTANGLE, "six")
    False

    >>> at_most_one_vertical(
    ... PUZZLE_VERTICALLY_LONG_RECTANGLE, WORD_NOT_IN_PUZZLE)
    True

    >>> at_most_one_vertical(
    ... PUZZLE_SINGLE_HORIZONTAL_LINE, "electrocardiographic")
    False

    >>> at_most_one_vertical(PUZZLE_SINGLE_HORIZONTAL_LINE, WORD_NOT_IN_PUZZLE)
    True

    >>> at_most_one_vertical(
    ... PUZZLE_SINGLE_VERTICAL_LINE, "counterdemonstration")
    True

    >>> at_most_one_vertical(PUZZLE_SINGLE_VERTICAL_LINE, WORD_NOT_IN_PUZZLE)
    True

    >>> at_most_one_vertical(PUZZLE_ONE_CHARACTER, "q")
    False

    >>> at_most_one_vertical(PUZZLE_ONE_CHARACTER, WORD_NOT_IN_PUZZLE)
    True
    '''
    # Check if the word is in either one of the axes, but not both
    is_in_puzzle_one_axis = in_exactly_one_dimension(puzzle, word)
    # Check if the word is in the vertical axis
    is_in_puzzle_vertical = in_puzzle_vertical(puzzle, word)
    # Check the amount of occurrencs of the desired word in the vertical axis
    # is exactly one
    is_in_puzzle_once = (
        (lr_occurrences(rotate_puzzle(puzzle), word) +
         lr_occurrences(rotate_puzzle_bottom_to_top_position(puzzle), word)) ==
        1)
    # Check if the word does not appear in the puzzle at all
    is_in_puzzle = not(in_puzzle(puzzle, word))
    # Combine all boolean statements
    is_in_puzzle_vertical_once = ((is_in_puzzle_one_axis and
                                  is_in_puzzle_vertical and
                                   is_in_puzzle_once) or
                                  is_in_puzzle)
    # Return the status on the word's appearance
    return is_in_puzzle_vertical_once


def do_tasks(puzzle, name):
    r'''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    print(lr_occurrences(puzzle, name))  # your print call here

    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(lr_occurrences(rotate_puzzle(puzzle), name))

    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(lr_occurrences(rotate_puzzle_right_to_left_position(puzzle), name))

    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(rotate_puzzle_bottom_to_top_position(puzzle), name))

    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print(total_occurrences(puzzle, name))

    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print(in_puzzle_horizontal(puzzle, name))

do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, "nick")

# *task* 7: call do_tasks on PUZZLE2  and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, "nick")

# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, "nick"))

# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'thierry'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, "thierry"))
