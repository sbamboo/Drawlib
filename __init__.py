from . import assets
from . import coloring
from . import coreTypes
from . import legacy
from . import linedraw
from . import pointGroupAlgorithms
from . import basicShapes
from . import objects
from . import SimpleSpriteRenderer
from . import tools
from . import tui
from . import imaging
from . import manip
from . import generators

fill_terminal = linedraw.fill_terminal
reset_write_head = linedraw.reset_write_head
stdpalette = coloring.getStdPalette()
baseGenerator = generators.baseGenerator
repeatGenerator = generators.repeatGenerator
numberGenerator = generators.numberGenerator
rainbowGenerator = generators.rainbowGenerator
rainbowGeneratorZero = generators.rainbowGeneratorZero

class DrawlibRenderer():
    def __init__(self):
        self.assets = assets
        self.coloring = coloring
        self.coreTypes = coreTypes
        self.legacy = legacy
        self.linedraw = linedraw
        self.pointGroupAlgorithms = pointGroupAlgorithms
        self.basicShapes = basicShapes
        self.objects = objects
        self.simpleSpriteRenderer = SimpleSpriteRenderer
        self.tools = tools
        self.tui = tui
        self.stdpalette = stdpalette
        self.fill_terminal = linedraw.fill_terminal
        self.reset_write_head = linedraw.reset_write_head
        self.imaging = imaging
        self.manip = manip
        self.baseGenerator = baseGenerator
        self.repeatGenerator = repeatGenerator
        self.numberGenerator = numberGenerator
        self.rainbowGenerator = rainbowGenerator
        self.rainbowGeneratorZero = rainbowGeneratorZero
