class Room(object):

    def __init__(self, x, y, visited, stench, breeze, safe):
        self.x = x
        self.y = y
        self.visited = visited
        self.stench = stench
        self.breeze = breeze
        self.safe = safe

    def setX(self, xnum):  # position coordinates
        self.x = xnum

    def getX(self):
        return self.x

    def setY(self, ynum):
        self.y = ynum

    def getY(self):
        return self.y

    def setVisited(self, visited):  # boolean value
        self.visited = visited

    def getVisited(self):
        return self.visited

    def setStench(self,
                  stench):  # stench, breeze, wumpus will consist of an integer point value that will reflect the chances of any of these in the specific room
        self.stench += stench

    def getStench(self):
        return self.stench

    def setBreeze(self, breeze):
        self.breeze += breeze

    def getBreeze(self):
        return self.breeze