import math
from .coreTypes import cmpxPixelGroup_to_sprite

# Function to print a texture(listOfLines) position colors and such
def drawlib_internal_printmemsprite(texture,posX,posY,colorcode,offsetX=None,offsetY=None):
  if offsetX != None: posX = posX + offsetX
  if offsetY != None: posY = posY + offsetY
  print("\033[s") # Save cursorPos
  c = 0
  OposY = int(posY)
  for line in texture:
    posY = OposY + c
    ANSIprefix = "\033[" + str(posY) + ";" + str(posX) + "H" + "\033[" + str(colorcode) + "m"
    print(ANSIprefix, str(line), "\033[0m")
    c += 1
  print("\033[u\033[2A") # Load cursorPos


# Internal function to generate a texture of a curve, taking center points, radius and character.
def drawlib_internal_draw_curve(center=tuple(), radius=int(), char=str()):
    # Initialize an empty list to store the curve
    rows = []
    # Create a list with the same number of rows and columns as the size of the curve (Nested lists for al cells)
    for _ in range(2*(center[1] + radius) + 1):
        rows.append([" " for _ in range(2*(center[0] + radius) + 1)])
    # Iterate over all angles between 0 and 90 degrees (to only get one quadrant)
    for angle in range(0, 90):
        # Calculate the x and y coordinates of the point on the curve for the current angle
        x = center[0] + int(radius * math.cos(math.radians(angle))) * 2
        y = center[1] + int(radius * math.sin(math.radians(angle)))
        # Set the character of the point at the calculated coordinates
        rows[y][x] = char
    # Join each row of the list into a single string and return it
    return "\n".join("".join(row) for row in rows)


def draw_fillcircle(char,posX,posY,diameter):
  colorcode = "33"
  # Generate a memSprite
  radius = diameter / 2 - .5
  r = (radius + .25)**2 + 1
  memsprite = ""
  for i in range(diameter):
    y = (i - radius)**2
    for j in range(diameter):
      x = (j - radius)**2
      if x + y <= r:
        memsprite = memsprite + f'{char}{char}'
      else:
        memsprite = memsprite + '  '
    memsprite = memsprite + '\n'
  # Print memsprite
  drawlib_internal_printmemsprite( memsprite.split('\n'),posX,posY,colorcode )

# Function that draws a curve at the given cordinates (top-right) taking radius char.
def draw_curve(cordinates=tuple(), radius=int(), char=str(), quadrant=int()):
    flipped_texture = []
    curve_texture = ( drawlib_internal_draw_curve((0,0), radius, char) ).split("\n")
    if quadrant == 1 or quadrant == 4:
        flipped_texture = reversed(curve_texture)
    else:
        flipped_texture = curve_texture
    if quadrant == 4 or quadrant == 3:
        curve_texture = flipped_texture
        flipped_texture = []
        for line in curve_texture:
            line = ''.join(reversed(list(str(line))))
            flipped_texture.append(line)
    flipped_texture = [s for s in flipped_texture if s.strip()]
    drawlib_internal_printmemsprite(flipped_texture,cordinates[0],cordinates[1],"0")

# Pixelstrip
def pixelStrip_to_cmpxPixelGroup(pixelStrip=dict):
    pixels = pixelStrip["po"]
    chars = pixelStrip["st"].split("§;§")
    cmpxPixelGroup = []
    for i,char in enumerate(chars):
        cmpxPixelGroup.append( {"char":char,"pos":pixels[i]} )
    return cmpxPixelGroup

def cmpxPixelGroup_to_pixelStrip(cmpxPixelGroup):
    strip = ""
    _strip = []
    poss = []
    for pGroup in cmpxPixelGroup:
        _strip.append(pGroup["char"])
        poss.append(pGroup["pos"])
    strip = "§;§".join(_strip)
    return {"st":strip,"po":poss}

def render_pixelStrip(pixelStrip=dict,ansi=None):
    cmpxPixelGroup = pixelStrip_to_cmpxPixelGroup(pixelStrip)
    render_cmpxPixelGroup(cmpxPixelGroup,ansi=ansi)

class pixelStrip():
    def __init__(self,strip=None,positions=None,pixelStrip=None, color=None,palette=None):
        if strip != None:
            if isinstance(strip, str) != True: raise ValueError("Strip must be a string!")
        if positions != None:
            if isinstance(positions, list) != True: raise ValueError("Positions must be a list!")
        if pixelStrip != None:
            if isinstance(pixelStrip, list) != True: raise ValueError("PixelStrip must be a dict!")
        self.strip = strip
        self.positions = positions
        if pixelStrip != None:
            self.strip = pixelStrip["st"]
            self.positions = pixelStrip["po"]
        self.ansi = autoNoneColor(color,palette)
    def asPixelGroup(self):
        return self.positions
    def asCmpxPixelGroup(self):
        pixelStrip_to_cmpxPixelGroup({"st":self.strip,"po":self.positions})
    def asSprite(self,exclusionChar=" "):
        cmpxPixelGroup = pixelStrip_to_cmpxPixelGroup({"st":self.strip,"po":self.positions})
        return cmpxPixelGroup_to_sprite(cmpxPixelGroup,exclusionChar)
    def asTexture(self,exclusionChar=" "):
        cmpxPixelGroup = pixelStrip_to_cmpxPixelGroup({"st":self.strip,"po":self.positions})
        sprite = cmpxPixelGroup_to_sprite(cmpxPixelGroup,exclusionChar)
        return sprite["xPos"],sprite["yPos"],sprite_to_texture(sprite)
    def asPixelStrip(self):
        return {"st":self.strip,"po":self.positions}
    def draw(self):
        render_pixelStrip(pixelStrip,self.ansi)