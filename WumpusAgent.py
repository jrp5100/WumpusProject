# WumpusAgent.py
# Agent for Wumpus World Project
# Mason Humphrey,
# 2/7/2021

# This agent aims to guide an explorer through a cave littered with pits and wumpi in search for endless riches
# Takes in percepts from driver, returns appropriate action
from WumpusRoom import Room
import HuntTheWumpus
htw = HuntTheWumpus

# For movement function recieve percepts (each defined)
# Stench - the Wumpus is in a directly adjacent square (not diagonal).
# Breeze - there is a pit in a directly adjacent square (not diagonal).
# Glitter - the gold is in the current square
# Bump - you walked in to a wall of the dungeon
# Scream - the Wumpus was killed!
# S - stench
# G - glitter
# U - bump
# C - scream

# For movement function return a string indicating
# N - move north
# S - move south
# E - move east
# W - move west
# SN - shoot north
# SS - shoot south
# SE - shoot east
# SW - shoot west
# G - grab gold
# C - climb out
#
gameType = 0
numArrows = 0
numWumpi = 0
up = False #going down or south by default
left = False #moving right or west by default
moves = [] #list of all made moves by the agent

north = False #global variable for telling if we are moving north, or south 0 - Moving South, 1 - Moving North
east = True #Global variables for telling if we are moving east, or west: 0 - moving west, 1 - moving east
breaker = 0 #used to break infinite loops
shootcount = 0
possiblecorner = False #used to check if we have reached a coerner of the cave. If bumpcheck is true, then possibleCorner is set true. if on the next turn bumpcheck is true again, then we have hit a corner
currentRoom = (0,0)# key of the current room


# sets the type of wumpi (moving/stationary), # of arrows, and # of wumpi: used for re-setting the game in the driver code
def setParams(type, arrows, wumpi):
    try:  # Should check to make sure that the inputs for the parameters are valid (integers), turns out Alan took care of the int()
        gameType = int(type)
    except ValueError:
        gameType = 1
        print("Game type invalid, defaulting to 1.")

    if gameType > 2 or gameType < 1:
        gameType = 1
        print("Game type invalid, defaulting to 1.")

    try:
        numArrows = int(arrows)
    except ValueError:
        numArrows = 1
        print("Number of arrows invalid, defaulting to 1.")

    try:
        numWumpi = int(
            wumpi)  # ????????????Do we need to check for anything else? ex. that this isnt too large? idk since we don't know size of cave
    except ValueError:
        numWumpi = 1
        print("Number of wumpi invalid, defaulting to 1.")

    return 0

#Q: Should we make these global variables? then we could just check them whenever without making a funciton call. -Mason
def eastOrWest(east):#tells move functions whether to move east or west based off of the status of the left variable
    if(east):
        return 'E'
    else:
        return 'W'

def northOrSouth(north):#checks if agent is moving north or south
    if(north):
        return 'N'
    else:
        return 'S'

def vertical(s): #chekcs if last move was vertical. if it was not then its horizontal
    if s == 'N' or s == 'S':
        return True
    elif s == 'E' or s == 'W':
        return False

#create a dict to use as a map
#Each room object will have a tuple coordinate as a key. Room objects will contain the data that we know about the room and can be updated to reflect newfound info
startroom = Room(0, 0, False, 0, 0, 0)#first room added to our map-will be updated
map = {(0,0): startroom}


def getCurrentRoom(prevroomx, prevroomy, move):#takes in coordinates of prevroom to return key coordinates of newroom
    if move == 'N':
        return (prevroomx, prevroomy +1)
    if move == 'S':
        return (prevroomx, prevroomy -1)
    if move == 'E':
        return (prevroomx -1, prevroomy)
    if move == 'W':
        return (prevroomx +1, prevroomy)
    else:
        return(prevroomx, prevroomy)


def getMove(sensor):
    percepts = list(sensor)  # Creates a list out of input percepts
    print(percepts)
    move = ''  # move performed by the agent this turn
    global north
    global east
    global moves
    global map

    getCurrentRoom()

    for p in percepts:

        if p == 'G':
            escape()
            return 'G'

    for p in percepts:
        if p == 'S':  # if there is a wumpus in an adjacent square
            shootcount = shootcount + 1  # add to shootcount for each shot
            # return wumpus(numArrows, shootcount)
            return 'SN'  # not sure wumpus method is correct so for now just shoot north

    for p in percepts:
        if p == 'C':  # if wumpus is hit then reset shootcount
            shootcount = 0

    for p in percepts:
        if p == 'B':  # If the current percept is a pit
            return pit(p, percepts)

    for p in percepts:
        if p == 'U':  # If there is an edge
            return edge(p, percepts)  # may need to include map?

    # bumpcheck clear, move vertically and add move to moves list

    if north == True:
        moves.append('N')
        return 'N'
    else:
        moves.append('S')
        return 'S'







    # if sensor is clear in desired direction, move to desired square and return this, otherwise send to appropriate danger function (what about percepts that don't matter? i.e wumpus to the right, but we are moving down)
    # if we reach bottom, move right once, change up_down to up (1)
    # if we reach top, move righ once, change up_down to down (0)
    # if we reach bottom/top far right corner with no gold, do the same thing but from right to left until you find the gold.

    return 0  # should return a string back to driver to indicate each move

def map(): #uses a 2X2 list to create a dynamic map which contains precept based predictions on rooms



#in the case that there is a G in the percept list, we come here to try to work out getting it. Once we are done here, we trigger escape()
#params: some info (may need more) from the main nav function to help it make its decision, it should also have access to the global map
 def foundGold(p, percepts):
    currentPercept = p
    perceptList = percepts

    return 0





#in the case of an edge, the main movement function sends us here in order to try and get to the next desired tile, takes over for main movement function until it has reached this
#NOTE: We should be able to use the global variable north to tell if we've been previously moving north or south.
#NOTE  For example if we have been moving down, and hit an edge, we can simply check the value of north. If north is false we see that we have been moving down. Then we can change it to true then turn so that it represents that we are now going up.
def edge(p, percepts):
    currentPercept = p
    perceptList = percepts
    global north #important to include these in order to edit global variables
    global east
    global moves
    global map
    print("In edge case")

#cases:
# HIT BOTTOM MOVING DOWN / RIGHT
# 1. moving down (north = False) && moving right (east = True) && last move NOT move right (east): set north to true, return move right,
# 1.a moving down (north = False) && moving right (east = True) && last move WAS move right (east) : return move down   - case for if we are at the step after we have hit the top (our last move was move right), so we simply return go down

#HIT BOTTOM MOVING DOWN / LEFT
# 2. moving down (north = False) && moving left (east = False) && last move NOT move left: set north to true, return move left
# 2a. moving down (north = False) && moving left (east = False) && last move WAS move left: return move down

#HIT TOP MOVING UP / RIGHT
# 3. moving up(north = True) && moving right (east = True) && last move NOT move right: set north to False, return move right
# 3a. moving up(north = True) && moving right (east = True) && last move WAS move right: return move up - case for if we have just previously hit the bottom and moved right, so we want to simply go up

#HIT TOP MOVING UP / LEFT
# 4.)  moving up(north = True) && moving left (east = False) && last move NOT move left: set north to False, return move left
# 4a.)  moving up(north = True) && moving left (east = False) && last move WAS move left: return move up

#HIT CORNER - Good Question

    #1 hit bottom moving right
    if north == False and east == True and moves[-1] != 'E':
        north = True
        moves.append('E')
        return 'E'

    #1a hit top, but just moved left
    if north == False and east == True and moves[-1] == 'E':
        moves.append('S')
        return 'S'

    #2 hit bottom moving left
    if north == False and east == False and moves[-1] != 'W':
        north = True
        moves.append('W')
        return 'W'

    #2a hit top, but just moved right
    if north == False and east == False and moves[-1] == 'W':
        moves.append('S')
        return 'S'

    #3
    if north == True and east == True and moves[-1] != 'E':
        north = False
        moves.append('E')
        return 'E'
#3a
    if north == True and east == True and moves[-1] == 'E':
        moves.append('N')
        return 'N'

    #4
    if north == True and east == False and moves[-1] != 'W':
        north = False
        moves.append('W')
        return 'W'

    #4a
    if north == True and east == False and moves[-1] == 'W':
        moves.append('N')
        return 'N'


# in the case of a pit, the main movement function sends us here in order to try and get to the next desired tile, takes over for main movement function until it has reached this
def pit(p, percepts):
    currentPercept = p
    perceptList = percepts
    global moves
    global breaker
    print("In pit case")

    breaker = breaker + 1

    if breaker > 15:
        return 0

    return 'S'  # temporary


# In the case of a wumpus, mmain movement function sends us here in order to try and kill it.
def wumpus():

    return 0


def escape(): #takes in reverse moves list and flips each direction then adds it to reverse separate list then returns reversed symbol for movement
    revmoves = []
    for i in reversed(moves):
        if moves[i] == 'N':
            moves[i] = 'S'
            revmoves.__add__(moves[i])
        elif moves[i] == 'S':
            moves[i] = 'N'
            revmoves.__add__(moves[i])
        elif moves[i] == 'E':
            moves[i] = 'W'
            revmoves.__add__(moves[i])
        elif moves[i] == 'W':
            moves[i] = 'E'
            revmoves.__add__(moves[i])
    for j in revmoves:
        return revmoves[j]


    

#def gold(): #checks for gold at our feet in move method, then grabs gold if true and proceeds to entrance
    #return 'G'
    #escape()



def foundGold(p, percepts):
    currentPercept = p
    perceptList = percepts

    return 0
