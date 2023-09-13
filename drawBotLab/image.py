from drawBot import *

def scaledImage(imagePath, x, y, w=None, h=None):
    """
    Draw an image at a specific location
    and size instead of scaling and 
    translating everytime.
    """
    iw,ih = imageSize(imagePath)

    t = True
    if w and h:
        fx = w/iw
        fy = h/ih
    if not w and not h:   
        t = False
        w,h = iw,ih
        fx = fy = 1
    elif not h:
        # allow proportional scaling
        h = w
        fy = fx = w/iw
    elif not w:
        # allow proportional scaling
        w = h
        fx = fy = h/ih
    
    # get opposite scaler for translation
    opx = 1/fx
    opy = 1/fy

    with savedState():
        scale(fx,fy)        
        if t:
            translate((x * opx),(y * opy))
        image(imagePath,(x,y))