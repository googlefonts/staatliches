# Render this specimen GIF with DrawBot3: http://www.drawbot.com/

import math
import os

# Basic variables  (width, height, margin, frame-count ):
W, H, M, F = 1024, 1024, 128, 32

# Load font and print font info:
os.chdir("..")
os.chdir("..")
font("fonts/Staatliches-Regular.ttf")
#for axis, data in listFontVariations().items():
#    print((axis, data))  # Get axis info from font

# Grid drawn from a given increment:
def grid(inc):
    stroke(0.3)  # Set grid line color
    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX  # Set position for next gridline
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY  # Set position for next gridline

# Page loop
newPage(W, H)
fill(0)           # Background color
rect(0, 0, W, H)  # Draw the background

# Draw the grid (uncomment next line)
#grid(32)

# Basic Style
stroke(None)
fill(1)
lineSpaceA = 24
lineSpaceB = 21
startPointA = 900
startPointB = 784



#draw main
fontSize(90)
tracking(0)

# Draw large text
fill(1, 0.1, 0)
text("STAATLICHES", (M, (startPointA)-(lineSpaceA*2)))
fill(0,0.5,1)
text("BAUHAUS", (M, (startPointA)-(lineSpaceA*5)))
fill(1,0.1,0)
text("IN WEIMAR", (M, (startPointA)-(lineSpaceA*8)))
fill(0,0.5,1)
text("1919—1923", (M, (startPointA)-(lineSpaceA*11)))
#text("1919—1923", (M, (startPointA)-(lineSpaceA*14)))

tracking(0)
fill(1)
text(" ABCDEFGHIJ", (M+379, (startPointA)-(lineSpaceA*2)))
text(" KLMNOPQRSTUV", (M+265, (startPointA)-(lineSpaceA*5)))
text(" WXYZ12345678", (M+303, (startPointA)-(lineSpaceA*8)))
text(" 90!?@$%&.,:;*", (M+326, (startPointA)-(lineSpaceA*11)))

fontSize(48)
tracking(2)
text("AÁĂÂÄÀĀĄÅǺÃÆǼBCĆČÇĈĊDÐĎĐĊDÐĎĐEÉĔ", (M, (startPointB)-(lineSpaceB*13)))
text("ĚÊËĖÈĒĘFGĞĜĢĠHĦȞĤIĬĮĨJĴKĶLĹĽĻĿŁMNŃŇ", (M, (startPointB)-(lineSpaceB*16)))
text("ŅŊÑOÓŎÔÖÒŐŌØǾÕŒPÞQRŔŘŖSŚŠŞŜȘTŦŤŢ", (M, (startPointB)-(lineSpaceB*19)))
text("ȚUÚŬÛÜÙŰŪŲŮŨVWẂŴẄẀXYÝŶŸỲZŹŽŻ!¡?¿¦", (M, (startPointB)-(lineSpaceB*22)))
text("", (M, (startPointB)-(lineSpaceB*25)))
text("½¼¾(){}[]_-–—“”‘’¢$€ƒ£¥+−×÷=≠∞◊¶", (M, (startPointB)-(lineSpaceB*25)))
text("§©®™°†‡", (M, (startPointB)-(lineSpaceB*28)))


t = FormattedString()
# set a font
t.font("fonts/Staatliches-Regular.ttf")
# set a font size
t.fill(1)
t.tracking(2)
t.fontSize(48)
# add some glyphs by glyph name
t.appendGlyph("A.alt1", "A.alt2", "Eng", "S.alt1", "germandbls", "zero.zero", "numbersign",)
# draw the formatted string
text(t, (304, 194))


# Save GIF
os.chdir("docs")
os.chdir("images")
saveImage("basic-specimen.gif")
os.chdir("..")
#os.chdir("sources")
