import os
from .coreTypes import render_texture
from .coloring import autoNoneColor,standardPalette

class buffer():
    # INIT
    def __init__(self,sizeX,sizeY,autoMake=False):
        #vars
        columns, rows = os.get_terminal_size()
        self.createdScreenSize = (columns, rows)
        self.bufferSize = (None,None)
        self.buffer = None
        #sizeX
        if sizeX != None:
            if type(sizeX) != int:
                raise TypeError("If sizeX is defined it must be an int!")
            else:
                self.bufferSize[0] = sizeX
        else:
            self.bufferSize[0] = columns
        #sizeY
        if sizeY != None:
            if type(sizeY) != int:
                raise TypeError("If sizeY is defined it must be an int!")
            else:
                self.bufferSize[1] = sizeY
        else:
            self.bufferSize[1] = rows
        #automake
        if autoMake == True:
            self.make()
    # make
    def make(self):
        self.buffer = []
        for _ in range(self.bufferSize[1]):
            line = []
            for _ in range(self.bufferSize[0]):
                line.append(" ")
            self.buffer.append(line)
    def unmake(self):
        self.buffer = None
    #gets
    def getLine(self,y):
        return self.buffer[y-1]
    def getChar(self,x,y):
        return self.buffer[y-1][x-1]
    def getBuffer(self):
        return self.buffer
    def getBufferWJS(self) -> list:
        '''With joined strings'''
        wjsBuffer = []
        for line in self.buffer:
            wjsBuffer.append("".join(line))
        return wjsBuffer
    def getBufferAS(self) -> str:
        '''As string'''
        wjsBuffer = []
        for line in self.buffer:
            wjsBuffer.append("".join(line))
        return "\n".join(wjsBuffer)
    #set
    def setPoint(self,char=int,x=int,y=int):
        self.buffer[y-1][x-1] = char
    def setLine(self,line=str,y=int):
        self.buffer[y-1] = list(line)
    def setLineFl(self,line=list,y=int):
        self.buffer[y-1] = line
    # clear
    def clearPoint(self,x=int,y=int):
        self.setPoint(" ",x,y)
    def clearLine(self,y=int):
        self.setLine(" "*self.bufferSize[0],y=y)
    # draw
    def drawBuffer(self,xPos=0,yPos=0,color=None,palette=standardPalette):
        ansi = autoNoneColor(color, palette)
        fl = self.setLineFl()
        render_texture(xPos,yPos,texture=fl,ansi=ansi)