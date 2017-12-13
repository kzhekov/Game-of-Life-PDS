class Cell():
    def __init__(self, x, y, live=True):
        self.x, self.y = x, y
        self.live = live
        self.around = 0

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def spawn(self):
        self.live = True
        self.around = 0
        return self

class Grid():
    def __init__(self, width, height):
        self.xMax = width
        self.yMax = height
        self.cells = []
        self.deltas = [(-1, -1), (0, -1), (1, -1), (1, 0),
                      (1, 1), (0, 1), (-1, 1), (-1, 0)]

    def tick(self):
        newCells = self.cells[:]
        ''' create potential new cells '''
        for cell in self.cells:
            for dx, dy in self.deltas:
                newCell = Cell((cell.x+dx)%self.xMax,
                               (cell.y+dy)%self.yMax, live=False)
                if newCell not in newCells:
                    newCells.append(newCell)
                newCells[newCells.index(newCell)].around += 1
        ''' spawn new cells for next grid '''
        self.cells = []
        for cell in newCells:
            if (cell.live and cell.around in [2, 3]
            or not cell.live and cell.around == 3):
                self.cells.append(cell.spawn())