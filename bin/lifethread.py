"""
Class for the life calculating thread.
"""

from threading import Thread

ALIVE = 1
DEAD = 0


class LifeThread(Thread):
    def __init__(self, grid, sizeX, sizeY):
        """ Constructor """
        Thread.__init__(self)
        self.grid = grid
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.newGrid = self.grid.copy()

    def run(self):
        """ Work done here """
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                total = (self.grid[i, (j - 1) % self.sizeX] + self.grid[i, (j + 1) % self.sizeX] +
                         self.grid[(i - 1) % self.sizeY, j] + self.grid[(i + 1) % self.sizeY, j] +
                         self.grid[(i - 1) % self.sizeY, (j - 1) % self.sizeX] + self.grid[
                             (i - 1) % self.sizeY, (j + 1) % self.sizeX] +
                         self.grid[(i + 1) % self.sizeY, (j - 1) % self.sizeX] + self.grid[
                             (i + 1) % self.sizeY, (j + 1) % self.sizeX])
                if self.grid[i, j] == ALIVE:
                    if (total < 2) or (total > 3):
                        self.newGrid[i, j] = DEAD
                else:
                    if total == 3:
                        self.newGrid[i, j] = ALIVE

    def join(self, timeout=None):
        Thread.join(self)
        return self.newGrid
