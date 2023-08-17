from .imageRenderer.ImageRenderer_Beta import ImageRenderer
from .coreTypes import render_texture

class asciiImage():
    def __init__(self,imagePath=str,mode="standard",char=None,pc=False,method="lum",invert=False,monochrome=False,widht=None,height=None,resampling="lanczos",textureCodec=None):
        # Req Arguments
        self.imagePath = imagePath
        # Presets
        self.type = "ascii"
        self.texture = None
        # Set other arguments
        self.mode = mode
        self.char = char
        self.pc = pc
        self.method = method
        self.invert = invert
        self.monochrome = monochrome
        self.widht = widht
        self.height = height
        self.resampling = resampling
        self.textureCodec = textureCodec
    def _getTexture(self,asTexture=True):
        self.texture = ImageRenderer(image=self.imagePath,type=self.type,mode=self.mode,char=self.char,pc=self.pc,method=self.method,invert=self.invert,monochrome=self.monochrome,width=self.widht,height=self.height,resampling=self.resampling,textureCodec=self.textureCodec, asTexture=asTexture,colorMode="pythonAnsi")
    def resize(self,width=int,height=int,resampling=None):
        if resampling != None: self.resampling = resampling
        self.widht = width
        self.height = height
        self.texture = None
    def print(self):
        self._getTexture(asTexture=False)
        self.texture = None
    def asTexture(self):
        if self.texture == None: self._getTexture()
        return self.texture
    def draw(self,xPos=int,yPos=int):
        if self.texture == None: self._getTexture()
        render_texture(xPos,yPos,texture)

class boxImage():
    def __init__(self,imagePath=str,mode="foreground",char=None,monochrome=False,widht=None,height=None,resampling="lanczos",textureCodec=None):
        # Req Arguments
        self.imagePath = imagePath
        # Presets
        self.type = "box"
        self.texture = None
        # Set other arguments
        self.mode = mode
        self.char = char
        self.monochrome = monochrome
        self.widht = widht
        self.height = height
        self.resampling = resampling
        self.textureCodec = textureCodec
    def _getTexture(self,asTexture=True):
        self.texture = ImageRenderer(image=self.imagePath,type=self.type,mode=self.mode,char=self.char,monochrome=self.monochrome,width=self.widht,height=self.height,resampling=self.resampling,textureCodec=self.textureCodec, asTexture=asTexture,colorMode="pythonAnsi")
    def resize(self,width=int,height=int,resampling=None):
        if resampling != None: self.resampling = resampling
        self.widht = width
        self.height = height
        self.texture = None
    def print(self):
        self._getTexture(asTexture=False)
        self.texture = None
    def asTexture(self):
        if self.texture == None: self._getTexture()
        return self.texture
    def draw(self,xPos=int,yPos=int):
        if self.texture == None: self._getTexture()
        render_texture(xPos,yPos,texture)