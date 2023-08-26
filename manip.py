def fillShape(texture=list,backgroundChar=" ",fillChar=str):
    nTex = []
    for line in texture:
        sline = list(line)
        si = None
        ei = None
        nline = ""
        chars = []
        for i,char in enumerate(sline):
            if char != backgroundChar:
                chars.append(i)
        si = min(chars)
        ei = max(chars)
        indexes = list(range(si + 1, ei))
        for index in indexes:
            if 0 <= index < len(sline):
                sline[index] = fillChar
        nline = ''.join(sline)
        nTex.append(nline)
    return nTex

def stretchShape(texture=list, backgroundChar=""):
    doubled_texture = []

    for line in texture:
        doubled_line = ""
        for i, char in enumerate(line):
            if char in backgroundChar:
                # Check left and right characters for edge preservation
                left_char = line[i - 1] if i > 0 else ' '
                right_char = line[i + 1] if i < len(line) - 1 else ' '

                # Determine the character to use for preserving edges
                edge_char = char if left_char in backgroundChar or right_char in backgroundChar else ' '
                doubled_line += edge_char * 2
            else:
                # Double the non-empty characters
                doubled_line += char * 2
        doubled_texture.append(doubled_line)
    return doubled_texture

def fillShapeObj(shapeObj):
    pass

def stretchShapeObj(shapeObj):
    pass