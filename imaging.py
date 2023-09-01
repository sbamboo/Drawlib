from .imageRenderer.ImageRenderer_Beta import ImageRenderer
from .coreTypes import render_listTexture,render_textureAlt,_join_with_delimiter

class asciiImage():
    def __init__(self,imagePath=str,mode="standard",char=None,pc=False,method="lum",invert=False,monochrome=False,width=None,height=None,resampling="lanczos",textureCodec=None,xPos=None,yPos=None,strTxtMethod=False):
        # Req Arguments
        self.imagePath = imagePath
        # Presets
        self.rentype = "ascii"
        self.texture = None
        # Set other arguments
        self.mode = mode
        self.char = char
        self.pc = pc
        self.method = method
        self.invert = invert
        self.monochrome = monochrome
        self.width = width
        self.height = height
        self.resampling = resampling
        self.textureCodec = textureCodec
        self.xPos = xPos
        self.yPos = yPos
        self.strTxtMethod = strTxtMethod
    def _getTexture(self,asTexture=True,delimitChars=False):
        if self.strTxtMethod == True:
            self.texture = _join_with_delimiter(ImageRenderer(image=self.imagePath,rentype=self.rentype,mode=self.mode,char=self.char,pc=self.pc,method=self.method,invert=self.invert,monochrome=self.monochrome,width=self.width,height=self.height,resampling=self.resampling,textureCodec=self.textureCodec, asTexture=asTexture,colorMode="pythonAnsi",delimitChars=delimitChars),"\n")
        else:
            self.texture = ImageRenderer(image=self.imagePath,rentype=self.rentype,mode=self.mode,char=self.char,pc=self.pc,method=self.method,invert=self.invert,monochrome=self.monochrome,width=self.width,height=self.height,resampling=self.resampling,textureCodec=self.textureCodec, asTexture=asTexture,colorMode="pythonAnsi",delimitChars=delimitChars)
    def resize(self,width=int,height=int,resampling=None):
        if resampling != None: self.resampling = resampling
        self.width = width
        self.height = height
        self.texture = None
    def print(self):
        self._getTexture(asTexture=False)
        self.texture = None
    def asTexture(self):
        if self.texture == None: self._getTexture()
        return self.texture
    def asSplitPixelGroup(self,xOverride=None,yOverride=None):
        oldt = self.texture
        self._getTexture(delimitChars=True)
        newt = self.texture
        self.texture = oldt
        splitPixelGroup = {"ch":[],"po":[]}
        for li,line in enumerate(newt):
            sline = line.split(";delim;")
            for ci,char in enumerate(sline):
                splitPixelGroup["ch"].append(char)
                xPos,yPos = 0,0
                if self.xPos != None: xPos = self.xPos
                if self.yPos != None: yPos = self.yPos
                if xOverride != None: xPos += xOverride
                if yOverride != None: yPos += yOverride
                splitPixelGroup["po"].append([ci+xPos,li+yPos])
        return splitPixelGroup
    def draw(self,xPos=None,yPos=None,altrenmethod=False):
        if xPos == None: xPos = self.xPos
        if xPos == None: raise ValueError("xPos not defined!")
        if yPos == None: yPos = self.yPos
        if yPos == None: raise ValueError("yPos not defined!")
        if self.texture == None: self._getTexture()
        if self.strTxtMethod == True:
            render_textureAlt(xPos,yPos,self.texture)
        else:
            render_listTexture(xPos,yPos,self.texture)
        return self

class boxImage():
    def __init__(self,imagePath=str,mode="foreground",char=None,monochrome=False,width=None,height=None,resampling="lanczos",method=None,textureCodec=None,xPos=None,yPos=None,strTxtMethod=False):
        # Req Arguments
        self.imagePath = imagePath
        # Presets
        self.rentype = "box"
        self.texture = None
        # Set other arguments
        self.mode = mode
        self.char = char
        self.monochrome = monochrome
        self.width = width
        self.height = height
        self.resampling = resampling
        self.textureCodec = textureCodec
        self.xPos = xPos
        self.yPos = yPos
        self.method = method
        self.strTxtMethod = strTxtMethod
    def _getTexture(self,asTexture=True,delimitChars=False):
        if self.strTxtMethod == True:
            self.texture = _join_with_delimiter(ImageRenderer(image=self.imagePath,rentype=self.rentype,mode=self.mode,char=self.char,monochrome=self.monochrome,width=self.width,height=self.height,resampling=self.resampling,textureCodec=self.textureCodec,method=self.method, asTexture=asTexture,colorMode="pythonAnsi",delimitChars=delimitChars),"\n")
        else:
            self.texture = ImageRenderer(image=self.imagePath,rentype=self.rentype,mode=self.mode,char=self.char,monochrome=self.monochrome,width=self.width,height=self.height,resampling=self.resampling,textureCodec=self.textureCodec,method=self.method, asTexture=asTexture,colorMode="pythonAnsi",delimitChars=delimitChars)
    def resize(self,width=int,height=int,resampling=None):
        if resampling != None: self.resampling = resampling
        self.width = width
        self.height = height
        self.texture = None
    def print(self):
        self._getTexture(asTexture=False)
        self.texture = None
    def asTexture(self):
        if self.texture == None: self._getTexture()
        return self.texture
    def asSplitPixelGroup(self,xOverride=None,yOverride=None):
        oldt = self.texture
        self._getTexture(delimitChars=True)
        newt = self.texture
        self.texture = oldt
        splitPixelGroup = {"ch":[],"po":[]}
        for li,line in enumerate(newt):
            sline = line.split(";delim;")
            for ci,char in enumerate(sline):
                splitPixelGroup["ch"].append(char)
                xPos,yPos = 0,0
                if self.xPos != None: xPos = self.xPos
                if self.yPos != None: yPos = self.yPos
                if xOverride != None: xPos += xOverride
                if yOverride != None: yPos += yOverride
                splitPixelGroup["po"].append([ci+xPos,li+yPos])
        return splitPixelGroup
    def draw(self,xPos=None,yPos=None):
        if xPos == None: xPos = self.xPos
        if xPos == None: raise ValueError("xPos not defined!")
        if yPos == None: yPos = self.yPos
        if yPos == None: raise ValueError("yPos not defined!")
        if self.texture == None: self._getTexture()
        if self.strTxtMethod == True:
            render_textureAlt(xPos,yPos,self.texture)
        else:
            render_listTexture(xPos,yPos,self.texture)
        return self
        