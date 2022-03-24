# Definities voor de p5py-bibliotheek 
from processing import *
import __main__

# Vormgeving
from processing import rectMode as rect_mode
from processing import ellipseMode as ellipse_mode
from processing import strokeWeight as stroke_weight
from processing import strokeCap as stroke_cap
from processing import strokeJoin as stroke_join
from processing import noStroke as no_stroke
from processing import noFill as no_fill

# Lettertypen
from processing import createFont as create_font
from processing import loadFont as load_font
from processing import textFont as text_font

# Tekst
from processing import textAlign as text_align
from processing import textLeading as text_leading
from processing import textMode as text_mode
from processing import textSize as text_size
from processing import textWidth as text_width

# Kleur
from processing import blendColor as blend_color
from processing import lerpColor as lerp_color
from processing import color as Color
  
# Afbeeldingen
from processing import createImage as create_image
from processing import imageMode as image_mode
from processing import loadImage as load_image
from processing import noTint as no_tint
from processing import requestImage as request_image

# Omgeving
from processing import frameRate as frame_rate
from processing import noCursor as no_cursor
from processing import noLoop as no_loop

# Omzetten
from processing import applyMatrix as apply_matrix
from processing import popMatrix as pop_matrix
from processing import printMatrix as print_matrix
from processing import pushMatrix as push_matrix
from processing import resetMatrix as reset_matrix
from processing import rotateX as rotate_x
from processing import rotateY as rotate_y
from processing import pushStyle as push_style
from processing import popStyle as pop_style

from processing import run as main_run

# Toetsenbord

def mousePressed():
  if hasattr(__main__, "muis_ingedrukt"):
    muis_ingedrukt = getattr(__main__, "muis_ingedrukt")
    muis_ingedrukt()
    
def mouseReleased():
  if hasattr(__main__, "muis_losgelaten"):
    muis_losgelaten = getattr(__main__, "muis_losgelaten")
    muis_losgelaten()
  
__main__.muis_x = 0
__main__.muis_y = 0
__main__.muis_px = 0
__main__.muis_py = 0
__main__.frame_count = 0
__main__.frame_rate = 60

def mouseMoved():
  __main__.muis_x = muis.x
  __main__.muis_y = muis.y
  __main__.muis_px = muis.px
  __main__.muis_py = muis.py
  if hasattr(__main__, "muis_verplaatst"):
    muis_verplaatst = getattr(__main__, "muis_verplaatst")
    muis_verplaatst()

def mouseDragged():
  if hasattr(__main__, "muis_gesleept"):
    muis_gesleept = getattr(__main__, "muis_gesleept")
    muis_gesleept()

def new_draw():
  __main__.frame_count = frameCount
  frameRate = __main__.frame_rate
  old_draw()
  
def run():
  global old_draw
  old_draw = __main__.draw
  __main__.draw = new_draw
  main_run()
  
def raster():
  pushMatrix()
  stroke(200)
  fill(0)
  line(0, height/2, width, height/2)
  line(width/2, 0, width/2, height)
  x_coords = [0, width/2, width]
  y_coords = [0, height/2, height]
 
  for x in x_coords:
    for y in y_coords:
      toon_coordinaten(x, y)

  popMatrix()

def toon_coordinaten(x, y):
  if x == width:
    x_align = RIGHT
  elif x == 0:
    x_align = LEFT
  else:
    x_align = CENTER
  
  if y == height:
    y_align = BASELINE
  elif y == 0:
    y_align = TOP
  else:
    y_align = CENTER
    
  pushStyle()
  fill(100)
  text_align(x_align, y_align)
  text('(' + str(int(x)) + ', ' + str(int(y)) + ')', x, y)
  popStyle()
